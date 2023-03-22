def suma(x, y):
    return x+y

print(suma(4,6))

resta = lambda x, y: x - y
print(resta(10, 5))

def calcula(x, y, operacio):
    return operacio(x, y)

print(calcula(3, 8, suma))
print(calcula(10, 8, resta))
print(calcula(2, 3, lambda x, y: x*y))
print(calcula(6, 2, lambda x, y: x/y))

my_list = [12, 65, 34, 56, 76, 32]

result = list(filter(lambda x:(x % 13 == 0), my_list))

print(result)

noms = {"Aida", "Jordi", "Arnau", "Alex", "Dani"}

def startsWithWovel(word):    
    word_lower = word.lower()
    if word_lower.startswith('a'):
        return True 
    if word_lower.startswith('e'):
        return True 
    if word_lower.startswith('i'):
        return True 
    if word_lower.startswith('o'):
        return True 
    if word_lower.startswith('u'):
        return True 
    return False


noms_startsWovel = list(filter(startsWithWovel, noms))

print(list(filter(lambda x: x[0].lower() in 'aeiou', noms)))

print(list(filter(lambda x: (x[0].lower() in 'aeiou')and (len(x)>4), noms)))