import os
from pymilvus import (
    connections,
    utility,
)

fmt = "\n=== {:30} ===\n"

print(fmt.format("start connecting to Milvus"))
host = os.environ.get('MILVUS_HOST')
if host == None:
    host = "localhost"
print(fmt.format(f"Milvus host: {host}"))
connections.connect("default", host=host, port="19530")

print(fmt.format("Drop collection `hello_milvus_pk`"))
utility.drop_collection("hello_milvus_pk")

print(fmt.format(f"Drop collection `hello_milvus_pk_recover`"))
utility.drop_collection("hello_milvus_recover_pk")