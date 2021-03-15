import urllib
import requests


erabiltzailea = ''
pasahitza = ''
uriEskaera1  = ''
cookie = ''


def datuakEskatu():
    global erabiltzailea
    global pasahitza

    print("Sartu eGela-ko erabiltzailea:")
    erabiltzailea = input()
    print("\nSartu eGela-ko erabiltzailearen pasahitza:")
    pasahitza = input()


def eskaera1():
    global uriEskaera1
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
    uriEskaera1 = erantzuna.headers['Location']
    cookie = erantzuna.headers['Set-Cookie'].split(";")[0]

    print("\n\n\n###########")
    print("1. ESKAERA")
    print("###########\n")

    # Eskaerari buruzko informazioa pantailaratu
    print("\n1. eskaerari buruzko informazioa:\n")
    print("Metodoa: \"" + metodoa + "\". URI-a: \"" + uria + "\"")
    print("Edukia:")
    for x in edukia.keys():
        print("     " + x + ": " + edukia[x])

    # Lortutako erantzunari buruzko informazioa pantailaratu
    print("\n\n1. eskaerarekin lortutako erantzunari buruzko informazioa:\n")
    print("Status: \"" + str(erantzuna.status_code) + "\". Deskribapena: \"" + erantzuna.reason + "\"")
    print("Goiburuak:")
    for x in erantzuna.headers.keys():
        print("     " + x + ": " + erantzuna.headers[x])



    # print(erantzuna.content) HTML KODEA LORTZEKO


def eskaera2():
    # Eskaera egin
    metodoa = 'GET'
    uria = uriEskaera1
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Cookie': cookie}
    edukia = ''
    erantzuna = requests.request(metodoa, uria, data=edukia,
                                 headers=goiburuak, allow_redirects=False)

    print("\n\n\n###########")
    print("2. ESKAERA")
    print("###########\n")

    # Eskaerari buruzko informazioa pantailaratu
    print("\n2. eskaerari buruzko informazioa:\n")
    print("Metodoa: \"" + metodoa + "\". URI-a: \"" + uria + "\"")

    # Lortutako erantzunari buruzko informazioa pantailaratu
    print("\n\n2. eskaerarekin lortutako erantzunari buruzko informazioa:\n")
    print("Status: \"" + str(erantzuna.status_code) + "\". Deskribapena: \"" + erantzuna.reason + "\"")
    print("Goiburuak:")
    for x in erantzuna.headers.keys():
        print("     " + x + ": " + erantzuna.headers[x])


def eskaera3():
    # Eskaera egin
    metodoa = 'GET'
    uria = "https://egela.ehu.eus/"
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Cookie': cookie}
    edukia = ''
    erantzuna = requests.request(metodoa, uria, data=edukia,
                                 headers=goiburuak, allow_redirects=False)

    print("\n\n\n###########")
    print("3. ESKAERA")
    print("###########\n")

    # Eskaerari buruzko informazioa pantailaratu
    print("\n3. eskaerari buruzko informazioa:\n")
    print("Metodoa: \"" + metodoa + "\". URI-a: \"" + uria + "\"")

    # Lortutako erantzunari buruzko informazioa pantailaratu
    print("\n\n3. eskaerarekin lortutako erantzunari buruzko informazioa:\n")
    print("Status: \"" + str(erantzuna.status_code) + "\". Deskribapena: \"" + erantzuna.reason + "\"")
    print("Goiburuak:")
    for x in erantzuna.headers.keys():
        print("     " + x + ": " + erantzuna.headers[x])
    print("\nErantzunaren edukia:\n")
    print(erantzuna.content)


def eskaera4():
    # Eskaera egin
    metodoa = 'GET'
    uria = "https://egela.ehu.eus/course/view.php?id=42336"
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Cookie': cookie}
    edukia = ''
    erantzuna = requests.request(metodoa, uria, data=edukia,
                                 headers=goiburuak, allow_redirects=False)

    print("\n\n\n###########")
    print("4. ESKAERA")
    print("###########\n")

    # Eskaerari buruzko informazioa pantailaratu
    print("\n4. eskaerari buruzko informazioa:\n")
    print("Metodoa: \"" + metodoa + "\". URI-a: \"" + uria + "\"")

    # Lortutako erantzunari buruzko informazioa pantailaratu
    print("\n\n4. eskaerarekin lortutako erantzunari buruzko informazioa:\n")
    print("Status: \"" + str(erantzuna.status_code) + "\". Deskribapena: \"" + erantzuna.reason + "\"")
    print("Goiburuak:")
    for x in erantzuna.headers.keys():
        print("     " + x + ": " + erantzuna.headers[x])
    print("\nIkasgai honetako eGelako orrialde nagusiko HTML-a:\n")
    print(erantzuna.content)


if __name__ == '__main__':
    datuakEskatu()
    eskaera1()
    eskaera2()
    eskaera3()
    eskaera4()