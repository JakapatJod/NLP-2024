import random

name = "Bot"
weather = "cloudy"

responses = {
    'statement': [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way?',
        'I find that extremely interesting',
        'can you back that up?', 'oh wow!',
        ':)'
    ],
    'question': [
        "I don't know :(",
        'you tell me!'
    ],
    "default": ["default message"]
}

def send_message(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message


def respond(message):
    # Check for a question mark
    if '?' in message:
        # Return a random question response
        return random.choice(responses['question'])
    # Return a random statement response
    return random.choice(responses['statement'])

# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")
# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")

while True:
    messages = input('USER: ')
    if messages.lower() == 'bye':
        print('BOT: Good BYE !')
        break

    print('BOT:', send_message(messages))
