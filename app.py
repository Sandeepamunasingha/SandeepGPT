from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    bot_response = ""
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['user_input']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        bot_response = response['choices'][0]['message']['content']

    return render_template('chat.html', user_input=user_input, bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
