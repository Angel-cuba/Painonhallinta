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