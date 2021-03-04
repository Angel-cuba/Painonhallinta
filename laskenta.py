# Modulin funktioilla voidaan laskea painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """Laskee painoindeksi kaavalla paino jaettuna pituuden neliöllä

    Args:
        paino (float): paino kiloina (kg)
        pituus (float): pituus metreinä (mm)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / pituus ** 2
    return painoindeksi

# Aikuisen rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
    """[summary]

    Args:
        bmi (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli (): 1 - Miehet, 0 - Naiset

    Returns:
        float: Kehon rasvaprosentti
    """
    rprosentti = 1.2 * bmi + 0.23 * ika -10.8 * sukupuoli - 5.4
    return rprosentti

# Testit
if __name__ == '__main__':

    # 1. testi omapainoindeksi
    pituus = 1.71
    paino = 74.9
    omabmi = bmi(paino, pituus)
    print('Pituus:', pituus, 'Paino: ', paino, 'Painoindeksi', omabmi)

    # 2. testi oma rasvaprosentti
    ika = 59
    sukupuoli = 1
    print('Rasvaprosentti: ', rasvaprosentti(omabmi, ika, sukupuoli))