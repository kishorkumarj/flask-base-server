import os

DEBUG = True
TESTING = True
DEVELOPMENT = False

SECRET_KEY = os.environ.get('SECRET_KEY', "o$#d$yq8yj7@ow(u=z_m2gnn95k&==wo3)6-c2y#nhdh+lb4e1")
USE_X_SENDFILE = True
