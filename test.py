import requests
from PIL import Image

image_data = open("test.jpg","rb").read()
image = Image.open("test.jpg").convert("RGB")

try:
	response = requests.post("http://localhost:80/v1/vision/face/recognize",
	files={"image":image_data}).json()

	for user in response["predictions"]:
	    print(user["userid"])

	print("Full Response: ",response)
	for face in response["predictions"]:
	    userid = face["userid"]
	    y_max = int(face["y_max"])
	    y_min = int(face["y_min"])
	    x_max = int(face["x_max"])
	    x_min = int(face["x_min"])
	    cropped = image.crop((x_min,y_min,x_max,y_max))
	    cropped.save("face.jpg")
	    
except:
	print("failed to fetch")
	