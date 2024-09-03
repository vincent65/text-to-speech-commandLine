import grpc
from apiGRPC import text_speech_pb2
from apiGRPC import text_speech_pb2_grpc
import os
import subprocess

def play_audio(file_path):
    if os.name == 'posix':  # For Linux and macOS
        subprocess.run(["afplay" if os.uname().sysname == "Darwin" else "aplay", file_path])
    elif os.name == 'nt':  # For Windows
        from playsound import playsound
        playsound(file_path)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = text_speech_pb2_grpc.TextSpeechStub(channel)
        text = input("Enter the text you want to convert to speech: ")
        response = stub.Say(text_speech_pb2.Text(text=text))
        
        # Save the audio to a temporary file
        temp_file = "temp_audio.wav"
        with open(temp_file, "wb") as f:
            f.write(response.Audio)
        
        print(f"Playing audio... (saved as {temp_file})")
        play_audio(temp_file)

if __name__ == '__main__':
    run()