import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    
    SECRET_KEY = os.getenv('SECRET_KEY', "o$#d$yq8yj7@ow(u=z_m2gnn95k&==wo3)6-c2y#nhdh+lb4e1")
    USE_X_SENDFILE = True
    
class DevConfig(Config):
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True