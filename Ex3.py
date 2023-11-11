def numCounter(userNums):
    userNums_dic = {}

    for num in userNums:
        if num not in userNums_dic.keys():
            userNums_dic[int(num)] = int(userNums.count(num))

    userNumsTopThree_dic = sorted(userNums_dic.items(), key = lambda x: x[1]) [-3:]

    userNumsTopThreeSorted_dic = sorted(userNumsTopThree_dic)
    print(userNumsTopThreeSorted_dic)

numCounter("9998887777791")