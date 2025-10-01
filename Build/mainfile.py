from flask import Flask
import requests

app = Flask(__name__) #tells flask that the application's main code in located in the current file.

@app.route("/<username>",methods=['GET'])
def get_user(username):
    url = f"https://api.github.com/users/{username}/gists"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return (response.json())

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return f"User '{username}' not found", 404
        else:
            return f"HTTP Error: {e}", e.response.status_code

if __name__== "__main__":
    app.run(host='0.0.0.0')
