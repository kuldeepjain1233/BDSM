import random


def random_string():
    random_list = [
        "I'm sorry, I didn't quite understand your question. Could you please provide more details or perhaps try 'help bot'?",
        "Can you please rephrase your question or perhaps try 'help bot'?",
        "I'm sorry, I'm not familiar with that specific question. Is there anything else I can assist you with or perhaps try 'help bot'?",
        "I apologize, but I'm unable to provide a response to your question at the moment,Maybe try using 'help bot'."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
