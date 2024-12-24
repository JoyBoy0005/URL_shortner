import random
import string
from flask import Flask, request, render_template, redirect
#author = Prince Patel
app = Flask(__name__)


shortened_urls = {}

def generate_short_url(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    long_url = None
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if not long_url:
            return "Error: Please provide a valid URL", 400
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()
        shortened_urls[short_url] = long_url
    return render_template('index.html', short_url=short_url, long_url=long_url)


@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    return "Error: Short URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
