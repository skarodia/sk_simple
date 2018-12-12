

#with open('input.txt') as f:
#    content = f.readlines()

a_var = 0
freqs_var = [a_var]
mult_var = False
def part2( a, freqs,mult ):
    with open('input.txt') as f:
        content = f.readlines()
    for line in content:
        line = int(line)
        a = a+ line
        if a in freqs:
            print('first repeating number: ')
            print(a)
            mult = True
            break
        else:
            freqs.append(a)
    if mult == True:        
       #print(a)
       f.close()
    else:
        #print(a)
        #print(freqs)        
        part2( a, freqs, mult )


part2( a_var, freqs_var, mult_var)
#freqs.append(a)
#        : function()

    

#    print( line )
#    print( type(line))
 
#print(a)
#print(freqs)

