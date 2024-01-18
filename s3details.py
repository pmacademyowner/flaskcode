import logging
import boto3
from botocore.exceptions import ClientError
import os


def s3DownloadUpload(emailId):
    
    file_name = "emaillist.txt"
    object_name = "emaillist.txt"
    bucket = "cloudtrainingdetails9880"
   
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket, object_name, file_name)

    fl = open(object_name, "a")
    fl.write(emailId+"\n")
    fl.close()
    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__": 
    emailId = 'praveen.gunasekar@outlook.com'
    s3DownloadUpload(emailId)
