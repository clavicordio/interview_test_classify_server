import grpc
import numpy as np
import base64
import classification_pb2
import classification_pb2_grpc
from classification_pb2_grpc import ClassificationStub
from classification_pb2 import B64Image, ImageCategory, ClassificationResponse
from PIL import Image

WIDTH = 256
HEIGHT = 256

channel = grpc.insecure_channel("localhost:50051")
client = ClassificationStub(channel)

with Image.open('cat.png') as img:
    img_arr = np.asarray(img)
    data = base64.b64encode(img_arr)


image_req = classification_pb2.B64Image(b64image=data, width=img_arr.shape[0],
                                        height=img_arr.shape[1])

recommendations_response = client.Classify(image_req)

print(recommendations_response)
