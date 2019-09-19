import random

def question():
    response = input("What is your question?")

# B - pick a random answer
ans_list_b = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]

ans_b = random.choice(ans_list_b)
print(ans_b)
