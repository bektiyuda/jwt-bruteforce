import jwt

secret = ""
payload = {
    "user": "hacker",
    "role": "user"
}

token = jwt.encode(payload, secret, algorithm="HS256")

print("Generated JWT:")
print(token)