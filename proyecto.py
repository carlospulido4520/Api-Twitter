from flask import Flask
from flask import render_template, request
import tweepy
import jinja2

auth = tweepy.OAuthHandler("uR4Ui0UsqXb7CB9eLVdUxbeoq", "rEmOHqxHM5KT0J5fSyxCehLQq96ASwZaU2I0mZNeGTmxzrJPDf")
auth.set_access_token("1181947712381620224-KXAWgek7nOmKtM5GK0iyZmXh6Y67Cl", "DXTqrHgWzVShLHIeo7wZfmCeFJiwFT8c3E7jttP7vZlnS")

api = tweepy.API(auth)
app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def hello():

    user = request.args.get('usuario')
    userContent = api.get_user(user)
    followers = userContent.followers_count
    name = userContent.name
    foto = userContent.profile_image_url_https
    print (userContent)
    return render_template('index.html', followers = followers, user = user, name=name, foto=foto)

if __name__ == "__main__":
    app.run(debug=True)