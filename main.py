from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

def request_data() :
  blog_url = 'https://api.npoint.io/0543494d63afb91b8aa0'
  resp = requests.get(blog_url)
  resp.raise_for_status()
  all_posts = resp.json()['posts']
  return all_posts
  
@app.route('/samplepost')
def samplepost() :
  return render_template('sample_post.html')
  
@app.route('/about')
def about() :
  return render_template('about.html')

@app.route('/contact')
def contact() :
  return render_template('contact.html')  
  
@app.route('/')
def home () :
  all_posts = request_data()
  return render_template('index.html', data = all_posts)

@app.route('/post')
def post() :
  all_posts = request_data()
  url_params = request.args
  _id       = url_params.get('id', None)
  article   = [ p for p in all_posts if p['id'] == int(_id) ] if _id is not None else all_posts
  return render_template('post.html', data = article)

  
if __name__ == "__main__":
  app.run( debug=True, host='0.0.0.0', port = 2000 )