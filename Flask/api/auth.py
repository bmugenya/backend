import jwt
import datetime

# Secret key for JWT encoding and decoding
SECRET_KEY = 'your_secret_key_here'

def create_auth_token(user_id, expiration_hours=1):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=expiration_hours)

    payload = {
        'user_id': user_id,
        'exp': expiration
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def destroy_auth_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        return True
    except jwt.InvalidTokenError:
        return False
