import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get credentials and config
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# File to upload
FILE_PATH = "grafana/dashboards/nexaplay-dashboard.json"
S3_KEY = "dashboards/nexaplay-dashboard.json"

def upload_to_s3():
    try:
        # Create S3 client
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        # Upload file
        s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)

        print("✅ Dashboard uploaded successfully to S3!")

    except Exception as e:
        print("❌ Error uploading to S3:")
        print(e)

if __name__ == "__main__":
    upload_to_s3()