def count_matches(s1, s2):
    """ (str, str) -> int
    Return the number of positions in s1 that
    contain the same character in s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    """
    result = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += 1
    return result


def sum_items(list1, list2):
    """ () -> 
    Return a new list in which each item is the sum of items
    at the corresponding positions in list1 and list2
    
    Precondition: len(list1) == len(list2)
    
    >>> sum_items([1,2,], [2,2])
    [3,3]
    """
    result = []
    for i in range(len(list1) - 1):
        result.append(list1[i] + list2[i])
        
    return result

def shift_left(L):
    """ (list) -> NoneType
    
    Shift each item in L one position to the left
    and shift the first item to the last position.
    
    Precondition: len(L) >= 1    
    """
    first_item = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]
    L[-1] = first_item
        

def count_adjacent_repeats(s):
    """ (str) -> int
    Returns the number of occurances of a character and an adjecent
    character being the same.
    
    >>> count_adjacent_repeats('abccdeffggh')
    3
    """
    repeats = 0
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats += 1
            
    return repeats

def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

def shift_right(L):
    ''' (list) -> NoneType
    Shifts elements of the list L to the right
    
    '''
    last_item = L[-1]
    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
    L[0] = last_item

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list
    
    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.
    
    Precondition: len(list1) == len(list2)
    
    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''
    
    pairs = []
    
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])
        
    return pairs

def contains(value, lst):
    """ (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False  # We have not yet found value in the list.

    # CODE MISSING HERE
    for sublist in lst:
        if value in sublist:
            found = True

    return found

print(count_adjacent_repeats('abccdeffggh'))
