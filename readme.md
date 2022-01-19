# JWT Receptor & Generator

We are using [PyJWT](https://pyjwt.readthedocs.io/en/stable/usage.html) for JWT generation, encoding, decoding, and handling. We send request JWT to SSSC's ADFS server.


## Breakdown of JWT:

Can be done visually on -> [jwt.io](https://jwt.io/#debugger-io).

**Header:**
```
{
  'x5t': 'vxAKeI6ewGAIDTycUXnW3UnPNiE=',
  'typ': 'JWT',
  'alg': 'RS256'
}
```
- **x5t**: is a base64 encoded fingerprint of the client's certificate
- **typ**: The type of token
- **alg**: The encryption algorithm used

**Body:**
```{
  'aud': 'https://portal.afw.weather.dev.solidstatescientific.com/adfs/oauth2/token',
  'sub': '36b08ef1-d37d-4c0e-989f-ade4e5ce9d08',
  'iss': '36b08ef1-d37d-4c0e-989f-ade4e5ce9d08',
  'iat': 1637611163,
  'jti': '09ffb6fa-9ece-42c2-bd4c-efd61da7e626',
  'client_id': 'https://test-sandbox.afw.dev.solidstatescientific.com/graphql',
  'exp': 1637611223
}
```
- **aud**: Audience
- **sub**: Subject
- **iss**: Issuer
- **iat**: Token generation time in seconds since epoch
- **jti**: Random uuid
- **client_id**: The service you want a token for
- **exp**: Token expiration time in seconds since epoch

### Run this project

