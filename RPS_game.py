import random

choice=["scissors", "paper", "rock"]
st={
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

while True:
    fuad=input("Choose rock, paper or scissors: "). lower()
    if fuad in st:
        fuad=st[fuad]

    if (fuad=="quit"):
        print("ok, have a nice day fuad!")
        break
    if fuad not in choice:
        print("plz fuad choose any of this.")
        continue

    computer=random.choice(choice)
    print("Computer chose:", computer)

    if fuad==computer:
        print("damn its  a tie")
    elif (fuad=="rock" and computer=="scissors") or \
        (fuad=="paper" and computer=="rock") or\
        (fuad=="scissors" and computer=="paper"):
        print("Damn,fuad win!")
    else:
        print("Sorry you losse!")
