def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print greet('es'), 'Glenn'
print greet('fr'), 'Sally'
print greet('ir'), 'Jimbob'

def addtwo(a,b):
    return a + b
x = addtwo(4,2)
print x


