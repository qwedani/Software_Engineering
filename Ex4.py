vowels = ["a","e","i","o","u","A","E","I","O","U"]
counter = 0

string = input("Enter your sentence: ")

# 1. Длина предложения
print(f"Lenght of sentence is {len(string)}")

# 2. Предложение в нижнем регистре
print(f"Your sentence in lower case: {string.lower()}")

# 3. Кол-во глассных
for i in range(len(string)):
    if string[i] in vowels:
        counter += 1
print(f"Amount of vowels is {counter}")
# Альтернативый способ: print(string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u"))

# 4. Замена ugly на beauty
print("Replace ugly with beauty: " + string.replace("ugly","beauty"))

# 5. Проверка начинается ли с The и заканчивается ли на end
if string[:3] == "The" and string[(len(string)-3):(len(string))] == "end":
    print("Your sentence starts with \"The\" and ends with \"end\"")
else:
    print("Your sentence isn't start with \"The\" and end with \"end\"")
