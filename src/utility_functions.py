from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
from datetime import datetime, timedelta, time
import jwt
import uuid

# Global Vars
JWT_REQUEST_EXPIRATION_MINUTES = 1


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


# Generate & Decode to test 
def encode_new_jwt(incoming_payload, incoming_key, incoming_algorithm):
    print('Encoding JWT...')
    return jwt.encode(incoming_payload, incoming_key, incoming_algorithm)


def decode_new_jwt(incoming_jwt, decode_key, decode_algorithm):
    print('Decoding JWT...')
    return jwt.decode(incoming_jwt, decode_key, decode_algorithm)


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