import boto3
import json
from fastapi import FastAPI

app = FastAPI()

s3 = boto3.resource("s3")
BUCKET_NAME = "lab2-demo-bucket-532188"

@app.get("/users")
def get_users():
    obj = s3.Object(BUCKET_NAME, "lab2/users.json")
    body = obj.get()['Body'].read()
    data = json.loads(body)
    return data

@app.get("/movies")
def get_movies():
    obj = s3.Object(BUCKET_NAME, "lab2/movie_data.json")
    body = obj.get()['Body'].read()
    data = json.loads(body)
    return data

