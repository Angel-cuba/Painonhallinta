# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import sanity as s
#import laskenta as l
from laskenta import bmi 

# Varsinaisen pääohjelman alku

# Komponenttie alustukset

# Työsimulkka, ikuinen, jossa on poistumistoiminto

uusi = 'K'
while True:
     # Kysytään käyttäjältä paino
   paino_str =input("'Paino (kg)? ")
   paino = s.on_jarkeva(paino_str, 20, 300)

   pituus_str = input('Pituus (m)?')
   pituus = s.on_jarkeva(pituus_str, 1, 3)

   print('Painoindeksi on ', bmi(paino, pituus))
    # Poistuminen ikuisesta simulkassa
   uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/E)') 
   if uusi == 'E':
    break


