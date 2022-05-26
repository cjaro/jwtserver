from base64 import b64decode
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask
from utility_functions import private_key, public_key, generate_new_jwt

import jwt
import logging
import os
import uuid


# Global Vars
JWT_REQUEST_EXPIRATION_MINUTES = 1

load_dotenv()
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
app = Flask(__name__)
logger = logging.getLogger(__name__)

# - Get the request JWT and extract the parameters
# - Generate a JWT based on the requested service URL, client_id and current time
# - Return a JSON response containing the access_token and expires_in

key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=2048
)

private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption()
)

public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH,
    crypto_serialization.PublicFormat.OpenSSH
)


def generate_new_jwt(decoded_jwt, expiration):
    new_client_id = decoded_jwt['client_id']
    new_service_url = decoded_jwt['service_url']
    curr_time = datetime.now().timestamp()
    new_expiry = (curr_time + timedelta(minutes=expiration)).timestamp()

    return jwt.encode(
        payload={
            'sub': new_client_id,
            'iat': int(curr_time),
            'jti': str(uuid.uuid4()),
            'client_id': new_service_url,
            'exp': int(new_expiry)
        },
        key=private_key,
        algorithm='RS256'
    )


if __name__ == '__main__':
    now = datetime.now()
    print(now)
    issued_at = now.timestamp()
    req_exp = os.getenv('JWT_REQUEST_EXPIRATION_MINUTES')
    expires_at = (now + timedelta(minutes=req_exp)).timestamp()

    payload_claims = os.getenv('CLAIMS')
    logger.info(f'Claims:\n {payload_claims}')

    # pass options per https://github.com/marcospereirampj/python-keycloak/issues/89
    options = {'verify_signature': True, 'verify_aud': False, 'exp': True}
    encoded = jwt.encode(
        payload=payload_claims,
        key=private_key,
        algorithm='RS256')
    logger.info(f'encoded: {encoded}')

    decoded = jwt.decode(encoded, public_key, algorithms='RS256', options=options)
    logger.info(f'decoded: {decoded}')

    try:
      generate_new_jwt(decoded_jwt=decoded, expiration=req_exp)
    except Exception as e:
      logger.info(e)
      logger.error(e, exc_info=1)
