import boto3
s3=boto3.client("s3",region_name="ap-south-1")

bucket_name="s3-bucket-transfer-acceleration-lab-2026"
response=s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint":"ap-south-1"
    }
)
print("Bucket Created Successfully!")
print(response)