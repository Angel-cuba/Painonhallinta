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
       korjattu_syote= puhdistettu_syote.replace(',', '.')
    
    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('An exception occurred, just numbers')
        luku = 0
    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if  luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella          
    try:
        if  luku > alaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Palautetaan luku
    return luku

 # Testataan toimintaa
    tulos = on_jarkeva('sata', 1, 500)
    print(tulos)