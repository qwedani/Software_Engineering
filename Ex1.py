def getInfo():

    userInfo = input()

    userInfoList = userInfo.split(" ")
    userInfoTuple = tuple(userInfoList)

    print(userInfoList)
    print(userInfoTuple)

getInfo()