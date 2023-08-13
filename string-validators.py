
s = input()
for c in [s]:    
    if c in [s]:
        c =s.isalnum()
    print ((True))
    if c in [s]:
        c =s.isalpha()
    print ((True))
    if c in [s]:
        c =s.isdigit()
    print ((True))
    if c in [s]:
        c =s.islower()
    print ((True))
    if c in [s]:
        c =s.isupper()
    print ((True))


'''
s = input()
for c in [s]:    
    if c in [s]:
        c =s.isalnum()
    if c in [s]:
        c =s.isalpha()
    if c in [s]:
        c =s.isdigit()
    if c in [s]:
        c =s.islower()
    if c in [s]:
        c =s.isupper()

'''
'''


s = input()
print(any([c.isalnum() for c in s]))
print(any([c.isalpha() for c in s]))
print(any([c.isdigit() for c in s]))
print(any([c.islower() for c in s]))
print(any([c.isupper() for c in s]))
'''

