class Pastis:
    def __init__(self, pes, xocolata = False):
        self.pes = pes
        self.xocolata = xocolata

## Instanciació
pes = 150 #grams
pastis_1 = Pastis(pes)
pastis_2 = Pastis(pes)
pastis_3 = Pastis(200)
pastis_xocolata = Pastis(200, True)

bossa = list()
bossa.append(pastis_2)
bossa.append(pastis_3)
bossa.append(pastis_xocolata)

for pastis in bossa:
    if pastis.xocolata == True:
        print("Xocolata!")

print(pastis_xocolata.pes)
print(f"pastis_xocolata és de xocolata? {pastis_xocolata.xocolata}")