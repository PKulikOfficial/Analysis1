#-----------------------------------------------------------#
#Input van de gebruiker.
instruments = int(input())

#-----------------------------------------------------------#
def amplify(n):
    #Som van de unieke cijfers berekenen.
    s = set(str(n))
    SumS = sum(tuple(map(int, s)))
    
    #Aantal unieke cijfers in het getal.
    b = len(set(str(n)))
    if b == 1:
        b = 10
        
    #Berekening van de som door de basis.
    TempS = SumS
    x = ''
    while TempS > 0:
        m = TempS % b
        x = str(m) + x
        TempS = TempS // b
    return n,SumS,b,x

#-----------------------------------------------------------#
#Output die de gebruiker ontvangt.
print(amplify(instruments))

#TESTREGELS
for x in (1,2,12,1221,123456789, 123123123123456789999, 1359,9531, 315191):
    print(*amplify(x))


#Patryk Kulik
#0989317
#INF1J
