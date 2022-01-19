from base64 import b64decode
from datetime import datetime, timedelta
from flask import Flask
from utility_functions import private_key, public_key, generate_new_jwt
import jwt
import logging
import os

dotenv
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
app = Flask(__name__)
logger = logging.getLogger(__name__)


# - Get the request JWT and extract the parameters
# - Generate a JWT based on the requested service URL, client_id and current time
# - Return a JSON response containing the access_token and expires_in

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
