from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
debug = DebugToolbarExtension(app)


newStory = Story(["noun", "place", "verb", "adjective"],
    """Once upon a time long ago, there was a {adjective} {noun} that lived in a {place}. It loved to {verb}.""")


@app.route('/')
def home():
    prompts = newStory.prompts
    return render_template("madlib-form.html", prompts=prompts)


@app.route('/madlib-answer')
def answer():
    text = newStory.generate(request.args)
    return render_template("madlib-answer.html", text=text)




