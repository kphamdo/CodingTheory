#assuming list1 and list2 have the same number of entries
#return the hamming distance between list1 and list2
def hammingDistance(list1, list2):

    distance = 0
    for index in range(0, len(list1)):
        if (list1[index] != list2[index]):
            distance += 1
    return distance


#returns all possible vectors in the vectorspace [0,1] of the given length
def vectorspace(length):
    #number of possibilities given the size of vectors
    possibilities = 2 ** length
    list = [[0 for x in range(length)] for x in range(possibilities)]
    for i in range(0, possibilities):
        for j in range(0, length):
            list[i][j] = int(i % (2 ** (length - j)) // (2 ** (length - j - 1)))
    return list

#returns the subset of the vectorspace(length) that has a hamming distance
#of distance from the zero vector of length "length"
def subset(length, distance):
    set = vectorspace(length)
    subset = []
    subset.append(set[0])
    for i in range(len(set)):
        if (hammingDistance(set[i], set[0]) >= distance):
            subset.append(set[i])
    return subset


#returns the maximum size for a subset of vectors of the given length
#that all have a hamming distance given by distance
def maxDistanceSubset(length, distance):
    #list[0] is always the zero vector
    list = subset(length, distance)
    solution = []
    solution.append(list[0])
    solutionFound = False
    i = 1
    max = 0
    numSolutions = 0
    while(i < len(list)):
        solution.append(list[i])
        for j in range(1, len(list)):
            works = True
            for vector in solution:
                if ((hammingDistance(list[j], vector)) < distance):
                    works = False
            if works == True:
                solution.append(list[j])
        if (len(solution) >= max):
            max = len(solution)
            #print(max, ": ", solution)
            numSolutions += 1
        solution.clear()
        solution.append(list[0])
        i += 1
    #print("num solutions: ", numSolutions)
    return max


for i in range(5, 8):
    for j in range(3, i):
        print("length:", i, " distance:",j, " max subset size:", maxDistanceSubset(i, j))