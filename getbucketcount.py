def get_bucket_count():
    
    try:
        s3 = boto3.resource('s3')
    except NoCredentialsError:
        print("@InvalidCredentials")
        sys.exit()

    try:
        no_of_buckets = len(list(s3.buckets.all()))
        print("You have", str(no_of_buckets), "Amazon S3 buckets.")
        return no_of_buckets

    except ClientError as ex:
        print(ex)
        return 0


if __name__ == '__main__':
    get_bucket_count()
