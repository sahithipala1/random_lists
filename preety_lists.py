list_of_shame = []

while True:
    name = input("what is your name ?")
    age = input("what is your age?")
    pref = input("what is your computer platform?")
    row = [name, age, pref]
    list_of_shame.append(row)
    exit = input("y/n")
    if exit.strip().lower()[0] == "y":
        break

print(list_of_shame)
