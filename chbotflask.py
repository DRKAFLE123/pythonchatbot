from flask import Flask, request,render_template
from chbot import handle_user_input

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chbot.html')


# Route to handle user input and return chatbot response
@app.route('/get-response', methods=['GET'])
def get_chatbot_response():
    user_input = request.args.get('user_input')
    response = handle_user_input(user_input)  # Call the function to get chatbot response
    return response

# Run the Flask server
if __name__ == '__main__':
    app.run()
