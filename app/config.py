import os 
from dotenv import load_dotenv
class Config:
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True  # Set to False in production
    STATIC_FOLDER = 'src/static'
    TEMPLATES_FOLDER = 'src/templates'
    
a=Config() 
