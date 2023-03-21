def suma(x,y):
    return x+y

print(suma(4,6))


resta = lambda x, y: x - y
print(resta(10,5))

def calcula(x,y,operacion):
    return operacion(x,y)

print(calcula(3,8,suma))
print(calcula(9,5,resta))
print(calcula(2,3,lambda x,y:y*x))
print(calcula(2,3,lambda x,y:y/x))