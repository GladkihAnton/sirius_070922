import jwt

encoded = jwt.encode(
    {
        "user_id": 123
     },
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
)
jwt.decode(
    encoded,
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
)
