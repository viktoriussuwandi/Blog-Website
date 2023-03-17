from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)
data = {}

def request_data() :
  blog_url = 'https://api.npoint.io/0543494d63afb91b8aa0'; resp = requests.get(blog_url); resp.raise_for_status(); all_posts = resp.json()['posts']
  return all_posts

@app.route('/samplepost')
def samplepost() :
  data = { 'bm_img'  : 'static/img/sample_post-bg.jpg', 'txt_heading' : 'Man must explore, and this is exploration at its greatest',
    'txt_subheading' : 'Problems look mighty small from 150 miles up', 'posts' : None }
  return render_template('sample_post.html', data = data)

@app.route('/')
def home () :
  data = { 'bm_img' : 'static/img/home-bg.jpg', 'txt_heading' : 'My Web Blog', 'txt_subheading' : 'Wellcome To My Home Blog', 'posts' : request_data() }
  return render_template('index.html', data = data )
  
@app.route('/about')
def about() :
  data = { 'bm_img' : 'static/img/about-bg.jpg', 'txt_heading' : 'About Me', 'txt_subheading' : 'This is what I do.','posts' : None }
  return render_template('about.html', data = data)

@app.route('/post')
def post() :
  url_params = request.args
  _id        = url_params.get('id', None)
  data = { 'bm_img' : 'static/img/home-bg.jpg', 'posts' : [ p for p in request_data() if p['id'] == int(_id) ] if _id is not None else request_data() }
  return render_template('post.html', data = data)

@app.route('/contact')
def contact() :
  data = { 'bm_img' : 'static/img/contact-bg.jpg', 'txt_heading' : 'Contact Me', 'txt_subheading' : 'Have questions? I have answers.', 'posts' : None }
  return render_template('contact.html', data = data)

@app.route('/form-entry', methods = ['GET','POST'])
def receive_data() :
  if request.method == 'POST' :
    data = {'username' : request.form['username'], 'email' : request.form['email'], 
            'phone'    : request.form['phone'],    'message' : request.form['message']    
    }
    print(data)
    return '<h1> Successfully sent your message </h1>'
  else : return render_template('contact.html')

if __name__ == "__main__":
  app.run( debug=True, host='0.0.0.0', port = 2000 )