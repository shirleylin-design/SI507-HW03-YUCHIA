def question():
    response = input("What is your question?")

# Question_C answer is here:
answer_c_list =["Reply hazy, try again.","Ask  again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

answer_c_item = random.choice(answer_c_list)
print(answer_c_item)
