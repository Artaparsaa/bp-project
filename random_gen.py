import math
import time

class rand :
    def __init__(self, seed=int(time.time())): # Linear congruential generator
        self.seed = seed

    def rand(self):
        self.seed = (1103515245*self.seed + 12345) & 0x7fffffff 
        return self.seed / 0x7fffffff

    def rand_int(self, a, b) : # random int dar baze [a, b]
        return int((b + 1 - a) * self.rand() + a)

    def rand_float(self, a, b) : # random float dar baze [a, b)
        return (b - a) * self.rand() + a

    def rand_normal(self, m, s) : # random dar tozi'e normal ba miangin m va enheraf meyar s
        return math.sqrt(-2 * math.log(self.rand())) * math.cos(2 * math.pi * self.rand()) * s + m