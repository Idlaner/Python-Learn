#Guess the answer using loop
print("This is a Manchester United player")
secret_person = "Harry Maguire"

guess = ""
guess_count = 0
guess_limit = 5
outof_guess = False
while guess != secret_person and not(outof_guess):
    if guess_count < guess_limit:
        guess = str(input("Guess a player: "))
        guess_count = guess_count + 1
    else:
        outof_guess = True
if outof_guess:
    print("You lose!")
else:
    print("Congratulations!")
