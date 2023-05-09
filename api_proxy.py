from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with the external API URL you want to forward requests to
external_api_url = 'https://api.upcitemdb.com/prod/trial/lookup'

@app.route('/', methods=['GET', 'POST'])
def proxy():
    if request.method == 'GET':
        # Forward the GET request to the external API
        response = requests.get(external_api_url, params=request.args)
    elif request.method == 'POST':
        # Forward the POST request as a GET request to the external API
        post_data = request.json if request.is_json else request.form.to_dict()
        response = requests.get(external_api_url, params=post_data)

    # Return the response from the external API
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)