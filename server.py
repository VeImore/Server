"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSLIST = [
    'jiveturkey', 'smelly', 'yo mama', 'deez', 'whack', 'butthead', 'stupid'
    'lame'
]


@app.route('/')
def start_here():
    """Home page."""

    return """
      <!doctype html>
      <html>
        <head>
          <title>Free $100 click here</title>
        </head>
        <body>
          <h1>Hi! This is the home page.</h1>
          <a href = "/hello">Click here to visit the 'hello' page!</a>
        </body>
      </html>
      """

    
@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          </br>
          What compliment would you like to choose?
          </br>
          <input type ="radio" name ="compliment" value = "awesome"> Awesome </br>
          <input type ="radio" name ="compliment" value = "terrific"> Terrific </br>
          <input type ="radio" name ="compliment" value = "fantastic"> Fantastic </br>
          <input type ="radio" name ="compliment" value = "neato" > Neato </br>
          <input type ="radio" name ="compliment" value = "fantabulous" > Fantabulous </br>
          <input type ="radio" name ="compliment" value = "oh-so-not-meh" > Oh-So-Not-Meh</br>
          <input type ="radio" name ="compliment" value = "wonderful"> Wonderful</br>
          <input type ="radio" name ="compliment" value = "wowza"> Wowza</br>
          <input type ="radio" name ="compliment" value = "smashing"> Smashing</br>
          <input type ="radio" name ="compliment" value = "lovely"> Lovely</br>
          </br>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          What's your name to get DISSED? <input type="text" name="person">
          </br>
          <input type="submit" value="Submit">
        </form>
        
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    ## compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def say_diss():
    """Dissing you like it is 1995 """

    player = request.args.get("person")
    diss = choice(DISSLIST)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Big Fat Diss!</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
