from flask import Flask
import random

app = Flask(__name__)

found_me_pic_url = 'https://media0.giphy.com/media/f3qJsJ6C3F1X51OwsQ/giphy.gif?cid=ecf05e47izxi8e2917eum2v19hrsmju6tuxzxpaqfwcxan1p&rid=giphy.gif&ct=g'
num_pic_url = 'https://media2.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif?cid=ecf05e4769pg85hjra1sbnrjwnju4qh37n368oy7b48xnjsc&rid=giphy.gif&ct=g'
too_high_pic_url = 'https://media1.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif?cid=ecf05e476fmphnhvtskjmbggmsla2yxrsznwrdmdc1sglmwu&rid=giphy.gif&ct=g'
too_low_pic_url = 'https://media1.giphy.com/media/fnlXXGImVWB0RYWWQj/giphy.gif?cid=ecf05e476fmphnhvtskjmbggmsla2yxrsznwrdmdc1sglmwu&rid=giphy.gif&ct=g'


@app.route('/')
def index_page():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<img src={num_pic_url}>"


number = random.randint(0, 9)


@app.route('/<int:guessed_number>')
def feedback(guessed_number):
    if guessed_number > number:
        return f"<h1 style='color:red;'>Too high! Try again.</h1>" \
           f"<img src={too_high_pic_url}>"
    elif guessed_number < number:
        return f"<h1 style='color:blue;'>Too low! Try again.</h1>" \
           f"<img src={too_low_pic_url}>"
    else:
        return f"<h1 style='color:green;'>You found me!</h1>" \
               f"<img src={found_me_pic_url}>"


if __name__ == '__main__':
    app.run(debug=True)
