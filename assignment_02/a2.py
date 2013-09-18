def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1
    
def is_valid_sequence(str):
    '''(str) -> bool
    
    Checks whether a str contains only 'A', 'T', 'G' ot 'C'.
    
    >>> is_valid_sequence("AATG")
    True
    >>> is_valid_sequence("")
    False
    >>> is_valid_sequence("Aatg")
    False
    '''
    if str == '':
        return False
    for char in str:
        if not (char in 'ATGC'):
            return False
    return True

def insert_sequence(str1, str2, idx):
    '''(str, str, int) -> str

    Insert str2 into str1 at posiiton idx.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    
    '''
    return str1[:idx] + str2 + str1[idx:len(str1)]

def get_complement(str):
    '''(str) -> str

    Return a complementary nucleotide to the given nucleotide.

    >>> get_complement('A')
    T
    >>> get_complement('C')
    G
    >>> get_complement('a')
     # empty string
    '''
    if str == 'A':
        return 'T'
    elif str == 'T':
        return 'A'
    elif str == 'G':
        return 'C'
    elif str == 'C':
        return 'G'
    else:
        return ''

def get_complementary_sequence(str):
    ''' (str) -> str

    >>> get_complementary_sequence('AAA')
    TTT
    >>> get_complementary_sequence('aaa')
      # empty string

    '''
    result = ''

    for chr in str:
        result = result + get_complement(chr)

    return result
    
