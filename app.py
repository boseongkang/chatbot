from decouple import config
from flask import Flask

token = config('TELEGRAM_TOKEN')
app = Flask(__name__)

@app.route('/')
def index():
    return 'chatbot!'

if __name__ == '__main__':
    app.run(debug=True)
