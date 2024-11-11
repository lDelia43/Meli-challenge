"""
    Determines if a sequence of letters is a mutant sequence.
    A sequence is considered mutant if there is more than one sequence of four
    sequence (list of str): A list of strings representing a sequence of letters
    returns a boolean: True if the sequence is mutant and False otherwise
"""
def check_sequence(sequence):
    return len(sequence) >= 4 and all(x == sequence[0] for x in sequence)


"""
    Determines if a human is a mutant based on their DNA sequence.
    A human is considered a mutant if there is more than one sequence of four
    identical letters (A, T, C, G) consecutively aligned horizontally, 
    vertically, or diagonally in the DNA sequence matrix.
    dna (list of str): A list of strings representing an NxN matrix
    returns a boolean: True if the human is a mutant and False otherwise
"""
def is_mutant(dna):
    dna_lenght = len(dna)
    sequences_found = 0

    # Check horizontal
    for row in dna:
        for i in range(dna_lenght - 3):
            if check_sequence(row[i:i + 4]):
                sequences_found += 1
                if sequences_found > 1:
                    return True
                
    # Check vertical
    for col in range(dna_lenght):
        for row in range(dna_lenght - 3):
            if check_sequence([dna[row + i][col] for i in range(4)]):
                sequences_found += 1
                if sequences_found > 1:
                    return True
                
    # Check diagonal right
    for row in range(dna_lenght - 3):
        for col in range(dna_lenght - 3):
            if check_sequence([dna[row + i][col + i] for i in range(4)]):
                sequences_found += 1
                if sequences_found > 1:
                    return True
                
    # Check diagonal left
    for row in range(dna_lenght - 3):
        for col in range(3, dna_lenght):
            if check_sequence([dna[row + i][col - i] for i in range(4)]):
                sequences_found += 1
                if sequences_found > 1:
                    return True

    return False