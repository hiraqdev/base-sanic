import dotenv
from os import environ
from os.path import join, dirname

class Settings(object):

    def __init__(self, filename='.env'):
        envpath = join(dirname(__file__), filename)
        dotenv.load_dotenv(envpath)

        self.SECRET_KEY = environ.get('SECRET_KEY')

