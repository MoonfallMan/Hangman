from flask import Flask, jsonify
import os,json

app = Flask(__name__)

with open('words.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def home():
    #return jsonify({"message": "Hello1, World!"})
    return data

if __name__ == '__main__':
    app.run(debug=False)
