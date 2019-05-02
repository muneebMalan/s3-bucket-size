import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    total_size = 0

    full_path = event['myfolder']

    if full_path[-1] == '/':
        full_path = full_path[:-1]

    folders_in_path = full_path.split('/')
    print(folders_in_path)

    bucket = folders_in_path[2]
    folder = folders_in_path[-1]

    S3_bucket = s3.list_objects_v2(Bucket=bucket, Prefix=folder)
    content = S3_bucket['Contents']
    for bucket in content:
        size_bytes = bucket['Size']
        total_size += size_bytes

    size_in_megebytes = round(float(total_size) / (1024 * 1024), 2)
    print('The size of ' + folder + ' is ' + str(size_in_megebytes) + 'MB')

    return 'Completed'