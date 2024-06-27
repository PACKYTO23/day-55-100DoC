from flask import Flask
import random

app = Flask(__name__)


r_num = random.randint(0, 9)
print(r_num)


@app.route("/")
def play_game():
    return (f"<h1>Guess a number between 0 and 9</h1>"
            f"<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmlmdHk2OWJkNHh2cHk1cnpjNjg2MzY5ZWRpNTJpOWpnbHF1"
            f"c3o0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPwoeGErMmaI43S/giphy.gif' width=400> ")


@app.route("/<int:number>")
def guess_number(number):
    if number < r_num:
        return "<h1 style='color: red'>The number is too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > r_num:
        return "<h1 style='color: purple'>The number is too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found the random number!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
