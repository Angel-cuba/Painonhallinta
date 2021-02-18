numeroarvo = '123.45'
pilkkunpaikka = numeroarvo.find('.')
print(pilkkunpaikka)
osat = numeroarvo.split('.')
print(osat, 'osia on', len(osat), 'kpl')
print(osat.isnumeric())