from flask import Flask
import os

app = Flask(__name__)

zip_dict = {}

with open('zipcode.txt','r') as f:
    for count, line in enumerate(f):
        zip_data = line.strip().split(',')
        zip_dict[zip_data[0]] = zip_data[1:]

@app.route('/<zipcode>/')
def get_coordinate(zipcode):
    return str(zip_dict.get(zipcode,'Zip Not Found'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738)) 
    app.run(host = '0.0.0.0', port=port)