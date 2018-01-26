from flask import Flask
from random import choice
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    movietom = get_random_movie()
    if movietom == movie:
        movietom = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    
    content = "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + movietom + "</li>"
    content += "</ul>"


    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movielist = ["The Matrix", "Willow", "Blade", "Transformers", "Frankenstein", "Wall-E", "Snow White"]
    # TODO: randomly choose one of the movies, and return it
    randmovie = random.choice(movielist)
    return randmovie


app.run(host='0.0.0.0')
