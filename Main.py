from DNA_Generator import DNA_Generator
from ADN import ADN
from ARN import ARN
from Ribosoma import Ribosoma

def main():
    dna_generator = DNA_Generator()
    data = dna_generator.gen_data(10)
    adn_list = [ADN(data=dna) for dna in data]

    for adn in adn_list:
        arn = ARN(adn)
        ribosoma = Ribosoma()
        proteina = ribosoma.makeProtein(arn)
        print("ADN:", adn.data)
        print("ARNm:", arn.getData())
        print("Proteína:", proteina)
        print()

if __name__ == "__main__":
    main()
