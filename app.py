from flask import Flask, render_template, request
import pyttsx3
import speech_recognition as sr
import nltk

app = Flask(__name__)

# Sample product database (replace it with your actual product database)
product_database = ["item1", "item2", "item3"]

def get_total_amount(items):
    # Replace this with your logic to calculate the total amount
    return 100  # Sample total amount

def voice_prompts(total_amount):
    engine = pyttsx3.init()
    engine.say("Please confirm your order:")
    engine.say("Total amount: {}".format(total_amount))
    engine.runAndWait()

def process_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your order:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def extract_order_details(text):
    tokens = nltk.word_tokenize(text)
    item_names = [token for token in tokens if token in product_database]
    quantities = [int(token) for token in tokens if token.isdigit()]
    return item_names, quantities

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm_order', methods=['POST'])
def confirm_order():
    order_text = process_speech()
    item_names, quantities = extract_order_details(order_text)
    total_amount = get_total_amount(item_names)  # You may want to improve this logic
    voice_prompts(total_amount)
    return render_template('confirmation.html', item_names=item_names, quantities=quantities, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)
