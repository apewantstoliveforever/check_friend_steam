import requests
from bs4 import BeautifulSoup
import urllib.request


class Check_friends:
    def __init__(self, links):
        self.links = links
        self.friends = []
        self.friends_link = []

    def all_friend(self):
        url =  self.links
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        new_feed = soup.find('div', class_='friends_container').find_all('div', attrs={'data-panel' : '{"flow-children":"row"}'} )
        b = 0
        for i in new_feed:
            b += 1
            try:
                name = i.get('data-search')
                steam_id = i.get('data-steamid')
                # print('Name: {} - Steam_id: {}'.format(name, steam_id))
                self.friends.append(steam_id)
                steam_link = i.find('a', class_="selectable_overlay").get('href')
                self.friends_link.append(steam_link)
            except Exception:
                pass

        return self.friends_link
    def check(self):
        if "          " in self.friends:  #steam_id
            print(self.links,"yes")



p1 = Check_friends('            ')
list = p1.all_friend()
for i in list:
    p2 = Check_friends(i + '/friends')
    p2.all_friend()
    p2.check()
