class Pastis:
    def __init__(self, pes = 50, xocolata = False):
        self.__pes = pes
        self.__xocolata = xocolata

    @property
    def pes(self):
        return self.__pes
    
    @pes.setter
    def pes(self, value):
        if value > 0:
            self.__pes = value
        else:
            print(f"{value} is invalid")
            
    @property
    def xocolata(self):
        return self.__xocolata
    
    @xocolata.setter
    def xocolata(self, value):
        if value is True or value is False:
            self.__xocolata = value
            
    def __str__(self):
        return f"Pastis despres{self.__pes}. Xocolata?"

pastis_1 = Pastis(-60)
print(pastis_1.pes)

pastis_1.pes = -50
print(pastis_1.pes)
