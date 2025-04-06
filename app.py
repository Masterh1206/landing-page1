from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contract = request.form['contract']
        signature = request.form['signature']

        os.makedirs('data', exist_ok=True)
        with open('data/signups.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, contract, signature])
        
        return render_template('thank_you.html', name=name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)