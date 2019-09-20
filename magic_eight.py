import random

# B - pick a random answer


def question():
    ans_list_b = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]
    ans_b = random.choice(ans_list_b)

    # Question_C answer is here:
    answer_c_list =["Reply hazy, try again.","Ask  again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    answer_c_item = random.choice(answer_c_list)
# <<<<<<< HEAD

    not_quit = True
    response = input("what is your question?")

    if response != "quit":
        while not_quit == True:
            if response[-1] == "?":
                print("This is the answer form b:" + ans_b)
                print("This is the answer form c:" + answer_c_item)
                not_quit = False
            else:
                print("I'm sorry, I can only answer questions.")
                response = input("what is your question?")
# >>>>>>> check_question


question()
