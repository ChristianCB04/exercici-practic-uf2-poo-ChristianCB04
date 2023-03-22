from pastisseria import Pastis
import copy

pastis_1 = Pastis(160)
pastis_2 = Pastis(120)
pastis_3 = Pastis(180)
pastis_4 = Pastis(220)
pastis_5 = Pastis(130)

pastissos = list()

pastissos.append(pastis_1)
pastissos.append(pastis_2)
pastissos.append(pastis_3)
pastissos.append(pastis_4)
pastissos.append(pastis_5)

print(pastis_1)

len(pastissos)

for pastis in pastissos:
    print(pastis.xocolata)
    
def xocolatejar(pastis):
    pastis_copia = copy.copy(pastis)
    pastis_copia.xocolata = True
    return pastis_copia
pastis_amb_xocolata = list((map(xocolatejar,pastissos)))

for pastis in pastissos:
    pastis_tempora1 =xocolatejar(pastis)
    pastis_amb_xocolata.append(pastis_tempora1)
    
for pastis in pastissos:
    print(pastis.xocolata)
    
for pastis in pastis_amb_xocolata:
    print(pastis.xocolata)
    