from flask import Flask, render_template

app = Flask(__name__)

# Simulates a DB call
posts = [
    {
        'author': 'Jon Hourany',
        'title': 'How to create Flask Apps!',
        'content': "You won't believe how easy it is!",
        'date_posted': 'September 5, 2018'
    },
    {
        'author': 'George G',
        'title': "Switching to Android -- Breaking Apple's Chains",
        'content': "I have freed myself from my overlords!",
        'date_posted': 'September 3, 2018'
    }
]

# routing multiple endpoints to a single function
@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)