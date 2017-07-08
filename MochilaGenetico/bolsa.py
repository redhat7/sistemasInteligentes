class Bolsa(object):

    def __init__(self, id_, rng, peso = None, precio = None):
        '''
        Constructor
        '''

        self.id = id_
        self.precio = precio
        self.peso = rng.randint(0, 500) if peso is None else peso # Al azar si no pasa nada
        self.precio = rng.randint(0, 500) if precio is None else precio # Al azar si no pasa nada

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Bolsa(id = {0}, peso = {1}, precio = {2})'.format(self.id, self.peso, self.precio)
