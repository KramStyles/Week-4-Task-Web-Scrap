from components.display_data import DisplayData
from components.get_data import GetData
from components.clean_data import CleanData
from components.save_data import SaveData


class Run:
    def __init__(self):
        run = input('Would you like to scrape a website (y/n)? ')
        while run.lower() != 'n':
            if run.lower() == 'y':
                url = input('Enter a website to analyze!: ')
                self.data = GetData(url)
                self.soup = self.data.get_soup()
                if type(self.soup) == str and len(self.soup) > 50:
                    self.cleaned_data = CleanData(self.soup)
                    print('The top word is:', self.cleaned_data.words[0][0], '\n')
                    DisplayData(self.cleaned_data.words).plot_charts()
                    SaveData(url, self.cleaned_data.words[0])
                else:
                    print(self.soup, '\n')
            else:
                print('Only y and n are allowed')

            run = input('Would you like to scrape a website (y/n)? ')
        print('Thanks for analyzing! Come back again!')
