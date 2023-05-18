import json
import re
import unknown_questions


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")

def get_response(input_string):
    input_string = input_string.lower()
    # split_message = input_string.lower().split(' ')
    split_message=re.split(r'\s+|[,;?!.-]\s*',input_string.lower())
    score_list = []

    # Check all responses
    for response in response_data:
        response_score = 0
        required_score = 0
        necessary_words = response["necessary_words"]

        # Check if there are any necessary words
        if necessary_words:
            # required_score = sum(word in input_string for word in necessary_words)
            # if required_score != len(necessary_words):
            #     continue
            for word in split_message :
                if word in necessary_words :
                    required_score +=1
        # regular expression pattern for the response phrases
        pattern = r'\b(?:{})\b'.format('|'.join(map(re.escape, response["user_input"])))

        # input string matches the pattern using regular expression or not
        # if re.search(pattern, input_string):
        #     response_score += 1
        if required_score == len(necessary_words) :
            for word in split_message :
                if word in response['user_input']:
                    response_score +=1

        # Add score to list
        score_list.append(response_score)

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If it doesn't understand the question or has no answer, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return unknown_questions.random_string()

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))