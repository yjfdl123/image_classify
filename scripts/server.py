#encoding=utf-8

from flask import Flask, request
import flask
import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request

import data_center
import config 

app=Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
PEOPLE_FOLDER = os.path.join('static', 'upload_image')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
db_agent = data_center.get_db_agent()
model_agent = data_center.get_model_agent()

 
@app.route('/')
def hello_flask():
    print(  os.getcwd())
    return "<h1>Welcome to use Apple Image Detect System!</h1>"

@app.route('/upload_photo', methods=['POST'])
def update_photo():
    result = {'success': False}
    print("request:", request.form)
    label = request.form.get("label", type=str,default=None)
    if label != "OK" and label != "NEG":
        return {"ret": "fail", "info": "label error"}
    upload_file = request.files['file']
    file_name = upload_file.filename
    save_dir = config.DIR_UPLOAD_DATA + "/" + label
    if upload_file:
        file_paths = os.path.join(save_dir, file_name)
        upload_file.save(file_paths)
        return {"ret":"ok"}
    return result


@app.route("/predict", methods=["POST"])
def predict():
    result = {'success': False}
    if request.method == 'POST':
        upload_file = request.files['file']
        file_name = upload_file.filename
        save_dir = config.DIR_PREDICT_DATA 
        static_dir = config.DIR_STATIC_IMG
        if upload_file:
            save_path = os.path.join(save_dir, file_name)
            upload_file.save(save_path)
            static_save_path = os.path.join(static_dir, file_name)
            print("savepath:", static_save_path)
            upload_file.save(static_save_path)
            model_name, model_version, prob = model_agent.predict_image(save_path)
            result['predictions'] = [str(prob)]
            result['success'] = True
            db_agent.insert_image_score(file_name, model_name, prob)
    return flask.jsonify(result)

@app.route("/train", methods=["GET"])
def train_model():
    result = {'success': False}
    if request.method == 'GET':
        model_name, model_version =  model_agent.finetune_model()
        db_agent.insert_model_version(model_name, model_version)
        result['op'] = "retrain"
        result['success'] = True
    return flask.jsonify(result)

@app.route("/metadata", methods=["GET"])
def get_metadata():
    result = {'success': False}
    if request.method == 'GET':
        ret = db_agent.select_model_version()
        result['result'] = ret
        result['op'] = "metadata"
        result['success'] = True
    return flask.jsonify(result)

@app.route("/history", methods=["GET"])
def get_history():
    result = {'success': False}
    if request.method == 'GET':
        lst_score, lst_image_name = db_agent.select_image_score()
        result['result'] = lst_score
        result['op'] = "history"
        result['success'] = True
        lst_image_path = []
        for name in lst_image_name:
            user_image = os.path.join(app.config['UPLOAD_FOLDER'], name)
            print("user_image:", user_image)
            lst_image_path.append(user_image )

        user_image = os.path.join(app.config['UPLOAD_FOLDER'], '07.jpg')
        return render_template('tables.html',  name="yjf", lst_score = lst_score, user_image = user_image, lst_image_name=lst_image_path)
    return flask.jsonify(result)

 
if __name__=='__main__':
    app.debug=True
    #app.run(host='127.0.0.1',port=5000)
    app.run(host='0.0.0.0',port=config.SERVER_PORT)


