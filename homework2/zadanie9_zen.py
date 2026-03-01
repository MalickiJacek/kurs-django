import io
import sys

stare_wyjscie = sys.stdout
sys.stdout = io.StringIO()

import this

zen_tekst = sys.stdout.getvalue()
sys.stdout = stare_wyjscie

linie = zen_tekst.split("\n")
licznik = 0
for linia in linie:
    if linia.strip():
        print(linia)
        licznik += 1
        if licznik == 2:
            break
