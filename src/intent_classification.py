from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import getenv
import pandas as pd

class IntentClassification:
    def __init__(self):
        pass

    def get_train_data(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() 
        drive = GoogleDrive(gauth)
        downloaded_file = drive.CreateFile({'id': getenv("INTENT_DATA_FILE_ID")})
        downloaded_file.GetContentFile('data/intent_data.csv')

    def train(self):
        self.get_train_data()
        data = pd.read_csv("data/intent_data.csv")

    def predict(self):
        pass