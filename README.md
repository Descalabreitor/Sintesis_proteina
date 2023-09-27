# Simulador de Síntesis de Proteínas en Python

Este repositorio contiene un simulador de síntesis de proteínas en Python. El programa genera datos de ADN, transcribe a ARN y traduce a proteínas utilizando un modelo básico de ribosoma.

## Estructura del Código

- `DNA_Generator.py`: Contiene la clase `DNA_Generator`, que genera datos de ADN.
- `ADN.py`: Define la clase `ADN` para representar el ADN y calcular la hebra complementaria.
- `ARN.py`: Define la clase `ARN` para representar el ARN y realizar la transcripción a partir de una secuencia de ADN.
- `Ribosoma.py`: Define la clase `Ribosoma` para la traducción de ARN a proteínas.
- `main.py`: Contiene la función principal (`main`) que utiliza las clases anteriores para simular la síntesis de proteínas.

## Uso

Asegúrate de tener Python instalado en tu sistema. Puedes clonar este repositorio y ejecutar el siguiente comando para iniciar la simulación:

```bash
python main.py
```

## Detalles de las Clases

### `DNA_Generator`

La clase `DNA_Generator` genera secuencias de ADN y contiene los siguientes métodos:

- `gen_dna()`: Genera una secuencia de ADN utilizando una lista de codones y un codón de inicio y fin.
- `gen_data(n_gen)`: Genera una lista de secuencias de ADN utilizando `gen_dna()`.

### `ADN`

La clase `ADN` representa una secuencia de ADN y contiene los siguientes métodos:

- `__init__(random, data)`: Inicializa un objeto ADN. Si se proporciona `data`, se utiliza como la secuencia de ADN; de lo contrario, se genera aleatoriamente.
- `calcular_hebra_complementaria(secuencia_adn)`: Calcula la hebra complementaria de una secuencia de ADN.

### `ARN`

La clase `ARN` representa una secuencia de ARN y contiene los siguientes métodos:

- `__init__(adn)`: Inicializa un objeto ARN a partir de un objeto ADN, realizando la transcripción cambiando 'T' por 'U'.
- `getData()`: Obtiene la secuencia de ARN.

### `Ribosoma`

La clase `Ribosoma` representa un ribosoma y contiene los siguientes métodos:

- `makeProtein(arn)`: Traduce una secuencia de ARN en una lista de aminoácidos utilizando un diccionario de codones a aminoácidos.

## Funcionamiento

El programa genera datos de ADN y crea una lista de objetos ADN. Luego, transcribe cada ADN a ARN y utiliza un ribosoma para traducir el ARN a proteínas. Se imprime la secuencia de ADN, la secuencia de ARNm y la proteína traducida para cada ADN en la lista.

## Contribución

Si deseas contribuir al desarrollo de este simulador de síntesis de proteínas, puedes hacer lo siguiente:

1. Fork del repositorio.
2. Realiza tus cambios y mejoras.
3. Crea un pull request describiendo los cambios realizados.

¡Gracias por contribuir!# Protein Synthesis Simulator in Python

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
