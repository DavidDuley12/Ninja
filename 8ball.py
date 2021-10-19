import random  

name = input("Hello there, What is your name")

def intro_greeting():
    global random_number
    random_number = random.randint(1, 9)
    global question
    question = input("What is your question for the all-knowing 8-Ball? ")
    print(random_number)
# answer = str("")

def eight_ball_replies():
    intro_greeting()

    if random_number == 1:
      answer = "Yes,most deffinitly"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 2:
      answer = "Sure why not"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 3:
      answer = "Yes,of course"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 4:
      answer = "answer a little hazy,try again later"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 5:
      answer = "Can not answer at the moment"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 6:
      answer = "My sources say no"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 7:
      answer = "Not the best idea"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 8:
      answer = "No you should not"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 9:
      answer = "I would not consider"
      print(name +" asks: "  + question)
      print("Magic 8-Ball's answer: " + answer)
    else:
      answer = "Error"

eight_ball_replies()
# print(answer)
# print(name +" asks: "+ question)
#

# print("Magic 8-Ball's asnwer: " + answer)

# run_again = print("Do you want to run again?")

def play_again():
    run_again = input("Do you want to run again? y/n:")
    if run_again == "y":
       eight_ball_replies()
       play_again()
    else:
         print("Thanks for playing.")

play_again()