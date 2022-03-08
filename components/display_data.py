import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class DisplayData:
    def __init__(self, words):
        self.words = words
        self.convert_data()

        # Chart information
        self.axis_x = self.words[0]
        self.axis_y = self.words[1]

        # Plot Charts
        self.plot_bar_chart()
        self.plot_pie_chart()

    def convert_data(self):
        self.words = pd.DataFrame(self.words)
        return self.words

    def plot_bar_chart(self):
        plt.bar(self.axis_x, self.axis_y)
        plt.show()

    def plot_pie_chart(self):
        plt.pie(self.axis_y, labels=self.axis_x, shadow=True,
                explode=np.random.uniform(low=0.05, high=0.05,
                                          size=self.axis_x.size))
        plt.show()
