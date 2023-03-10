import requests #para realizar solicitudes HTTP
import time #medición del tiempo de ejecución de un programa, la suspensión del programa durante un tiempo específico, la obtención de la hora actual.
from bs4 import BeautifulSoup #para parsear HTML
from fake_useragent import UserAgent #para solicitar la información de la navegacion
from win10toast import ToastNotifier #para notificar al usuario que se ha realizado una petición

toaster = ToastNotifier() #para notificar al usuario que se ha realizado una petición
search = input("Ingrese el nombre del producto: ")
store = {}
search_list = search.split()
amazon_link = "https://www.amazon.es/"

url = amazon_link + "/s?k=" + "+" .join(search_list) + "&ref=nb_sb_noss"

#function
def tracker(random_header):
    url_open = requests.get(url, headers = random_header)
    soup = BeautifulSoup(url_open.content, "html.parser")
    tag = soup('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    tag_2 = soup ('span', {'class': 'a-price-whole'})
    for i,j in zip(tag,tag_2):
        if search.lower() in (i.text).lower():
            print("{} || price: {} Eu".format(i.text,j.text))
            store [str(i.text)] = j.text
            for a,b in store.items():
                if str (i.text) == a:
                    if j.text <b:
                        toaster.show_toast("Amazon deal",i.text+" || price"+ j.text)

while True:
    user = UserAgent()
    randomheader = {'User-Agent': str(user.random)}
    print ('Tracking....', time.asctime(time.localtime(time.time())))
    tracker (randomheader)
    time.sleep(60*5)
















