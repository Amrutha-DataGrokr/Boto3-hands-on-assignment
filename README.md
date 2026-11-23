# Boto3 S3 Hands-on Assignment

This project demonstrates two basic Amazon S3 operations using Python and Boto3:

- Create an S3 bucket in the `ap-south-1` region.
- Enable S3 Transfer Acceleration for the bucket and display its accelerated endpoint.

## Prerequisites

- Python 3
- Boto3 installed
- AWS credentials configured locally
- Permission to create S3 buckets and change bucket configuration

Install Boto3:

```bash
pip install boto3
```

## Usage

Run the scripts in this order:

```bash
python create_bucket.py
python enable_transfer_acceleration.py
```

The scripts use the bucket name `s3-bucket-transfer-acceleration-lab-2026`. The bucket name must be globally unique, so update `bucket_name` in both scripts if the default name is unavailable.
