## https://realpython.com/token-based-authentication-with-flask/
##  pip3 install pyjwt
##     Successfully installed pyjwt-1.7.1
##     Successfully installed cffi-1.14.4 cryptography-3.2.1 jwt-1.1.0 pycparser-2.20 six-1.15.0
import datetime
import time
import jwt
SECRET_KEY = 'my_precious'
def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

token=encode_auth_token("pathikpaul")
print(token)
print(token.decode())
print("validate using https://devtoolzone.com/decoder/jwt ")

time.sleep(6)

payload=decode_auth_token(token)
print("payload=",payload)
