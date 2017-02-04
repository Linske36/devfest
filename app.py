from flask import Flask, render_template
import json
import requests
import urllib
import urllib2
import sys

app = Flask(__name__)

@app.route("/")
def hello():
   return render_template("hello.html")


@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/account")
def account_create():
    print("enters ac")
    customerId = "5895232b1756fc834d9046d5"
    apiKey = "089b208ea502bf77203c62728b0fab72"
#"6e48088d53bcf91c2a2aee659e458d82"
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
    payload = {
      "type": "Savings",
      "nickname": "test",
      "rewards": 10000,
      "balance": 10000, 
    }
    # Create a Savings Account
    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
        )

    if response.status_code == 201:
        return "account created"
    
    


def main():
    try:
        account_create()
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))




if __name__ == "__main__":
    app.run(host="0.0.0.0")
