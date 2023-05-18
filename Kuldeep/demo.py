import re
import long_responses as long
# import brain_cancer
import breast_cancer
import stock_m



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    # highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    # def response(bot_response, list_of_words, single_response=False, required_words=[]):
        # nonlocal highest_prob_list
        # highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    # Responses -------------------------------------------------------------------------------------------------------
    # response('Hello! I am a bot that provides various prediction analaysis like: Movie Recommendation, Stock Prediction, Music Recommendation, Book Recommendation, breast Cancer Prediction, Malaria Detection, Brain cancer Prediction. Please Choose from the above options: ', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    # response(movie_recommendation, ['movie', 'film','picture'], single_response=True)
    # response(breast_cancer.b_cancer(), ['breast'], required_words=['how'],single_response=True)
    # response('why', ['breast'], single_response=True)
    # response(bot_response, list_of_words)
    # response(brain_cancer_pred, ['brain'], single_response=True)
    # response(stock_m.stock(), ['stock', 'market', 'exchange'], single_response=True)

    # Longer responses
    # response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    # response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    # best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    # return long.unknown() if highest_prob_list[best_match] < 1 else best_match

    # print(message)
    if 'hello' or 'hi' or 'hey' or 'sup' or 'heyo' in message:
        print('Hello! I am a bot that provides various prediction analaysis like: Movie Recommendation, Stock Prediction, Music Recommendation, Book Recommendation, breast Cancer Prediction, Malaria Detection, Brain cancer Prediction. Please Choose from the above options:')
    elif 'movie' or 'film' or 'picture' in message:
        print('MOVIE')
    elif 'breast' in message:
        breast_cancer.b_cancer()
    elif 'stock' or 'market' or 'exchange' in message:
        stock_m.stock()
    elif ('hello' or 'hi' or 'hey' or 'sup' or 'heyo') and ('movie' or 'film' or 'picture') and 'breast' and ('stock' or 'market' or 'exchange') in message:
        print('TOO MANY INSTRUCTIONS')

# Used to get the response
# def get_response(user_input):
    # split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    # response = check_all_messages(split_message)
    # return response


# Testing the response system
while True:
    a=str(input('You: '))
    # print('Bot: ' + get_response(a))
    print('Bot: ' + check_all_messages(a))