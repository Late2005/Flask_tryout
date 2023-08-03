from flask import Flask

app=Flask(__name__)
#Add code below

@app.route('/')
def home():
    return "<p>Welkom op onze nieuwe website! <u>Powered by Flask</u></p>"

#Add code above
if __name__ == '__main__':
    app.run(port=5000, debug=True)
