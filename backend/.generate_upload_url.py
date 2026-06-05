import json
import boto3
import uuid
import random
import string
from datetime import datetime

# AWS Clients
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# Constants
BUCKET_NAME = "filesharing-thisside"
UPLOAD_FOLDER = "uploads/"
TABLE_NAME = "FileMappings"

# DynamoDB Table
table = dynamodb.Table(TABLE_NAME)


def generate_short_code(length=6):
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )


def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event.get("body", "{}"))

        filename = body.get("filename")
        content_type = body.get(
            "contentType",
            "application/octet-stream"
        )

        if not filename:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {"error": "Missing 'filename' in request body"}
                ),
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            }

        # Generate unique S3 file key
        unique_id = str(uuid.uuid4().hex)
        file_key = f"{UPLOAD_FOLDER}{unique_id}_{filename}"

        # Generate short code
        short_code = generate_short_code()

        # Save mapping in DynamoDB
        table.put_item(
            Item={
                "shortCode": short_code,
                "fileKey": file_key,
                "createdAt": datetime.utcnow().isoformat()
            }
        )

        # Generate pre-signed upload URL
        presigned_url = s3_client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": BUCKET_NAME,
                "Key": file_key,
                "ContentType": content_type
            },
            ExpiresIn=600
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "uploadUrl": presigned_url,
                "fileKey": file_key,
                "shortCode": short_code
            }),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
