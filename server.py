import grpc
from concurrent import futures
import time

from apiGRPC import text_speech_pb2 as pb2
from apiGRPC import text_speech_pb2_grpc as pb2_grpc
from gtts import gTTS
import io


class TextSpeechService(pb2_grpc.TextSpeech):

    def __init__(self, *args, **kwargs):
        pass

    def Say(self, request, context):
        text = request.text
        tts = gTTS(text=text, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return pb2.Speech(Audio=fp.read())



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TextSpeechServicer_to_server(TextSpeechService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server starting on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()