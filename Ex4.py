def passing():

    str = input()
    strIDPass = []
    strIDToCheck = []
    count = 0

    for num in str:
        if num.isdigit():
            strIDPass.append(int(num))
            if str[len(str)-2] == num:
                strIDToCheck.append(count)
            count += 1


    strIDPass.pop(len(strIDPass)-1)

    try:
        print(tuple(strIDPass[strIDToCheck[0]:strIDToCheck[1]+1]))
    except:
        print(())
passing()