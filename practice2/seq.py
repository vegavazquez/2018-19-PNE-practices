class Seq:


def __init__(self, strbase):
    self.strbase = strbase


def len(self): #longitud
    return len(self.strbase)


def complement(self): #fmetodo que te da la letra complementaria en una cadena de adn , si la letra es A, el output, la letra complementaroa es T, contandolas
    output = '' #lista vacia que se va rellenando con los comando siguientes dentro de la funcion
    for letter in self.strbase:
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'
    return Seq(output)


def reverse(self): #hebra contraria
    return Seq(self.strbase[::-1])


def count(self, base): #contador de bases
    contador = 0
    for letter in self.strbase:
        if (base == letter):
            cont = cont + 1
    return cont


def porc(self, base):
    return round((float(self.count(base)) / float(self.len())) * 100, 1)


def get_strbase(self):
    return self.strbase
