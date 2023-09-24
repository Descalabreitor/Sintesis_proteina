import numpy as np

class DNA_Generator:

    information_codons = ["AUG", "UUU", "UUC", "UUA", "UUG", "UCU", "UCC", "UCA", "UCG",
                     "UAU", "UAC", "UGU", "UGC", "UGG", "CUU", "CUC", "CUA", "CUG",
                     "CCU", "CCC", "CCA", "CCG", "CAU", "CAC", "CAA", "CAG", "CGU",
                     "CGC", "CGA", "CGG", "AUU", "AUC", "AUA", "AUG", "ACU", "ACC",
                     "ACA", "ACG", "AAU", "AAC", "AAA", "AAG", "AGU", "AGC", "AGA",
                     "AGG", "GUU", "GUC", "GUA", "GUG", "GCU", "GCC", "GCA", "GCG",
                     "GAU", "GAC", "GAA", "GAG", "GGU", "GGC", "GGA", "GGG"]

    start_codon = "AUG"
    end_codons = ["UAA", "UAG", "UGA"]

    def __init__(self, dna_len=12):
        if dna_len % 3 != 0:
            raise ValueError("dna_len must be a multiple of 3")
        self.dna_len = dna_len

    def gen_dna(self):
        data =  ''.join(np.random.choice(self.information_codons) for _ in range(self.dna_len / 3))
        return ''.join([self.start_codon, data, np.random.choice(self.end_codons)])
    
    def gen_data(self, n_gen=10):
        return [self.gen_dna() for _ in range(n_gen)]
