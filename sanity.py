# Moduli syötteen oikeellisuuden (sanity) tarkistamiseen

"""Tarkistaa käyttäjän syötteen oikeellisuuden tarkistusfunktioiden avulla  

        Raises:
        Exception: [description]
        Exception: [description]

        Returns:
        [type]: [description]
    """

# Funktioiden määrittelyt

def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit ja lopusta
    selvittää onko syötetty arvo annettujen rajojen sisällä Funktio muutta desimaalipilkun
    desimaalipisteeksi.

    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alarja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns (float) : Kättäjän syöttämä arvo numeerisena
    """

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # Selvitetään onko merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')
    
    # Jos pilkku löytty, korvataan pistellä
    if pilkunpaikka != -1:
       korjattu_syote = puhdistettu_syote.replace(',', '.')
    
    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu')
        luku = 0
    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella          
    try:
        if luku > alaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Palautetaan luku
    return luku
def liukuluku_ok(syote, alaraja, ylaraja):
    """Tarkistaa syötteen olevan numeerinen ja muuttaa sen liukuluvuksi. Syöttellä on alaraja ja ylaraja 

    Args:
        syote (string): Syöteenä saatu arvo
        alaraja (float): pienin hyväksyttävä arvo
        ylaraja (float): suurin hyväksyttävä arvo

    Returns:
        list: Palautaa arvon (float), virhekoodin (int), virhesanoman (string)
    """

    # Puhdistetaan syötteestä ylimääriset merkit (white space)
    puhdistettumerkkijono = syote.strip()

    # Tutkistaan onko syötteessä pilkku ja etsitään sen paikka
    pilkkunpaikka = puhdistettumerkkijono.find(',')

    # Jos pilkku löytyi, korvataan pisteellä
    if pilkkunpaikka != -1: # Jos ei löydy indeksi pn aina -1
        numeroarvo = puhdistettumerkkijono.replace(',', '.')
    else:
        numeroarvo = puhdistettumerkkijono # ei muutetaan 

    # Etsitään desimaalipistettä merkkijonnosta
    pisteenpaikka = numeroarvo.find('.') 

    # Jos desimaalipiste löytyy, jaetaan pisteen kohdalta erilliiisiksi, merkijo
    if pisteenpaikka != -1:
        osat = numeroarvo.split('.') # Syntyy lista osista 
        osien_maara = len(osat)
        # Selvitetään onko osia enenmän kuin 2 so. liika pilkkuja tai pisteitä
        if osien_maara > 2:
            virhekoodi = 1
            virhesanoma = "Syöttessä on useita desimaalipisteitä tai useita arvoja: vain yksi liukuluku on sallittu, esim. 12.3"
            arvo = 0 
        #TODO: tee osien numeerisuus testi valmisiksi
        # Muussa tapauksessa selvitetään onko alkuosassa pelkkiä numeroita
        else:
            osa = str(osat[0])
            if osa.isnumeric() == False:
                virhekoodi = 2
                virhesanoma = "Syöte sisältää teksiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim. 123.5"
                arvo = 0
            #
            else:
                osa = str(osat[1])
                if osa.isnumeric() == False:
                 virhekoodi = 2
                 virhesanoma = "Syöte sisältää teksiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim. 123.5"
                #  arvo = 0

    # Jos yksiosainen syöte sisäaltää muutakin kuin pelkkiä numeroita
    elif numeroarvo.isnumeric() == False:
        virhekoodi = 2
        virhesanoma = "Syöte sisältää teksiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim. 123.5"
        arvo = 0
       # virhekoodi = 0
        # virhesanoma = "Syöte ok"
    else:
        virhekoodi = 0
        virhesanoma = "Syöte ok"
        arvo = float(numeroarvo)


    # TODO: Muodosta kaksi funktiota: float ja raja-arvotarkistus erillisinä funktioina
    # 
    # Muodostetaan ja palautetaan funktion paluuarvo (lista)
    tulokset = [virhekoodi, virhesanoma, arvo]
    return tulokset

# Jos sanity.py-tiedostoa ajetaan terminaalissa, suoritetaan testit
if __name__ == '__main__':

    # Testataan toimintaa
    # tulos = on_jarkeva('sata', 1, 500)
    #print(tulos)    

# syote = '10.5'
# print(syote.strip(), 'kiloa')

    # Testataan 
    syote = 'sata'
    print(liukuluku_ok(syote, 0 , 500))