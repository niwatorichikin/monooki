C = 'Yvccfnficu!'
C = list(C)
for i in range(26):
    m = ''
    for c in C:

        if c.isalpha():
            if c.islower():
                n = (ord(c)+i)
                if n > ord('z'):
                    n = (ord('a')+n-ord('{'))
                m += chr(n)
                    
            elif c.isupper():
                    n = (ord(c)+i)
                    
                    if n > ord('Z'):
                        n = (ord('A')+n-ord('['))
                    m += chr(n)        

             
        
        else:
            m += c
    
    print(m)
