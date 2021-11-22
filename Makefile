# Build for local testing
build:
	mkdir -p ./messages
	rm -rf ./messages/*
	python3 -m grpc_tools.protoc -I ./protobufs --python_out=./messages --grpc_python_out=./messages ./protobufs/*.proto

# Run gRPC Service locally
run:
	./run.sh

# Build with containers
build-docker:
	docker build . -t grpc-service

# Run gRPC Service via container
run-docker:
	docker run -p 50051:50051 grpc-service
