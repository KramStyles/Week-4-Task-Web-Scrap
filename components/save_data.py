import csv
import os


class SaveData:
    def __init__(self, url, data):
        self.url = url
        self.data = data

        if os.path.exists(os.getcwd() + '/src/log.csv'):
            self.save_log()
        else:
            self.save_log(new_file=True)

    def save_log(self, new_file=False):
        try:
            with open(os.getcwd() + '/src/log.csv', mode='a') as file:
                writer = csv.writer(file, delimiter='\t')
                if new_file:
                    writer.writerow(['Scraped Website', 'Most Common Word', 'Number of Occurrence'])
                writer.writerow([self.url, self.data[0], self.data[1]])
        except IOError as err:
            print('IO Error has occurred: ->', err)
