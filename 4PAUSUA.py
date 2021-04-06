import urllib
import urllib.request
import requests
import os
from bs4 import BeautifulSoup

erabiltzailea = ''
pasahitza = ''
uriIkasgaia = 'https://egela.ehu.eus/course/view.php?id=42336'
cookie = ''
html = ''
pdfKop = 0


def datuakEskatu():
    global erabiltzailea
    global pasahitza

    print("Sartu eGela-ko erabiltzailea:")
    erabiltzailea = input()
    print("\nSartu eGela-ko erabiltzailearen pasahitza:")
    pasahitza = input()


def cookieLortu():
    global cookie

    # Eskaera egin
    metodoa = 'POST'
    uria = "https://egela.ehu.eus/login/index.php"
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    edukia = {'username': erabiltzailea,
              'password': pasahitza}
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))
    erantzuna = requests.request(metodoa, uria, data=edukia_encoded,
                                 headers=goiburuak, allow_redirects=False)

    # cookie-a aldagai global batean gorde
    cookie = erantzuna.headers['Set-Cookie'].split(";")[0]


def htmlLortu(uri):
    global html

    # Eskaera egin
    metodoa = 'GET'
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Cookie': cookie}
    edukia = ''
    erantzuna = requests.request(metodoa, uri, data=edukia,
                                 headers=goiburuak, allow_redirects=False)

    # html kodea aldagai global batean gorde
    html = erantzuna.content


def pdfKarpetaSortu():
    if not os.path.exists("pdf"):
        os.mkdir("pdf")


def deskargaEgin(uri):
    global pdfKop

    # Deskargatutako pdf-a izen originala mantentzeko
    split = str(uri).split("/")
    izena = split[len(split) - 1]

    print("\n" + izena + " deskargatzen...")

    # pdf-aren edukia lortu eskaera baten bidez, saioaren cookie-a erabiliz
    metodoa = 'GET'
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Cookie': cookie}
    edukia = ''
    erantzuna = requests.request(metodoa, uri, data=edukia,
                                 headers=goiburuak, allow_redirects=False)

    # pdf-aren edukia fitxategi batean gorde
    pdfEdukia = erantzuna.content
    file = open("./pdf/" + izena, "wb")
    file.write(pdfEdukia)
    file.close()

    print(izena + " deskargatu da")
    pdfKop += 1


def pdfDeskargatuEgoterakoan(uri):
    # Baliabidearen orrialdearen html-a lortu
    htmlLortu(uri)
    soup = BeautifulSoup(html, "html.parser")

    # Baliabidearen orrialdearen html-tik <a> motako elementuak lortu
    a_elements = soup.find_all('a')

    # <a> motako elementu bakoitzaren href begiratu, eta, ".pdf" badauka bere barnean (pdf motako fitxategi bat) aurrera jarraitu (pdf fitxategia deskargatu)
    for a in a_elements:
        if "href" in str(a):
            lortutakoUri = a["href"]
            if ".pdf" in lortutakoUri:
                deskargaEgin(lortutakoUri)


def deskargaProzesua():
    # Karpeta bat sortu, deskargatutako pdf fitxategiak gordetzeko
    pdfKarpetaSortu()
    soup = BeautifulSoup(html, "html.parser")

    # WS ikasgaiko eGela-ko orrialde nagusiaren html-tik <a> motako elementuak (class='' dutenak bakarrik) lortu
    a_elements = soup.find_all('a', {'class': ''})

    # <a> motako elementu bakoitzaren href begiratu, eta, "https://egela.ehu.eus/mod/resource/view.php?id=" motakoa bada (eGela-ko baliabidea) aurrera jarraitu
    for a in a_elements:
        if "href" in str(a):
            lortutakoUri = a["href"]
            if "https://egela.ehu.eus/mod/resource/view.php?id=" in lortutakoUri:
                pdfDeskargatuEgoterakoan(lortutakoUri)

    if os.name == "nt":
        print("\n" + str(pdfKop) + " pdf fitxategi deskargatu dira " + os.getcwd() + "\pdf karpetan")
    else:
        print("\n" + str(pdfKop) + " pdf fitxategi deskargatu dira " + os.getcwd() + "/pdf karpetan")


if __name__ == '__main__':
    datuakEskatu()
    cookieLortu()
    htmlLortu(uriIkasgaia)
    deskargaProzesua()