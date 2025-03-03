from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/')
def get_data():
    return jsonify({"message": "Get request received successfully !"})

@app.route('/post', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Post request received", "data_received":data})

if __name__ == '__main__':
    app.run(debug=True, port=4000) 
