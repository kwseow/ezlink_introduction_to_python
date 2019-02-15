import random
name = input("What is your name?")
randnum = random.randint(1,20)
print(randnum)
print("Well %s, I am thinking of a number between 1 and 20"%name)
found = False
for i in range(6):
    if not found:
        guess = int(input("Take a guess"))
        if guess == randnum:
            found = True
            break
        else:
            if (guess < randnum):
                print("Your guess is too low")
            else:
                print("Your guess is too high")


if found:
    print("Good job, %s! You guessed my number in %i guess" % (name, i + 1))
else:
    print("Nope. The number I was thinking of was %i" % randnum)
