# Protein Synthesis Simulator in Python

This repository contains a protein synthesis simulator in Python. The program generates DNA data, transcribes it to RNA, and translates it to proteins using a basic ribosome model.

## Code Structure

- `DNA_Generator.py`: Contains the `DNA_Generator` class, which generates DNA data.
- `ADN.py`: Defines the `ADN` class to represent DNA and calculate the complementary strand.
- `ARN.py`: Defines the `ARN` class to represent RNA and perform transcription from a DNA sequence.
- `Ribosoma.py`: Defines the `Ribosoma` class for translating RNA to proteins.
- `main.py`: Contains the main function (`main`) that uses the above classes to simulate protein synthesis.

## Usage

Make sure you have Python installed on your system. You can clone this repository and run the following command to start the simulation:

```bash
python main.py
```

## Class Details

### `DNA_Generator`

The `DNA_Generator` class generates DNA sequences and includes the following methods:

- `gen_dna()`: Generates a DNA sequence using a list of codons and a start and end codon.
- `gen_data(n_gen)`: Generates a list of DNA sequences using `gen_dna()`.

### `ADN`

The `ADN` class represents a DNA sequence and includes the following methods:

- `__init__(random, data)`: Initializes a DNA object. If `data` is provided, it is used as the DNA sequence; otherwise, it is generated randomly.
- `calculate_complementary_strand(dna_sequence)`: Calculates the complementary strand of a DNA sequence.

### `ARN`

The `ARN` class represents an RNA sequence and includes the following methods:

- `__init__(adn)`: Initializes an RNA object from a DNA object, performing transcription by replacing 'T' with 'U'.
- `getData()`: Gets the RNA sequence.

### `Ribosoma`

The `Ribosoma` class represents a ribosome and includes the following method:

- `makeProtein(arn)`: Translates an RNA sequence into a list of amino acids using a codon-to-amino acid dictionary.

## Functionality

The program generates DNA data and creates a list of DNA objects. It then transcribes each DNA sequence to RNA and uses a ribosome to translate the RNA to proteins. The DNA sequence, the mRNA sequence, and the translated protein for each DNA in the list are printed.

## Contribution

If you'd like to contribute to the development of this protein synthesis simulator, you can do the following:

1. Fork the repository.
2. Make your changes and improvements.
3. Create a pull request describing the changes made.

Thank you for contributing!
