# DeepStack-Face-Training-UI

## Run below cmd to start the Docker
```
sudo docker run -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 --name deepfacerecog deepquestai/deepstack
```

## Install streamlit
```
pip install streamlit
```

## Run streamlit

```
streamlit run main.py    
```

![alttext](https://github.com/jitunayak/DeepStack-Face-Training-UI/blob/master/screen1.png)
