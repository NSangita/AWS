import boto
iam = boto.connect_iam()

# Now create a user and place him in the Amazing group.

'''with open(createUser.txt) as f:
    content = f.readlines()'''

lines = [line.rstrip('\n') for line in open('createUser.txt')]


for u in lines:
    response = iam.create_user(u)
    user = response.user
    response = iam.add_user_to_group('Amazing', u)
    
for u in lines:
    response = iam.create_access_key(u)
    access_key = response.access_key_id
    secret_key = response.secret_access_key




