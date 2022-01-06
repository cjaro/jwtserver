from base64 import b64decode
from datetime import datetime, timedelta, time
import jwt
import logging
import os
import pem
import time
import uuid

# Global Vars
TOKEN_CACHE = {}
JWT_REQUEST_EXPIRATION_MINUTES = 1

# Required ENV_VARS
# CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_ID = '36b08ef1-d37d-4c0e-989f-ade4e5ce9d08'
CERT_PATH = os.getenv('CERT_PATH')
CERT_PASS = os.getenv('CERT_PASS')

# The 'auth server' would essentially need to do the reverse of the existing client:
# - Get the request JWT and extract the parameters
# - Generate a JWT based on the requested service URL, client_id and current time
# - Return a JSON response containing the access_token and expires_in


def mf_time_now(now):
    return now.timestamp()


def gen_expiry(now):
    return (now + timedelta(minutes=JWT_REQUEST_EXPIRATION_MINUTES)).timestamp()


def encode_new_jwt(incoming_payload, incoming_key, incoming_algorithm):
    print("Encoding JWT...")
    return jwt.encode(incoming_payload, incoming_key, incoming_algorithm)


def decode_new_jwt(incoming_jwt, decode_key, decode_algorithm):
    print("Decoding JWT...")
    return jwt.decode(incoming_jwt, decode_key, decode_algorithm)


def generate_new_jwt(decoded_jwt):
    new_client_id = decoded_jwt['client_id']
    new_service_url = decoded_jwt['service_url']
    curr_time = datetime.now().timestamp()
    new_expiry = gen_expiry(curr_time)

    return jwt.encode(
        payload={
            'sub': new_client_id,
            'iat': int(curr_time),
            'jti': str(uuid.uuid4()),
            'client_id': new_service_url,
            'exp': int(new_expiry)
        },
        key='secret',
        algorithm="HS256"
    )


if __name__ == '__main__':
    auth_url = 'https://portal.afw.weather.dev.solidstatescientific.com/adfs/oauth2/token',
    service_url = 'https://test-sandbox.afw.dev.solidstatescientific.com/graphql',
    # fingerprint = 'vxAKeI6ewGAIDTycUXnW3UnPNiE=',
    # headers = {
    #     'x5t': fingerprint,
    #     'typ': 'JWT',
    #     'alg': algorithm
    # }

    now = datetime.now()
    issued_at = mf_time_now(now)
    print('JWT issued', time.strftime('%d %B %Y %H:%M:%S', time.localtime(issued_at)))

    expires_at = gen_expiry(now)
    print('JWT expires', time.strftime('%d %B %Y %H:%M:%S', time.localtime(expires_at)))

    our_payload = {
        'aud': auth_url,
        'sub': CLIENT_ID,
        'iss': CLIENT_ID,
        'iat': int(issued_at),
        'jti': str(uuid.uuid4()),
        'client_id': service_url,
        'exp': int(expires_at)
    }

    key = 'secret'
    # pass in options per here: https://github.com/marcospereirampj/python-keycloak/issues/89
    options = {"verify_signature": True, "verify_aud": False, "exp": True}
    encoded = jwt.encode(
        payload=our_payload,
        key='secret',
        algorithm="HS256")
    print("encoded", encoded)

    decoded = jwt.decode(encoded, key, algorithms="HS256", options=options)
    print("decoded", decoded)

    generate_new_jwt(decoded_jwt=decoded)
