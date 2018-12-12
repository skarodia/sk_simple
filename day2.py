from collections import Counter


l = 'ybruvapdgixszyckwtfqjonsie'

TwoCount = 0
ThreeCount = 0

with open('input2.txt') as f:
    content = f.readlines()
    for line in content:

        c = Counter(line)
        d = set( c.values() )
        if 2 in d: TwoCount= TwoCount+1
        if 3 in d: ThreeCount = ThreeCount+1

print( TwoCount )
print( ThreeCount )
print( TwoCount*ThreeCount )
