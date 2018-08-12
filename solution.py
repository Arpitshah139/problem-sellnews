import random
def solution():
    #map alphabet with index position
    alphabet = {'a':0,'b':1,'c':2, 'd':3, 'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14}
    # create an list of 15 with zero's
    result = [0] * 15
    # define columns of matrix
    column = 5
    # define rows of matrix
    row =3
    # define matrix of 3*5
    matrix = [[0 for x in range(column)] for y in range(row)]

    # generate matrix that contains random characters from a-o
    for i in range(0,3):
        for j in range(0,5):
            r = random.choice(alphabet.keys())
            matrix[i][j] = r
    print "random matrix:"
    print matrix

#input as per problem

    ip = [[0,0,0,0,0],
[0,0,0,0,1],
[0,0,0,1,0],
[0,1,2,1,0],
[0,1,2,0,0],
[0,1,0,1,0],
[1,0,0,0,0],
[0,1,0,0,0],
[2,0,2,0,0],
[1,1,1,1,1],
[2,2,2,2,2],
[1,2,1,0,1],
[0,0,0,1,2],
[0,0,0,2,2],
[1,2,2,2,2],
[2,0,0,0,0],
[2,1,1,0,0],
[1,0,0,0,1],
[2,0,0,0,2],
[1,1,2,2,1]]


    # # input from user take 5 value comma separated
    # ip = []
    # print "Enter the input : "
    # for i in range(0,2):
    #     inpt = raw_input()
    #     numbers = map(int, inpt.split(','))
    #     if len(numbers) == 5:
    #         if all(i in [0, 1, 2] for i in numbers):
    #             ip.append(numbers)
    #             print "Your input is right"
    #         else:
    #             print "rows should have in 0,1,2"
    #             return
    #     else:
    #         print "wrong input You have to enter 5 numbers with value 0,1,2 by comma seperate"
    #         return


    # for every input increament result array by 1 where index of result matrix equal to value of symbol in alphabet
    # dictionary
    for numbers in ip:
        for i in range(0,5):
            result[alphabet[matrix[numbers[i]][i]]] = result[alphabet[matrix[numbers[i]][i]]] + 1

        # so we check that if any position of result array grather than three so we can declare it to win otherwise lost
        flag = any(i >= 3 for i in result)
        if (flag == False):
            print "LOSING INPUT IS "+str(numbers)
        else:
            print "WINNING INPUT IS "+str(numbers)
        result = [0] * 15

solution()