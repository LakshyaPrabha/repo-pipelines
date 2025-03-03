from flask import Flask, jsonify
import requests

app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/fetch', methods=['GET'])

def fetch_data():
    url="https://www.flipkart.com/mobile-phones-store"

    response=requests.get(url)
    return jsonify({
        "Status": response.status_code,
        "data": response.text
    })
if __name__ == '__main__':
    app.run(debug=True, port=9001)#updated getdata.py with new logic 
