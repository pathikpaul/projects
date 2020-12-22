from common import root_dir, nice_json
from flask import Flask
from flask_cors import CORS
#from werkzeug.exceptions import NotFound
import json
from flask import request
import jwt
import datetime
from flask import abort
SECRET_KEY = 'my_precious'

app = Flask(__name__)
CORS(app)

with open("{}/database/movies.json".format(root_dir()), "r") as f:
    movies = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movies/public/<movieid>", methods=['GET'])
def movie_pbulic_info(movieid):
    if movieid not in movies:
        raise NotFound

    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return nice_json(result)

@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    myHeader=request.headers.get('Authorization')
    if myHeader is None:
        abort(400, "Missign Authorization Token")
    if not myHeader.startswith('Bearer '):
        abort(400, "Missign Bearer Token")
    bearer,_,auth_token = myHeader.partition(' ')
    try:
        payload=decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        abort(400, "Signature expired. Please log in again.")
    except jwt.InvalidTokenError:
        abort(400, "Invalid token. Please log in again.")
    print('payload=',type(payload),payload)
    if movieid not in movies:
        abort(400,"Movie not found in List of Movies")

    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return nice_json(result)

@app.route("/movies/login", methods=['POST'])
def movie_login():
    myinput = request.json
    if myinput is None:
        abort(400, "username and password needs to be provided in json format" )
    if 'username' not in myinput.keys():
        abort(400, "username needs to be provided " )
    if 'password' not in myinput.keys():
        abort(400, "username needs to be provided " )
    if myinput["username"] != "admin" or myinput["password"] != "12345":
        abort(400, "Invalid username or password provided." )
    
    return nice_json({'username':myinput["username"],'jwt':encode_auth_token(myinput["username"])})


@app.route("/movies", methods=['GET'])
def movie_record():
    return nice_json(movies)

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload
    except:
        print ('invalid token')
        raise

def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(port=5001, host= '0.0.0.0' ,debug=True)

