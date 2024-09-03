build:
	protoc -I=. --python_out=. ./text_speech.proto

test:
	python -m grpc_tools.protoc --proto_path=. ./text_speech.proto --python_out=. --pyi_out=. --grpc_python_out=.
