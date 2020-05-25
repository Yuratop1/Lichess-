from bs4 import BeautifulSoup
import urllib.request

class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        # results = self.html.findAll("span", {'data-href': '/@/AylorSnow'})
        results = self.html.findAll("span", {'class': 'online user-link'})
        results_offline = self.html.findAll("h1", {'class': 'user-link offline'})
        results_patron = self.html.findAll("a", {'href': "/patron"})
        # tag = results[0]
        # line.patron::before
        # print(results_patron)
        # print(results)
        # if results_offline != []:
        #     print('offline')
        #     flag = False
        # elif results_patron != [] and results == []:
        #     print(f'online')
        #     flag = True
        # elif results != []:
        #     print(f"online")
        #     flag = True
        # else:
        #     print(f"offline")
        #     flag = False

        if results_offline != []:
            print('offline')
            flag = False
        else:
            print(f'online')
            flag = True
        # news = self.html.find_all('i', class_='user-link.online')
        # self.results.append({
        #     'news': news
        # })

    # def save(self):
    #     with open(self.path, 'w', encoding='utf-8') as f:
    #         i = 1
    #         # for item in self.results:
    #         #     f.write(f'{item["news"]}')
    #         #     i += 1


    def run(self):
        self.get_html()
        self.parsing()
        # self.save()