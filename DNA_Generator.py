import numpy as np

class DNA_Generator:

    bases = ["A", "C", "G", "T"] 

    def __init__(self, dna_len = 12 ):
        if dna_len % 3 != 0:
            raise print("dna len must be a multiple of 3 \n")
        self.dna_len = dna_len

    def gen_dna(self):
        return  ''.join(np.random.choice(self.bases) for _ in range(self.dna_len))

    def gen_data(self,  n_gen = 10):
        return [self.gen_dna() for _ in range(n_gen)]