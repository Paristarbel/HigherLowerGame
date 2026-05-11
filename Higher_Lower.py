print("         WELCOME TO HIGHER LOWER GAME😊⭐         ")
print("*****Choose which person has MORE Instagram followers*****")

score=0
def higher():
    Questions=[]
    Q1="Ariana Grande is a musician and actress from the United States."
    Q2="Taylor Swift is a musician from the United States."
    Q3="Cristiano Ronaldo is a football player from Portugal."
    Q4="Zendaya is an actress and musician from the United States."
    Q5="Lionel Messi is a football player from Argentina."
    Q6="Justin Bieber is a musician from Canada."
    Q7="Kim Kardashian is a media personality and businesswoman from the United States."
    Q8="Neymar Jr is a football player from Brazil."
    Q9="Billie Eilish is a musician from the United States."
    Q10="Selena Gomez is a musician and actress from the United States."

    Questions.append(Q1)
    Questions.append(Q2)
    Questions.append(Q3)
    Questions.append(Q4)
    Questions.append(Q5)
    Questions.append(Q6)
    Questions.append(Q7)
    Questions.append(Q8)
    Questions.append(Q9)
    Questions.append(Q10)

    print(Questions)
    answer=input("Who has more followers? Type 'A' or 'B':").lower()

higher()