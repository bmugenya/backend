import os,random, string

class Config(object):
    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY')

    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))   

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    CLOUDINARY_URL=os.getenv('CLOUDINARY_URL')
    USE_CORS = True
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_HEADERS = 'Content-Type'
        


class ProductionConfig(Config):
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
 

# Load all possible configurations
configurations = {
    'production': ProductionConfig,
    'development': DevelopmentConfig
}