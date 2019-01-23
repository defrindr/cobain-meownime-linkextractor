import requests
from bs4 import BeautifulSoup
import re

def link(link2extract):
    input1 = str(link2extract)
    url = requests.get(input1)
    page = BeautifulSoup(url.content, 'html.parser')
    for x in page.find_all('input', attrs={'type': 'hidden'}):
        inp = x.get('value')

    for a in page.find_all('form'):
        urls = a.get('action')

    data = {'get': inp}
    headers = {'User-Agent': 'Mozilla/5.0'}
    session = requests.Session()
    url2 = session.post(urls, data=data, headers=headers)
    page1 = BeautifulSoup(url2.content, 'html.parser')
    link = ('').join(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page1.text))
    return str(('').join((linkfix for linkfix in link.split("';window.open(a,"))))


def main():
    print('\n========================================\n\n\t==     == eownime.com\n\t= =   = =   Link\n\t=  = =  =   Extracttor\n\t=   =   =\n\n  Defri Indra M\n  https://github.com/greyxploiter\n========================================\n\t')
    try:
        choose = int(input('1. Single\n2. Mass\n\nChoose : '))
        if choose == 1:
            link2extract = input('Enter Link : ')
            print(f'''
[+] extracted => {(link(link2extract))}''')
        else:
            if choose == 2:
                fileName = input('Enter path to txt : ')
                print('')
                with open(fileName) as (file):
                    data = file.read()
                    i = 1
                    for link2extract in data.split('\n'):
                        print(f'''[{i}] => {(link(link2extract))}''')
                        i += 1

                    print('\n[+] Complete Extracted Link')
            else:
                print('Number not found !!!')
    except Exception as e:
        print(f'''Error : {e}''')

