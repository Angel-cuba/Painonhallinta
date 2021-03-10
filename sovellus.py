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
    # Simulka jossa pyörittään kunnes saadan järkevä arvo
    while tapahtui_virhe == True:
        paino_str = input('Paino (kg)? ')
        tulokset = sanity2.liukuluvuksi(paino_str)
            
        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            paino = tulokset[2]
            tarkistettu_paino = sanity2.rajatarkistus(paino, 40, 300)

            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_paino == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheimoitus
                 print(tarkistettu_paino[1])


        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus
        else:
             print(tulokset[1])           
    # Testit
    print('Ja paino oli', paino, 'kg')

    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/E)')
    if uusi == 'E' or uusi == 'e':
        break