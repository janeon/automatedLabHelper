import requests
from bs4 import BeautifulSoup
import re

class FindExamples:
    def __init__(self, searchTerm):
        self.urls = []
        # self.messageToURLS = {}
        self.searchTerm = searchTerm

    def fillURLS(self):
        # codes = list(open("errorCodes.txt","r"))
        # for line in codes:
        #     message = line.split(":")[1]
        #     self.messages.append(message)
        #     self.messageToURLS[message] = []

        # del self.messages[5:]

        # for msg in self.messages:
        message = "+".join(self.searchTerm.split("-"))
        page = requests.get("https://www.google.dz/search?q="+message)
        soup = BeautifulSoup(page.content, 'html.parser')

        links = soup.findAll("a")

        for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            urls = re.split(":(?=http)",link["href"].replace("/url?q=",""))
            for url in urls:
                cleanurl = url.split("&sa")[0]+'\n'
                if "%" not in cleanurl:
                    self.urls.append(cleanurl)
                    # print(cleanurl)
def main():
    x = FindExamples("test-this")
    # x.fillURLS()
    # print(x.urlsf)

if __name__ == "__main__":
    main()
