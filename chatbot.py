print("Good evening")
print("Type 'bye' to exit.\n")

while True:
    user = input("you: ").lower()
    if user == "heyy":
        print("bot:Hello master,how can i serve you today? ")
    elif user == "how you doi'n":
        print("bot:i am doing great,thanks for asking ")
    elif user == "who made you?":
        print("bot:i was made by my master parth")
    elif user == "what is the capital of india?":
        print("bot:it's new delhi")
    elif user == "which is your favourite comfart food?":
        print("bot: I love to eat farsan and chivda")
    elif user == "bye" or user == "exit":
        print("bot:exiting...")
        break
    else:
        print("bot:sorry master i am unable to understand your question")
