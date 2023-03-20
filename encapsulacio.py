class Myclass():
    def __init__(self):
        self.__superprivate  = "Hello"
        self._semiprivate  = ", World!"
        
mc = Myclass()

print(mc._Myclass__superprivate)

print(mc._dict__)