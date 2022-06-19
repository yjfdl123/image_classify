#encoding=utf-8
## func: db manu
import sqlite3
import config 

class DbManu(object):
    def __init__(self):
        self.db_name = config.DIR_DATABASE +  "/image_rec.db"
        print("db_name:", self.db_name)
        self.db_category = "sqllite3"
        if self.db_category == "sqllite3":
            self.conn =  sqlite3.connect(self.db_name, check_same_thread=False)
            self.cursor = self.conn.cursor()


    def create_table(self):
        """ 
        """
        if self.db_category == "sqllite3":
            sql = '''
                create table if not exists model_version (
                    model_name text, 
                    model_version text
                )
            '''
            self.cursor.execute(sql)
            print("create suc")

            sql = ''' 
                create table if not exists predict_score (
                    imagename text, 
                    model_name text, 
                    score real
                )
            '''
            self.cursor.execute(sql)
            print("create img_score suc")

    def insert_model_version(self, model_name, model_version):
        sql = ''' insert into model_version
                  (model_name, model_version)
                  values
                  (:model_name, :model_version)'''
        self.cursor.execute(sql,{'model_name':model_name, 'model_version':model_version})
        self.conn.commit()

    def insert_image_score(self, imagename, model_name, score):
        sql = ''' insert into predict_score
                  (imagename, model_name, score)
                  values
                  (:imagename, :model_name, :score)'''
        self.cursor.execute(sql,{'imagename':imagename, 'model_name':model_name, 'score':score})
        self.conn.commit()

    def select_model_version(self):
        sql = '''select * from model_version'''
        results = self.cursor.execute(sql)
        all_version = results.fetchall()
        ret = []
        for version in all_version:
            print(version)
            ret.append(version)
        return ret 

    def select_image_score(self, imagename = None):
        if imagename:
            sql = "select * from predict_score where imagename = '%s'" % (imagename)
        else:
            sql = "select * from predict_score"
        results = self.cursor.execute(sql)
        all_scores = results.fetchall()
        dic_iamge_name = {}
        lst_score = []
        for score in all_scores:
            print(score)
            lst_score.append(score)
            imagename = score[0]
            if not imagename in dic_iamge_name:
                dic_iamge_name[imagename] = 1
        lst_score.sort(key = lambda x:x[0]+x[1])
        lst_image_name = dic_iamge_name.keys()
        return lst_score, lst_image_name


if __name__ == "__main__":
    obj = DbManu()
    obj.insert_model_version("model_v3", "v4")
    obj.insert_model_version("model_v3", "v5")
    obj.select_model_version()

    # obj.create_table()
    obj.insert_image_score("1.jpg", "model_v2", 4.5)
    obj.insert_image_score("1.jpg", "model_v3", 8.0)
    obj.insert_image_score("1.jpg", "model_v4", 10.0)
    obj.insert_image_score("2.jpg", "model_v4", 10.0)
    obj.select_image_score("2.jpg")

    