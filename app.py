from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os

app = Flask(__name__)

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add an expense
@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form['date']
    category = request.form['category']
    description = request.form['description']
    amount = request.form['amount']

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    return redirect(url_for('index'))

# Route to view all expenses

@app.route('/expenses')
def view_expenses():
    expenses = []
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            expenses = list(reader)
    return jsonify(expenses)


if __name__ == '__main__':
    app.run(debug=True)
