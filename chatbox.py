import re
import random as ran
import respuestas

def get_user_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = verify_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    message_percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(message_percentage * 100)
    else:
        return 0

def verify_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response(respuestas.response1, respuestas.question1, required_words=['estudias'])
        response(respuestas.response2, respuestas.question2, single_response=True)
        response(respuestas.response3, respuestas.question3, single_response=True)
        response(respuestas.response4, respuestas.question4,required_words=['horario'])
        response(respuestas.response5, respuestas.question5 ,required_words=['numero'])

        response(respuestas.response6, respuestas.question6, required_words=['correo'])
        response(respuestas.response7, respuestas.question7 ,required_words=['precio'])
        response(respuestas.response8, respuestas.question8 ,required_words=['edificios'])
        response(respuestas.response9, respuestas.question9 ,required_words=['plataforma'])
        response(respuestas.response10, respuestas.question10, required_words=['años'])



        best_match = max(highest_prob, key=highest_prob.get)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response_default = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][ran.randrange(3)]
    return response_default

while True:
    print("Bot Izune 👩‍🏭" + get_user_response(input('Yo: ')))