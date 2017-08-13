import os
port=8000
BASE_DIR=os.path.dirname(__file__)
settings={
    "tempalte_path":os.path.join(BASE_DIR,'templates'),
    "static_path":os.path.join(BASE_DIR,'statics'),
    "debug":True,
}




