# Engeto projekt č.3 (Volby2017 - Projekt č. 3)
Poslední projekt na Engeto - Python Akademii. 

## Popis projektu
Hlavním cílem projetku je parsování výsledků parlamentních voleb z roku 2017. Odkaz k nahlédnutí [zde](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Všechny knihovny, které jsou nutné a zároveň jsou použity v programu, jsou uloženy v souboru `requirements.txt`. 
Pro instalaci těchto knihoven, lze použít nové virtuální prostředí.

## Spuštění projektu
Spuštění programu `main.py` v terminálu je potřeba zadat dva povinné argumenty, které se musí dát do uvozovek, aby program správně fungoval.
```
python main.py <odkaz_uzemniho_celku> <nazev_vystupniho_souboru>
```
Data budou stažena do souboru s příponou `.csv`.

## Argumenty pro projekt
Výsledky programu je hlasování pro Ústecký kraj, okres Litoměřice:

1. argument:  `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4203`
2. argument:  `Litomerice.csv`

###### Spuštění programu:
```
(venv) milospelikan@MacBook-Air ~ % /Users/milospelikan/PycharmProjects/Volby2017/venv/bin/python /Users/milospelikan/PycharmProjects/Volby2017/main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4203" "Litomerice.csv" 
```
### Cesta k souboru

```/Users/milospelikan```

