name = input("What's your name? ")

def names(variable_name):
    camelCase = ''
    for i in variable_name:
        if i.isupper():
            camelCase += '_' + i.lower()
        else:
            camelCase += i
    return camelCase.lstrip('_')

print(names(name))
