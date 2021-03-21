import jwt
import datetime

key = "1234"
token = jwt.encode({'email': "user.email", 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                            key,algorithm="HS256")

print(token)
data = jwt.decode(token, key, algorithms=["HS256"])
print(data)