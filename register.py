import requests
import sys

image1 =  sys.argv[1]
image2 =  sys.argv[2]
username = sys.argv[3]

user_image1 = open(image1,"rb").read()
user_image2 = open(image2,"rb").read()


print("registered for ",username)
response = requests.post("http://localhost:80/v1/vision/face/register",
files={"image1":user_image1,"image2":user_image2},data={"userid":username}).json()


print(response)
