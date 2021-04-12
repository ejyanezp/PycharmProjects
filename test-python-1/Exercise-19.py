from typing import Iterator


# Iterators: obtener el siguiente valor uno por uno
# Iterables: para recorrer los valores de un Iterator (en un for por ejemplo)
class PrimeGenerator:
    # Para evitar warnings del IDE poner el tipo genérico devuelto por el constructor.
    def __init__(self, stop) -> Iterator[int]:
        self.stop = stop
        self.current = 2

    def __next__(self):
        for n in range(self.current, self.stop):
            for i in range(2, 1 + self.current // 2):
                if n % i == 0:
                    break
            else:
                self.current = n + 1
                return n
        raise StopIteration()


pg = PrimeGenerator(20)
# al omitir el tipo "-> Iterator[int]" en el constructor __init__ de la clase,
# se muestra un warning en todos los next, porque el argumento "pg" no es un Iterator
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
