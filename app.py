from components.display_data import DisplayData
from components.get_data import GetData
from components.clean_data import CleanData


class Run:
    def __init__(self):
        run = input('Would you like to scrape a website (y/n)? ')
        while run.lower() != 'n':
            url = input('Enter a website to analyze!: ')
            self.data = GetData(url)
            self.soup = self.data.get_soup()
            if type(self.soup) == str and len(self.soup) > 50:
                self.cleaned_data = CleanData(self.soup)
                print('The top word is:', self.cleaned_data.words[0][0], '\n')
                DisplayData(self.cleaned_data.words)
            else:
                print(self.soup, '\n')

            run = input('Would you like to scrape a website (y/n)? ')
        print('Thanks for analyzing! Come back again!')


if __name__ == '__main__':
    Run()
