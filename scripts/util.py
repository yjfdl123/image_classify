#encoding=utf-8
import datetime
import sys, os

db_agent = None

def get_hour_str(delta=0):
    """[summary]

    Args:
        delta (int, optional): [description]. Defaults to 0.
    """
    yesterday = datetime.datetime.today() + datetime.timedelta(delta)
    yesterday_format = yesterday.strftime('%m%d_%H%M')
    return yesterday_format

if __name__ == "__main__":
#    print( get_root_path())
    print(get_hour_str())