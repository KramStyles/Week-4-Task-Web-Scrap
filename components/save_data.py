import csv
import os

class SaveData:
    def __init__(self, url, data):
        self.url = url
        self.data = data

        if os.path.exists(os.getcwd()+'/src/log.csv'):
            self.save_log()
        else:
            self.save_log(new_file=True)

    def save_log(self, new_file=False):
        if new_file:
            print('Site is:', self.url, 'Data is:', self.data)
        else:
            print(os.getcwd())
            print('Path not found')
