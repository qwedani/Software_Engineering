def deleteElemet():

    str = input()
    strNums = []

    for num in str:
        if num.isdigit():
            strNums.append(int(num))

    positionToDelete = strNums.pop(len(strNums)-1)

    if len(strNums) < positionToDelete:
        tupleNums = tuple(strNums)
        print(tupleNums)
    else:
        strNums.remove(positionToDelete)
        tupleNums = tuple(strNums)
        print(tupleNums)

deleteElemet()