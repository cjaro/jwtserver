
def generate_request_jwt(auth_url, service_url, fingerprint, pfx, algorithm="RS256"):
    ''' Generate a signed request JWT '''
    headers = {
        "x5t": fingerprint,
        "typ": "JWT",
        "alg": algorithm
    }
    now = datetime.now()
    issued_at = now.timestamp()
    expires_at = (now + timedelta(minutes=JWT_REQUEST_EXPIRATION_MINUTES)).timestamp()
    payload = {
        "aud": auth_url,
        "sub": CLIENT_ID,
        "iss": CLIENT_ID,
        "iat": int(issued_at),
        "jti": str(uuid.uuid4()),
        "client_id": service_url,
        "exp": int(expires_at)
    }
    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pfx.get_privatekey())
    encoded_jwt = jwt.encode(payload=payload, headers=headers, key=key, algorithm=algorithm)
    return encoded_jwt


def recieve_and_decode_jwt(incoming_jwt, algorithm="RS256"):
    ''' Recieve, decode, and generate new JWT '''
    decoded_incoming = jwt.decode(incoming_jwt)
