# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import sanity2
import laskenta 

# Varsinaisen pääohjelman alku

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
while True:

    # Kysytään käyttäjältä paino
    tapahtui_virhe = True
    while tapahtui_virhe == True:
            paino_str = input('Paino (kg)? ')
            tulokset = sanity2.liukuluvuksi(paino_str)
            if tulokset[0] == 0:
                paino = tulokset[2]
                tapahtui_virhe = False
            else:
                print(tulokset[1])           
    # Testit
    print('Ja paino oli', paino, 'kg')

    """
    #pituus_str = input('Pituus (m)? ')
    # pituus = 

    #print('Painoindeksisi on', bmi(paino, pituus))
    """
    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/E)')
    if uusi == 'E' or uusi == 'e':
        break