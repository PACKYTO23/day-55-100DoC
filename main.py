from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def style_function():
        return "<b>" + function() + "</b>"
    return style_function


def make_emphasis(function):
    def style_function():
        return "<em>" + function() + "</em>"
    return style_function


def make_underlined(function):
    def style_function():
        return "<u>" + function() + "</u>"
    return style_function


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img src='https://thumbs.dreamstime.com/b/cartoon-alarm-clock-28115617.jpg' width=600>")


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there, {name}! Soon you'll have {number} million in the bank!"


if __name__ == "__main__":
    app.run(debug=True)
