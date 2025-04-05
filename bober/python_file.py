import datetime
import time

import jwt

secret = "adfsgrhsatrjjjjjjjjjjjjjjjjjjjjjj"
unsecret = 'aefwaffzvbfesuhgrshd bssssssbeshrfddgffffgfdrrjdrrrrrrrrrrrrrrrrrrrrrrrrrrrr bbsdbdrbbb drh shrt '

payload = {
    "my_name": "Lev",
    "age": 12,
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=500),
    "my_city": "Odessa"
}

encode_jwt = jwt.encode(payload=unsecret, key=secret, algorithm="HS256")
print(encode_jwt)
time.sleep(15)

decoded = jwt.decode(
    encode_jwt,
    unsecret,
    algorithms=["HS256"],
#    options={
#        'verify_signature': False
#    }
)
print(decoded)