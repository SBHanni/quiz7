from flask import Flask
app = Flask(__name__)

def howzit_brah():
    return 'Howzit Brah!'
app.add_url_rule('/', 'howzit', howzit_brah)

if __name__ == '__main__':
    app.run(debug=True)