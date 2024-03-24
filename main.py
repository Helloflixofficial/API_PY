
import requests
from flask import Flask, jsonify, request,render_template
from flask_restful import Resource, Api
from flask import send_from_directory
app = Flask(__name__)
api = Api(app)

# favicon icon sire
@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsof.icon')


@app.route("/")
def index():
	return render_template("index.html")

# Fetch data from a given URL
def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json() # use extension sir
    else:
        return {'error': 'Failed to fetch data'}

# Welcome message for the home page
@app.route('/home', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API!'})


# Endpoint to get recent releases
@app.route('/recent-release', methods=['GET'])
def recent_release():
    url = 'https://webdis-7ies.onrender.com/recent-release'
    data = fetch_data_from_url(url)
    return jsonify(data)

# Endpoint to get popular data
@app.route('/popular', methods=['GET'])
def get_popular():
    url = 'https://webdis-7ies.onrender.com/popular'
    data = fetch_data_from_url(url)
    return jsonify(data)

# Endpoint to get top airing data
@app.route('/top-airing', methods=['GET'])
def top_airing():
    url = 'https://webdis-7ies.onrender.com/top-airing'
    data = fetch_data_from_url(url)
    return jsonify(data)



# Class-based resource for calculating square
class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2})

# Class-based resource for managing requirements file
class RQ(Resource):
    def get(self):
        rq = {}
        with open('requirements.txt', 'r') as f:
            for i, r in enumerate(f.readlines()):
                rq[f'{i}'] = r.strip()
        return jsonify(rq)

    def post(self):
        data = request.get_json()['Name']
        rq = {}
        with open('requirements.txt', '+a') as f:
            f.write(f'\n{data}')
            f.seek(0)
            for i, r in enumerate(f.readlines()):
                rq[f'{i}'] = r.strip()
        response = jsonify(rq)
        response.status_code = 200
        return response

if __name__ == '__main__':
    app.run(debug=True)
