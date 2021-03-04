# Tiivistetty versio Sanity.py-modulista eli suurinpiirtein se, mitä tuhosin vahingossa

def liukuluvuksi(syote):
    """Tarkistaa syötteen ja muuttaa sen liukuluvuksi
    Args:
        syote (string): Käyttäjän syöttämä arvo
    Returns:
        list: virhekoodi, virhesanoma ja syöte liukulukuna
    """

    # Asetetaan palautusarvojen oletukset
    virhekoodi = 0
    virhesanoma = 'Syöte OK'
    arvo = 0

    # Puhdistetaan syöte ylimääräisistä merkeistä (Whitespace)
    syote = syote.strip()

    # Selvitetään sisältääko syöte mahdollisen desimaalipilkun ja korvataan se pisteellä
    if syote.find(',') != -1:
        syote.replace(',', '.')

    # Selvitetään sisältääkö syöte desimaalipisteen ja jaetaan syöte pisteen kohdalta useammaksi merkkijonoksi
    if syote.find('.') != -1:
        osat = syote.split('.')

        # Selvitetään onko osia enemmän kuin 2, eli onko useita pisteitä
        if len(osat) > 2:
            virhekoodi = 1
            virhesanoma = 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu'
            
        # Jos osia on 2
        else:
            osa = str(osat[0])  

            # Jos ensimmäinen osa on numeerinen ts. ei sisällä muita merkkejä kuin 0...9      
            if osa.isnumeric():
                osa = str(osat[1])

                # Jos toinenkin osa on numeerinen
                if osa.isnumeric():
                    arvo = float(syote)
                else:
                    virhekoodi = 4
                    virhesanoma =  'Desimaalierottimen jälkeen ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu'

            else:
                virhekoodi = 3
                virhesanoma = 'Ennen desimaalierotinta ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu'
                

    # Tarkistetaan onko desimaaliton syöte numeerista
    elif syote.isnumeric():
        arvo = float(syote)
    else:
        virhekoodi = 2
        virhesanoma = 'Syötteessä ylimäärisiä merkkejä: vain numerot ja desimaalipiste on sallittu'   
    
    # Muodostetaan funktion paluuarvo ja palautetaan se
    paluuarvo = [virhekoodi, virhesanoma, arvo]
    return paluuarvo

    
# Funktio, jolla tarkistetaan, että syötetty arvo on haluttujen rajojen sisällä
def rajatarkistus(arvo, alaraja, ylaraja):
    """Tarkistaa, että syötetty arvo on suurempi tai yhtäsuuri kuin alaraja ja pienempi

    Args:
        arvo (float): tarkistettava arvo 
        alaraja (float): pienin salittu arvo 
        ylaraja (float): suurin salittu arvo

    Returns:
        list: virhekoodi, virheilmoitus
    """

    # Määritellään virheiden oletukset
    virhekoodi = 0
    virhesanoma = 'Arvo OK'

    paluuarvo = [virhekoodi, virhesanoma]
    return paluuarvo
    

      