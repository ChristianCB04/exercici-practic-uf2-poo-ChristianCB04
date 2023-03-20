from nuevo import Pastis

pastis_1 = Pastis(160)
pastis_2 = Pastis(120)
pastis_3 = Pastis(180)
pastis_4 = Pastis(220)
pastis_5 = Pastis(130)

pastissos_sense_xoco = list()

pastissos_sense_xoco.append(Pastis())
pastissos_sense_xoco.append(Pastis())
pastissos_sense_xoco.append(Pastis())
pastissos_sense_xoco.append(Pastis())
pastissos_sense_xoco.append(Pastis())

len(pastissos_sense_xoco)

def xocolatejar(pastis):
    pastis.xocolata = True
    return pastis

for pastis in pastissos_sense_xoco:
    print(pastis.xocolata)