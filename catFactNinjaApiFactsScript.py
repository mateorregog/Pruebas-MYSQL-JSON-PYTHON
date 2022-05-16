import json
import requests

def imprimirHechos(archivoJson):
    hechos = archivoJson.get("data")
    for hecho in hechos:
        print(hecho["fact"],"\n")
    
    
if __name__ == "__main__":
    url = "https://catfact.ninja/facts"
    r = requests.get(url)
    archivoJson = r.json()
    imprimirHechos(archivoJson)
    
    for _ in range(5):
        print("------------------- Siguiente página ---------------------- ")
        url_next = archivoJson.get("next_page_url")
        r = requests.get(url_next)
        archivoJson = r.json()
        imprimirHechos(archivoJson)