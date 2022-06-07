
from importlib.util import resolve_name
from pydoc import cli
from urllib import response
import boto3
import os

from pkg_resources import FileMetadata
client = boto3.client('s3',
            aws_access_key_id="",
            aws_secret_access_key="",
            region_name='us-east-1')

#creation of s3 bucket
'''
response = client.create_bucket(
    Bucket='aws-s3-chpr',
   
)
print(response)
'''


#upload a file into s3 bucket

'''
response = client.put_object(
    Body = open("index.html","r").read(),
    Bucket='aws-s3-chpr',
    #key - name of file in bucket 
    Key='s31.html'
)
print(response)
'''

#download a file to local system
'''
response = client.get_object(
    Bucket='aws-s3-chpr',
    Key="s3.py"
)
'''
# py s3.py > output.log -- gives log
#print(response)

#to get body use get("body").read() it gives in binary
#to decode use .decode()
'''
print(response.get("Body").read().decode())
'''
#storing data in another file
'''
data=response.get("Body").read().decode()
file=open("output1.py","w")
file.write(data)
file.close()
'''


#list s3 buckets
#py s3.py > output.log
'''
response = client.list_buckets()
buckets=response.get("Buckets")
print(f"total buckets in aws is : {len(buckets)}")
print(buckets)
'''

#list objects in bucket
'''
response=client.list_objects(
    Bucket='aws-s3-chpr'
)
objects= response.get("Contents")
print(f"Total objects : {(len(objects))}")
print(objects)
'''

#Delete file in buckets
'''
response=client.delete_object(
    Bucket='aws-s3-chpr',
    Key='s31.html'
)
print(response)
'''

#Delete bucket
'''
response=client.delete_bucket(
    Bucket='chpr'
)

print(response)
'''

