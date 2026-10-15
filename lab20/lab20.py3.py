#Guess the number
#store a secret number between 1 and 50
#keep asking until they get right
#after each wrong,guess,print "too high" or "too low"
#print how many attempt it took
#stop after 7 attempts and reveal the number.
secret_number = 31
attempts=0
while True:
    guess=int(input("guess the number (1-50):"))
    attempts +=1
    if guess == secret_number:
        print("correct")
        print(f"you got it in {attempts} attempt.")
        break
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")
    if attempts == 7:
        print("out of attempts!")
        print(f"The secret number was {secret_number}")
        break