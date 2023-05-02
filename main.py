"""
projekt_3.py
author: Miloš Pelikán
email: milos.pelikan@gymbeam.com
discord: Miloš P.#4629
"""

import csv
import requests
import sys
import os
from bs4 import BeautifulSoup as bs


def kontrola_vstupu(argv: str):
    """Kontrola vstupních dat."""
    if len(argv) != 2:
        print("Špatná vstupní data!")
        sys.exit()

    url = str(argv[0])
    jmeno_souboru = str(argv[1])

    if not url.startswith("https://www.volby.cz/pls/ps2017nss"):
        print("Špatná URL!")
        sys.exit()

    elif not jmeno_souboru.endswith(".csv"):
        print("Špatný formát souboru!")
        sys.exit()
    else:
        print(f"Stahuji data z: {url}")
        return url, jmeno_souboru


def code_location(url: str):
    """Parsuje stránku a poté pomocí for smyčky najde kódy územní úrovních a jejich jména."""
    vysledky_voleb = []
    odkazy = []
    zdroj_na_odkazy = "https://www.volby.cz/pls/ps2017nss/"
    parsovana_html = bs(requests.get(url).text, features="html.parser")
    tr_tagy = parsovana_html.find_all("tr")
    rozsah = range(1, 4)

    for tr_tag in tr_tagy:
        kod_lokace = dict()
        kod = tr_tag.find("td", {"class": "cislo"})
        for cislo in rozsah:
            jmeno = tr_tag.find("td", {"headers": f"t{cislo}sa1 t{cislo}sb2"})
            if kod and jmeno is not None:
                kod_lokace["code"] = kod.text
                kod_lokace["location"] = jmeno.text
                vysledky_voleb.append(kod_lokace)
                odkazy.append(zdroj_na_odkazy + kod.find("a")["href"])
                break
    return odkazy, vysledky_voleb


def reg_env_val(odkazy: list, vysledky_voleb: list):
    """Zjistí typy hlasů a jejich počet."""
    for index, kod_lokace in enumerate(vysledky_voleb):
        url = odkazy[index]
        parsovana_html = bs(requests.get(url).text, features="html.parser")
        kod_lokace["registered"] = parsovana_html.find("td", {"headers": "sa2"}).text.replace("\xa0", "")
        kod_lokace["envelopes"] = parsovana_html.find("td", {"headers": "sa5"}).text.replace("\xa0", "")
        kod_lokace["valid"] = parsovana_html.find("td", {"headers": "sa6"}).text.replace("\xa0", "")
    return vysledky_voleb


def hlasy_stran(odkazy: list, vysledky: list):
    """Zjistí názvy jednotlivých stran a počet hlasů, které získaly."""
    rozsah = range(1, 4)
    for index, rada in enumerate(vysledky):
        url = odkazy[index]
        parsovana_html = bs(requests.get(url).text, features="html.parser")
        div_tagy = parsovana_html.find("div", {"id": "inner"})
        tr_tagy = div_tagy.find_all("tr")
        for tr_tag in tr_tagy:
            jmeno_strany = tr_tag.find("td", {"class": "overflow_name"})
            for cislo in rozsah:
                hlasy = tr_tag.find("td", {"headers": f"t{cislo}sa2 t{cislo}sb3"})
                if jmeno_strany is not None and hlasy is not None:
                    rada[jmeno_strany.text] = hlasy.text.replace("\xa0", "")
                    break
    return vysledky


def uloz_do_csv(jmeno_souboru: str, vysledky_voleb: list):
    """Uloží stažená data do .csv souboru """
    with open(jmeno_souboru, "w", encoding="utf-8", newline="") as vysledny_soubor:
        jmena_poli = vysledky_voleb[0].keys()
        writer = csv.DictWriter(vysledny_soubor, fieldnames=jmena_poli, delimiter=";")
        writer.writeheader()
        writer.writerows(vysledky_voleb)
        print(f"Stažená data ukládám do souboru: {jmeno_souboru}",
              "Ukončuji program.",
              sep="\n")


def hlavni_program(argv: str):
    """Definice hlavního programu."""
    url_stranka, jmeno_souboru = kontrola_vstupu(argv)
    odkazy, code_loc = code_location(url_stranka)
    typy_hlasu = reg_env_val(odkazy, code_loc)
    vysledky_voleb_finalni = hlasy_stran(odkazy, typy_hlasu)
    uloz_do_csv(jmeno_souboru, vysledky_voleb_finalni)


if __name__ == "__main__":
    hlavni_program(sys.argv[1:])

"""Pošle cestu kam se finalní soubor uložil"""
print(os.getcwd())
