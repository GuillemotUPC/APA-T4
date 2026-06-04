"""
aleatorios.py

Autor/a: [El Teu Nom i Cognoms]
Descripció: Implementació d'un generador de nombres pseudoaleatoris
utilitzant l'algorisme de Generació Lineal Congruent (LGC).
Inclou una classe iteradora `Aleat` i una funció generadora `aleat()`.
"""

class Aleat:
    """
    Generador de nombres aleatoris usant el mètode LGC (classe iteradora).
    
    Atributs:
        m (int): Mòdul.
        a (int): Multiplicador.
        c (int): Increment.
        x (int): Valor actual de la seqüència (llavor).
        
    Mètodes:
        __next__(): Calcula i retorna el següent nombre aleatori.
        __call__(nova_semilla): Reinicia la seqüència amb una nova llavor.
        
    Proves unitàries:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15
    
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nova_semilla):
        self.x = nova_semilla


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Generador de nombres aleatoris usant el mètode LGC (funció generadora).
    
    Paràmetres:
        m (int): Mòdul.
        a (int): Multiplicador.
        c (int): Increment.
        x0 (int): Llavor inicial.
        
    Retorna:
        Genera (yield) el següent nombre pseudoaleatori de la seqüència.
        
    Proves unitàries:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        nova_semilla = yield x

        if nova_semilla is not None:
            x = nova_semilla
