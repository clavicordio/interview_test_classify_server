import classification_pb2_grpc
from classification_pb2 import B64Image, ImageCategory, ClassificationResponse
import grpc
from concurrent import futures
import base64
import numpy as np
from PIL import Image
import random
import datetime

INPUT_SHAPE = 1, 3, 128, 128


def foo(img):
    print('... running a neural network ...')
    return random.randint(0, 1)


class ClassificationService(
    classification_pb2_grpc.ClassificationServicer
):
    def Classify(self, b64img, context):
        bytes = b64img.b64image
        width = b64img.width
        height = b64img.height

        b64decoded = base64.b64decode(bytes)

        img_arr = np.frombuffer(b64decoded, dtype=np.uint8).reshape(width, height, -1)
        im = Image.fromarray(img_arr)

        ts = str(datetime.datetime.now()).replace(':','-')
        im = im.resize((INPUT_SHAPE[2], INPUT_SHAPE[3]))
        im.save('received_%s.png' % ts)

        img_arr_resized = np.asarray(im).reshape(*INPUT_SHAPE)

        # classify image
        category = foo(img_arr_resized)

        return ClassificationResponse(category=category)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    classification_pb2_grpc.add_ClassificationServicer_to_server(
        ClassificationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()