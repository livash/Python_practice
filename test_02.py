def mystery(s):
    ''' (str) -> str
    '''
    i  = 0 
    res = ''
    
    while not s[i].isdigit():
        res += s[i]
        i += 1
        
    return res

print(mystery('s1'))
#print(mystery('s'))

# calculate the sum of all odd numbers from 1523 to 10503

result = 0
for i in range(1523, 10503):
    if i % 2 != 0:
        result += i
    
print(result)