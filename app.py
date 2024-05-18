from flask import Flask, render_template, request
from logging import FileHandler,WARNING
from tensorflow.keras.models import load_model

app = Flask(__name__, template_folder="template", static_folder="static")
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

model = load_model('Verity.h5')

@app.route("/")
def main():
  return render_template('index.html', pred = ' ')

@app.route("/index.html")
def idx():
  return render_template('index.html', pred = ' ')

@app.route("/aboutus.html")
def about():
  return render_template('aboutus.html')

@app.route('/submit', methods=['POST'])
def predict():
    artcl = request.form['text']
    mail = request.form['mail']
    ans_str = (model.predict(artcl, mail))
    ans = int(ans_str)

    if(ans==1):
        return render_template('index.html', pred = 'Entered News Article contains true information')
    else:
        return render_template('index.html', pred = 'Entered News Article contains false information')
    
if __name__ == '__main__':
    app.run(debug = True)
