import boto3
s3 = boto3.client("s3", region_name="ap-south-1")

bucket_name = "s3-bucket-transfer-acceleration-lab-2026"
s3.put_bucket_accelerate_configuration(
    Bucket=bucket_name,
    AccelerateConfiguration={
        "Status": "Enabled"
    }
)
print("S3 Transfer Acceleration enabled successfully!")
response = s3.get_bucket_accelerate_configuration(
    Bucket=bucket_name
)

print("Transfer Acceleration Status:", response["Status"])

accelerated_endpoint = (
    f"https://{bucket_name}.s3-accelerate.amazonaws.com"
)

print("Accelerated Endpoint:", accelerated_endpoint)