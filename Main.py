from DNA_Generator import DNA_Generator

def dna_to_rnam(dna):
    return dna.replace("T", "U")



def main():
    dna_generator = DNA_Generator()
    data = dna_generator.gen_data(10)
    rnam_list = [dna_to_rnam(dna) for dna in data]


    

if __name__ == "__main__":
    main()