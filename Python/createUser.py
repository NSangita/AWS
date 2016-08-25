import boto
iam = boto.connect_iam()

# Now create a user and place him in the Amazing group.

response = iam.create_user('env_dev_admin')
user = response.user
response = iam.add_user_to_group('Amazing', 'env_dev_admin')


# Create AccessKey/SecretKey pair for env_dev_admin

response = iam.create_access_key('env_dev_admin')
access_key = response.access_key_id
secret_key = response.secret_access_key
