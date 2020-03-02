import requests
import time
import sys
from bs4 import BeautifulSoup

URL = sys.argv[1]
head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'} 

req = requests.get(URL, headers=head)
CONT = req.text

def verifySite(url, cabec):
  global CONT
  reqv = requests.get(url, headers=cabec)
  contv = reqv.text
  if (contv != CONT):
    enviaMsg()
    CONT = contv
  else:
    pass

def checkTravis(url, cabec):
  response = requests.get(url, headers=cabec)
  soup = BeautifulSoup(response.text, "lxml")
  if str(soup).find("Travis") == -1:
    print("Ainda Nada")
  else:
    enviaMsg()

def enviaMsg():
  requests.get("https://api.telegram.org/bot1145666491:AAGaneM5CKxslauH182jNjl995pwIyNRZrk/sendMessage?chat_id=-1001285983568&text=Corre que a página atualizou")

while True:  
  #verifySite(URL, head)
  checkTravis(URL, head)
  time.sleep(15)