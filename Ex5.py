string = "hello"
counter = 0
values = [0,2,4,6,8,10]

while "world" not in string:
    memory = string
    if counter in values:
        string = string + " world"
    print(string)
    if counter < 10:
        string = memory
    counter += 1
