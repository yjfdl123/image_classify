#encoding=utf-8
from db_wrap import DbManu 
from model import ImageModel

db_agent = None 
model_agent = None 

def get_db_agent():
    global db_agent
    if db_agent == None: 
        db_agent = DbManu() 
        db_agent.create_table()
    return db_agent

def get_model_agent():
    global model_agent
    if model_agent == None: 
        model_agent = ImageModel() 
        model_agent.load_model()
    return model_agent 
