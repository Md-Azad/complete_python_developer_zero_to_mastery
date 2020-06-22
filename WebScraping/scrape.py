import requests

from bs4 import BeautifulSoup

import pprint

res = requests.get('https://news.ycombinator.com/news')

# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')

subtext = soup.select('.subtext')

def listed_by_highest_vote(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href_link = links[idx].get('href', None)

        votes = subtext[idx].select('.score')

        if len(votes):

            points = int(votes[0].getText().replace(' points', ''))

            #print(points)

            if points > 99:

                hn.append({'title': title, 'link': href_link, 'votes': points})
    return listed_by_highest_vote(hn)


pprint.pprint(create_custom_hn(links, subtext))
# print(votes[0].contents)

# print(links)
