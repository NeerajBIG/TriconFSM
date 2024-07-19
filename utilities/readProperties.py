import configparser
import os

config = configparser.RawConfigParser()
config.read("C:/Users/neera/PycharmProjects/TriconFSM/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url1 = config.get('common data','baseURL')
        return url1

    @staticmethod
    def getUserEmai():
        username = config.get('common data', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def basePath():
        path = os.path.dirname(os.path.abspath(__file__))
        path = path.rsplit('\\', 1)[0]
        path = path.replace('\\', '/')
        return path