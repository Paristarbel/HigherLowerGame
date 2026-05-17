
from Art import logo
print(logo)

from Game_data import higher_lower_data
import random

account_a=random.choice(higher_lower_data)
account_b=random.choice(higher_lower_data)

if account_a==account_b:
    account_b=random.choice(higher_lower_data)
score=0
game_continuation=True
account_b=random.choice(higher_lower_data)

while game_continuation:
      account_a=account_b
      if account_a==account_b:
            account_b=random.choice(higher_lower_data)
      def format_data(account):
            #Format the account data into printable format
            account_name= account["name"]
            account_descr=account["description"]
            account_country=account["country"]

            return f"{account_name}, a {account_descr} , from {account_country}"

      print(f"Compare A: {format_data(account_a)}")
      from Art import vs
      print(vs)
      print(f"Against B: {format_data(account_b)}")

      # Ask for user to guess
      guess=input("Who has more followers? Type A or B: ").lower()
      print("\n"*20)

      # Check if user is correct 
      def check_answer(user_guess,a_followers,b_followers):
            
            if a_followers >b_followers:
                  return user_guess=="a"
            
            else:
                  return user_guess == "b"
            
      a_follower_count=account_a["followers"]
      b_followers_count=account_b["followers"]
      is_correct= check_answer(guess,a_follower_count,b_followers_count)


      if is_correct:
            score+=1
            print(f"You're right! , Current score {score}")
      else:
            score+=0
            print(f"Sorry, that's wrong.Final score: {score}")
            game_continuation=False