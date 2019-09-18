def question():
    not_quit = True
    response = input("what is your question?")

    if response != "quit":
        while not_quit == True:
            if response[-1] == "?":
                not_quit = False
            else:
                print("I'm sorry, I can only answer questions.")
                response = input("what is your question?")
