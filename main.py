'''
NB-2023.03.22

Feladat:

Van egy könyves bolt ahol minden vásárló aki KÁRTYÁVAL fizet kap 5% kedvezményt a vásárlás összértékéből. -ok
Minden vásárló aki vásárol teljesáras terméket és akciósat is újabb 5% kedvezményt kap.
Ezen felül, minden tizedik vásárló újabb 5% kedvezményt is kap.

Bekérni a teljesáras könyvek összegét - input
Bekérni az akciós könyvek összegét - input
Bekérni a fizetés módját -input
Generalni egy számot 1-10 között - random.randint

Értelmezés:

Vasarlas összege - változó
Kártya =  igen/nem
Vasarló sorszáma = random.randint
Döntés  IF függvénnyel

'''
import random

vegosszeg = 0

print("\033[H\033[2J")

teljesAras_konyv = int(input('Add meg a teljesáras könyvek összegét, ha nem volt, írj 0-t : '))
akcios_konyv = int(input('Add meg az akciós könyvek árát ha nem volt írj 0-t: '))
vevo_szama = random.randint(1, 10)

osszesen_konyv = teljesAras_konyv + akcios_konyv

print(f'A könyvek teljes ára:  {osszesen_konyv} Ft')
print()

if teljesAras_konyv and akcios_konyv != 0:
    ar = osszesen_konyv * 0.95
    print(f'Könyvek ára csomagkedvezménnyel: {ar} Ft')

else:
    ar = osszesen_konyv

print()

kartya = str(input('Kártyával fizetsz? i/n :  '))
print()

if kartya == 'i':
    vegosszeg = ar * 0.95
elif kartya == 'n':
    vegosszeg = ar
else:
    print('HIBA ---- Csak  i vagy n karakter adható meg !')

if vevo_szama == 10:
    total = vegosszeg * 0.95
else:
    total = vegosszeg

print(f"Fizetendő: %.2f Forint" % vegosszeg)
print(f'Ön a {vevo_szama}. vevő, ezért %.2f Ft a végösszeg' % total)
print()