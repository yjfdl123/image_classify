#encoding=utf-8
## function: client

import requests
import base64, os
import config 
import sys 

def upload_image(imagepath, label):
    # API address
    url = "http://%s:%s/upload_photo" % (config.SERVER_IP, config.SERVER_PORT)
    file_name = imagepath.split("/")[-1] 
    file=open(imagepath,'rb')
    files = {'file':(file_name,file,'image/jpg')}

    d = {"label": label}
    r = requests.post(url,files = files, data=d)
    result = r.content
    print("ret:", result)


def predict_image(imagepath):
    url = "http://%s:%s/predict" % (config.SERVER_IP, config.SERVER_PORT)
    file_name = imagepath.split("/")[-1] 
    file=open(imagepath,'rb')
    files = {'file':(file_name,file,'image/jpg')}
    r = requests.post(url,files = files)
    result = r.content
    print("ret:", result)

def train_model():
    url = "http://%s:%s/train" % (config.SERVER_IP, config.SERVER_PORT)
    r = requests.get(url)
    result = r.content
    print("ret:", result)

def get_metadata():
    url = "http://%s:%s/metadata" % (config.SERVER_IP, config.SERVER_PORT)
    r = requests.get(url)
    result = r.content
    print("ret:", result)

def get_history():
    url = "http://%s:%s/history" % (config.SERVER_IP, config.SERVER_PORT)
    r = requests.get(url)
    result = r.content
    print("ret:", result)

def helper():
    print("Welcome to use image_client!")
    print("used operations :")
    print("python3 client.py metadata")
    print("python3 client.py history")
    print("python3 client.py train")
    print("python3 client.py predict  your_path_image")
    print("python3 client.py upload_image your_path_image label(OK|NEG)")


if __name__ == "__main__":
    if len(sys.argv) <= 1: 
        print("pls input params: 1)opration 2)imagepath(optional)")
        exit(-1)
    operation = sys.argv[1]
    if operation=="predict" :
        if len(operation)<=2:
            print("pls input image path!")
            exit(-1)
    if operation == "upload_image":
        if len(operation)<=3:
            print("pls input image path; image label(NEG|OK)!")
            exit(-1)

    imagepath = None
    imagelabel = None
    if operation == "metadata":
        get_metadata()
    elif operation == "history":
        get_history()
    elif operation == "train":
        train_model() 
    elif operation == "predict":
        imagepath = sys.argv[2]
        predict_image(imagepath)
    elif operation == "upload_image":
        imagepath = sys.argv[2]
        imagelabel = sys.argv[3]
        if imagelabel not in ["NEG", "OK"]:
            print("pls input right label; (OK|NEG)")
            exit(-1)
        upload_image(imagepath, imagelabel)
    elif operation == "help":
        helper()
    else:
        print("Wrong operation:%s\n use help" % (operation))

       