import random

# Define the chatbot's responses
greetings = ['Hi there!', 'Hello!', 'Greetings!', 'Nice to meet you!']
intents = {
    'What is your name?': 'I am a chatbot developed by Jamun Tek Tech.',
    'What services do you provide?': 'We develop software and provide training on various technology stacks.',
    'Which programming languages do you teach?': 'We teach several programming languages, including Python, Java, C++, and JavaScript.',
    'How can I contact you?': 'You can reach us at contact@jamuntektech.com for any inquiries.',
    'What courses do you offer?': 'We offer courses in web development, mobile app development, data science, and more.',
    'Can you tell me about your training methodology?': 'Our training approach focuses on a combination of theoretical concepts and hands-on projects to ensure practical learning.',
    'Where are you located?': 'We are located at 123 Main Street, City, Country.',
    'Default': 'I''m sorry, I didn''t understand that. Can you please rephrase your question?'
}

# Function to generate chatbot responses
def get_response(message):
    if message in intents:
        return intents[message]
    else:
        return intents['Default']

# # Function to start the chatbot
# def start_chatbot():
#     print("Chatbot: " + random.choice(greetings))
#     print("Chatbot: How can I assist you today?")
    
#     while True:
#         user_input = input("User: ")
#         if user_input.lower() == 'bye':
#             print("Chatbot: Goodbye! Have a great day!")
#             break
        
#         response = get_response(user_input)
#         print("Chatbot: " + response)

# # Start the chatbot
# start_chatbot()

# Function to handle user input and return chatbot response
def handle_user_input(user_input):
    response = get_response(user_input)
    return response
