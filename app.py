from flask import Flask, render_template, url_for, request, redirect
from mail import sendMessage, sendMessageSelf

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/unfinished', methods=['GET'])
def unfinished():
    return render_template('unfinished.html')

@app.route('/wp-admin', methods=['GET'])
def troll():
    return render_template('troll.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name'].strip()
    email = request.form['email'].strip()
    phone = request.form['phone'].strip()
    message = request.form['message'].strip()
    if not (name or email or phone or message):
        return render_template('error.html', message="Please fill up all fields")
    if not sendMessage(name, email, message):
        return render_template('error.html', message="Please enter valid email address")
    if not sendMessageSelf(name, email, phone, message):
        return render_template('error.html', message="Please enter valid email address")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")