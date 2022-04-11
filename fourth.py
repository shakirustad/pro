from bs4 import BeautifulSoup
import csv
import requests
from requests import get
import re
import pandas as pd
import numpy
import html5lib
import lxml
domains = ['https://www.enterpriseschools.net/Domain/1884']


# function to check if small string is
# there in big string


# driver code


print(len(domains))
for l in domains:
    links = []
    emaillist=[]
    req1 = requests.get(l)
    req = req1.text
    if (req.find("mailto:") == -1):
        print("Emails visible")
    # soup = BeautifulSoup(req1.content, 'lxml')
        item = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', req)


        for it in item:
            emaillist.append(it)
            links.append(l)
        emaillist=item
        print(emaillist)
        dic1 = {
            'emails': emaillist,
            'links': l
        }
        df = pd.DataFrame(dic1)
        # # except:
        #     print("error is here")
        print(df)
        # f = open("emails.csv", "w")
        df.to_csv("emails.csv", mode='a', header=False)
    else:
        # page = "https://www.eurocham-cambodia.org/member/476/2-LEau-Protection"

        page = "https://www.enterpriseschools.net/Domain/1884"

        content = get(page).content
        soup = BeautifulSoup(content,"lxml")

        exp = re.compile(r"(?:.*?='(.*?)')")
        # Find any element with the mail icon
        for icon in soup.findAll("i", {"class": "icon-mail"}):
            print('icon found..')
            # the 'a' element doesn't exist, there is a script tag instead
            script = icon.next_sibling
            # the script tag builds a long array of single characters- lets gra
            chars = exp.findall(script.text)
            print(chars)
            output = []
            # the javascript array is iterated backwards
            for char in reversed(list(chars)):
                # many characters use their ascii representation instead of simple text
                if char.startswith("|"):
                    output.append(chr(int(char[1:])))
                else:
                    output.append(char)
            # putting the array back together gets us an `a` element
            link = BeautifulSoup("".join(output))
            email = link.findAll("a")[0]["href"][8:]
            # the email is the part of the href after `mailto: `
            print(email)
        # print("Email field hidden")