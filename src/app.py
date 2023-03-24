import json
import os

from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey

from commands import command_handler

DISCORD_PUBLIC_KEY = os.environ["DISCORD_PUBLIC_KEY"]
LOGGING = True


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        signature = event["headers"]["x-signature-ed25519"]
        timestamp = event["headers"]["x-signature-timestamp"]

        verify_key = VerifyKey(bytes.fromhex(DISCORD_PUBLIC_KEY))
        message = timestamp + json.dumps(body, separators=(",", ":"))

        try:
            verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
        except BadSignatureError:
            return {"statusCode": 401, "body": json.dumps("invalid request signature")}

        t = body["type"]
        if t == 1:  # ping
            return {"statusCode": 200, "body": json.dumps({"type": 1})}
        elif t == 2:
            return command_handler(body)
        else:
            return {"statusCode": 400, "body": json.dumps("unhandled request type")}
    except:
        raise
