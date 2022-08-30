from ast import Num
from operator import mul


class Tablas:
    num=0
    
    def crearTabla(self):
        for i in range(1,11,1):
            print(self.num," * ", i, " = ", self.num*i)
