import json
import boto3
import uuid

# Initialize S3 client outside handler for reuse
s3_client = boto3.client("s3")

# Hardcoded bucket name (you can also use environment variables)
BUCKET_NAME = "filesharing-thisside"  # your actual bucket name
UPLOAD_FOLDER = "uploads/"  # folder inside the bucket

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event.get("body", "{}"))
        filename = body.get("filename")
        content_type = body.get("contentType", "application/octet-stream")

        if not filename:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'filename' in request body"}),
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            }

        # Generate a unique file key
        unique_id = str(uuid.uuid4().hex)
        file_key = f"{UPLOAD_FOLDER}{unique_id}_{filename}"

        # Generate pre-signed URL (PUT method)
        presigned_url = s3_client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": BUCKET_NAME,
                "Key": file_key,
                "ContentType": content_type
            },
            ExpiresIn=600  # 10 minutes expiry
        )

        # Return URL and fileKey
        return {
            "statusCode": 200,
            "body": json.dumps({
                "uploadUrl": presigned_url,
                "fileKey": file_key
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


