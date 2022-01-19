# JWT Receptor & Generator

We are using [PyJWT](https://pyjwt.readthedocs.io/en/stable/usage.html) for JWT generation, encoding, decoding, and handling.

This is a request JWT that we send to SSSC's ADFS server
`eyJ4NXQiOiJ2eEFLZUk2ZXdHQUlEVHljVVhuVzNVblBOaUU9IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJodHRwczovL3BvcnRhbC5hZncud 2VhdGhlci5kZXYuc29saWRzdGF0ZXNjaWVudGlmaWMuY29tL2FkZnMvb2F1dGgyL3Rva2VuIiwic3ViIjoiMzZiMDhlZjEtZDM3ZC00YzBlLTk4OWYtYWRlNGU1Y2U5ZDA4IiwiaXNzIjoiMzZiMDhlZjEtZDM3ZC00YzBlLTk4OWYtYWRlNGU1Y2U5ZDA4IiwiaWF0IjoxNjM3NjExMTYzLCJqdGkiOiIwOWZmYjZmYS05ZWNlLTQyYzItYmQ0Yy1lZmQ2MWRhN2U2MjYiLCJjbGllbnRfaWQiOiJodHRwczovL3Rlc3Qtc2FuZGJveC5hZncuZGV2LnNvbGlkc3RhdGVzY2llbnRpZmljLmNvbS9ncmFwaHFsIiwiZXhwIjoxNjM3NjExMjIzfQ.hn44Cy-3wOSW6LFIaYu8hM4dDc_AsNC1V1_dPuWAC9mgmeEOnNTLCO15J12nMTomxTn6L3tTxKBPtXJ8uQ7Llt_yf8TmwGykVSgshCBR-_tnD5pgmJqzMUPAYCjoUilFuTut6pO9FSK9MgJRX-_UiEmvyftMFkDcix9nEM8WSQGKXWN2BM52pIux7y5GhMyBb9oPCjKGoH0hYKzTfdYP_NQjogpz3gA_r7he8kjhqteDcOX_sWzT3TbfHbbaCagyPLW1ABzE1-kkbCM0A-G7h0mGWOVjZewbZq1XllFS2ZThET9CBxZvy0EwknoSWIV-wnmCHo8lwz-e22qW0QbU0g`

## Breakdown of JWT:

Can be done on -> [jwt.io](https://jwt.io/#debugger-io).

Header:
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

Body:
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
