import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore,Style
import time
from urllib.parse import urlparse as getDomain



def downloadMeowDrive(link2Storage):
	# Cloud extract link
	namaFile = []
	download = []
	url = requests.get(link2Storage)
	bsMeow = BeautifulSoup(url.content,"html.parser")
	for name in bsMeow.find_all("h2"):
		namaFile.append(name.text)
	for linkDownload in bsMeow.find_all('a',attrs={"class":"btn meow","role":"button"}):
		download.append(linkDownload.get("href"))
	return (namaFile[0],download[0])




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
	link2Storage = link.split("';window.open(a,")[0]
	files = downloadMeowDrive(link2Storage)

	# print(link)
	# print(link2Storage)
	return files


def main():
	print('\n========================================\n\n\t==     == eownime.com\n\t= =   = =   Link\n\t=  = =  =   Extractor\n\t=   =   =\n\n  Defri Indra M\n  https://github.com/greyxploiter\n========================================\n\t')
	try:
		choose = int(input('1. Single\n2. Mass\n\nChoose : '))
		if choose == 1:
			link2extract = input('Enter Link : ')
			data = link(link2extract)
			print(f'''
{Fore.YELLOW} [ {data[0]} ]{Style.RESET_ALL} => {data[1]}''')
		else:
			if choose == 2:
				fileName = input('Enter path to txt : ')
				print('')
				dataWrite = ""
				with open(fileName) as (file):
					data = file.read()
					data = data.split('\n')
					for link2extract in data:
						if len(link2extract) <= 0:
							continue
						else:
							data = link(link2extract)
							dataWrite = dataWrite+""+data[0]+" => "+data[1]+"\n\n"
							print(f'''{Fore.RED}[{data[0]}]{Style.RESET_ALL} => {data[1]}''')
					print('\n[+] Complete Extracted Link')
					wrtQuest = str(input(f" Write data to result_{fileName} [y]es / [n]o) ?"))
					if wrtQuest[0] == 'y' or wrtQuest[0] == 'Y' or wrtQuest[0] == 'yes' or wrtQuest[0] == 'YES' or wrtQuest[0] == 'Yes':
						createTxt = open("result/result_"+fileName,"w+")
						createTxt.write(dataWrite)
						createTxt.close()
						print("[+] Thanks To Use My Tools")
					else:
						print("[+] Thanks To Use My Tools")
			else:
				print(' Number not found !!!')
	except Exception as e:
		print(f'''Error : {e}''')

