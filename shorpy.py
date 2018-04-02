import re
import os
import time
import requests
import urllib.request
from bs4 import BeautifulSoup


def scrape():

    link_index = 23225

    while link_index > 23000:
        request = requests.get("http://www.shorpy.com/node/" + str(link_index))
        data = request.text
        soup = BeautifulSoup(data, 'html.parser')

        suffix = ".preview.jpg"
        images = soup.find_all('img')

        for image in images:
            if (image['src'].endswith(suffix)):
                reg = re.compile(suffix).split((image['src']))
                print (reg[0] + ".jpg")
                urllib.request.urlretrieve(reg[0] + ".jpg", str(link_index) + ".jpg")


        link_index -= 1

#scrape()

def scrape_places():

        places = []

        start_http = "http://www.shorpy.com/"

        start_data = requests.get(start_http).text

        start_soup = BeautifulSoup(start_data, 'html.parser')

        for tag in start_soup.find_all('div', attrs = {'id':'block-block-81'}):
            for tag in tag.find_all('a'):
                if (tag.get('href')[-3:].isdigit()):
                    places.append(tag.get('href')[-3:])

        z = 0

        while z < len(places):

            pages = 0

            http = "http://www.shorpy.com/image/tid/" + places[z] + "?page=0"

            data = requests.get(http).text

            soup = BeautifulSoup(data, 'html.parser')

            location = str(soup.title.contents[0].split("|")[0])

            i = 0

            for tag in soup.find_all('a', attrs={'class':'pager-last active'}):
                reg = re.compile('=').split(tag['href'])
                pages = int(reg[1])

            print("Number of pages for " + location + ": " + str(pages+1) )

            while i <= pages:


                http = http[:-1] + str(i)
                data = requests.get(http).text
                soup = BeautifulSoup(data, 'html.parser')
                print("http is: " + http)

                suffix = ".thumbnail.jpg"
                images = soup.find_all('img')

                for image in images:
                    if ("IcedTee-1926-01" not in image['src']
                    and "1951_Air_Race_Santa_Ana_To_Detroit" not in image['src']):
                        reg = re.compile(suffix).split((image['src']))
                        print (reg[0] + ".jpg")
                        reg2 = re.compile("images/").split((reg[0]))
                        urllib.request.urlretrieve(reg[0] + ".jpg", reg2[1] + ".jpg")
                i  += 1
            z += 1

#scrape_places()

def scrape_anything():

        os.system("mkdir 'output'")

        pages = 0

        http = input("Enter Shorpy URL: ") + "?page=0"

        data = requests.get(http).text

        soup = BeautifulSoup(data, 'html.parser')

        location = str(soup.title.contents[0].split(" |")[0])

        os.system("mkdir output/" + '"' + location + '"')

        i = 0

        for tag in soup.find_all('a', attrs={'class':'pager-last active'}):
            reg = re.compile('=').split(tag['href'])
            pages = int(reg[1])

        print("Number of pages for " + location + ": " + str(pages+1) )

        while i <= pages:

            http = http[:-1] + str(i)
            data = requests.get(http).text
            soup = BeautifulSoup(data, 'html.parser')
            print("http is: " + http)

            suffix = ".thumbnail.jpg"
            images = soup.find_all('img')

            for image in images:
                if (image['src'].endswith(suffix)):
                    if ("IcedTee-1926-01" not in image['src']
                    and "1951_Air_Race_Santa_Ana_To_Detroit" not in image['src']):
                        reg = re.compile(suffix).split((image['src']))
                        print (reg[0] + ".jpg")
                        reg2 = re.compile("images/").split((reg[0]))
                        filename = os.path.join("/Users/Admin/Desktop/Programming/Py/scrape shorpy/output/" + location, reg2[1] + ".jpg")
                        urllib.request.urlretrieve(reg[0] + ".jpg", filename)
            i  += 1


scrape_anything()

def test():

    request = requests.get("http://www.shorpy.com/image/tid/263")
    data = request.text
    soup = BeautifulSoup(data, 'html.parser')



    for tag in soup.find_all('a', attrs={'class':'pager-last active'}):
        reg = re.compile('=').split(tag['href'])
        print(int(reg[1]))


#test()
