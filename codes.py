# Coding Theory Project: Sept 2015 - Dec 2015
# Author: Kaman Phamdo
# Mentor: Sean Ballentine
# University of Maryland

from math import factorial as fac, floor, ceil, log

# returns the hamming distance between the two parameter vectors, which should
# be two vectors of the same length
def hDist(v, w):
    d=0
    
    for index in range(0, len(v)):
        if (v[index] != w[index]):
            d += 1
    return d

# returns a list of all vectors in the vectorspace of vectors with length 'n' 
# over [0, 1]. The list will have 2^n total vectors.
def vspace(n):
    poss = 2**n
    list = [[0 for x in range(n)] for x in range(poss)]
    for i in range(0, poss):
        for j in range(0, n):
            list[i][j] = int(i % (2**(n-j)) // (2**(n-j-1)))
    return list

# given a list of vectors, returns a reduced list of vectors within the 
# parameter list that are a hamming distance of at least 'd' away from the 
# vector 'x'
def reduce(x, list, d):
    newlist = []
    for i in range(0, len(list)):
        if (hDist(list[i], x) > (d-1)):
            newlist.append(list[i])
    return newlist


# returns the size of a hamming ball with radius 'radius' for vectors of length
# 'n'. the ballsize corresponds to the number of vectors of length 'n' that
# have a hamming distance less than or equal to 'radius' from any given vector
def ballsize(radius, n):
    if (radius == 1):
        return (1 + n)
    else:
        return (fac(n)/(fac(radius) * fac(n - radius))) + ballsize(radius-1, n)

# generates a code of the largest size given length 'n' and minimum hamming
# distance 'd', and stores the result into the parameter list 'sol' (should
# be an empty list)
def bestCode(n, d, sol):   
    best=[]
    v = vspace(n)
    sol2 = []
    for i in range(0, len(sol)):
        v = reduce(sol[i], v, d)

    if(len(v) != 0):
        for i in range(0, len(v)):
            sol2 = sol[:]
            sol2.append(v[i])
        sol2 = bestCode(n, d, sol2)
                
    if(len(sol2)>len(best)):
        best = sol2
        return best
    else:
        return sol
        
# returns the largest possible minumum hamming distance (corresponding to the
# best error correcting capability) for a code, given the size and length of 
# the code
def distance(size, length):
    result = length
    while (size * ballsize(floor((result - 1)/2), length) > 2 ** length):
        result = result - 1

    while (len(bestCode(length, result, [])) < size):
        result -= 1
    return result

# returns the largest possible length of codewords for a code of size 'size' and
# minimum hamming distance of 'dist'
def length(size, dist):
    n = int(ceil(log(size, 2)))
    
    radius = floor((n-1)/2)
    while ((size * ballsize(radius, n)) > (2 ** n)):
        n += 1

    while (len(bestCode(n, dist, [])) < size):
        n += 1

    return n

option = 1
while (option != 0):
    print("(0) Quit")
    print("(1) In: Size, Length. Out: Distance")
    print("(2) In: Size, Distance. Out: Length")
    print("(3) In: Distance, Length. Out: Size")
    print("(4) Generate a code")
    option = input("Pick Option: ")

    if (option == 1):
        size = input("Size: ")
        length = input("Length: ")
        print "Calculated distance: ", distance(size, length)
    if (option == 2):
        size = input("Size: ")
        dist = input("Distance: ")
        print "Calculated length: ", length(size, dist)
    if (option == 3):
        dist = input("Distance: ")
        length = input("Length: ")
        print "Calculated size: ", len(bestCode(length, dist, []))
    if (option == 4):
        dist = input("Distance: ")
        length = input("Length: ")
        code = bestCode(length, dist, [])
        for i in code:
            print i