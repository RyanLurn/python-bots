while True:
    user_input = input("User: ")
    if user_input == "/exit":
        break
    echo = "Echo Bot: " + user_input  # Notice the space at the end after the ":"
    print(echo)
