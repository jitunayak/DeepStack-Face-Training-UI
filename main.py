import streamlit as st
from PIL import Image, ImageDraw
import os

# Run below cmd on Docker
# sudo docker run -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 --name deepfacerecog deepquestai/deepstack

st.title("Train images")

img1 = st.file_uploader("Upload first face", type=["png", "jpg", "jpeg"])
img2 = st.file_uploader("Upload second face", type=["png", "jpg", "jpeg"])
username = st.text_input("Enter Person's Name")
btn = st.button("Upload")

if btn:
	pil_image1 = Image.open(img1)
	pil_image2 = Image.open(img2)
	file_path1 = "images/"+username+"1"+".jpg"
	pil_image1.save(file_path1)
	file_path2 = "images/"+username+"2"+".jpg"
	pil_image2.save(file_path2)
	script = "python register.py "+file_path1+" "+file_path2+" "+username
	print(script)
	a  = os.popen(script).readlines()
	st.write(a)


st.title("Test new images")

test_img = st.file_uploader("Upload a new face", type=["png", "jpg", "jpeg"])
if test_img:
	pil_test = Image.open(test_img)
	pil_test.save("test.jpg")
	a = os.popen("python test.py").readlines()
	st.write(a)
	st.image("face.jpg")

