[![Use this template](https://github.com/stack-instance/badge.svg)](https://github.com/stack-instance?stack_template_owner=antgrutta&stack_template_repo=py-grpc-stack)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Python gRPC Stack
This template repository contains a bare-bones Python gRPC stack that can be used when starting a new project.

## Included in this stack

```
.
|__ .devcontainer          # For GitHub CodeSpaces or Visual Studio Code Remote.
|__ .github                # Where all the project templates and GitHub Actions are stored.
|__ interceptors           # A home for gRCP Interceptors.
|   |__ request_header.py  # A simple interceptor that logs request headers.
|__ protobufs              # A home for gRPC Protobufs.
|   |__ service.proto      # A simple gRPC Proto file with stubs for CRUD operations.
|__ services               # A home for gRPC service classes.
|   |__ service.py         # A simple gRPC service class that implements the service.proto file.
|__ .dockerignore          # A list of files to ignore when building the Docker image.
|__ .gitignore             # A list of files to ignore when committing to the repository.
|__ LICENSE                # The license for the project.
|__ Makefile               # A Makefile for various automation tasks.
|__ README.me              # You're reading it!
|__ app.py                 # The main application script (starts the gRPC server).
|__ config.py              # Configuration settings for the service.
|__ requirements.txt       # A list of dependencies for the service.
|__ run.sh                 # A script that sets up the environment and starts the gRPC server via app.py.
```

## Building for local development
If you are looking to avoid Docker and you have Python installed, you can build the project locally using the Makefile.  As a prerequiste, make sure you have [virtualenv](https://virtualenv.pypa.io/en/latest/) installed.  You will want to run `pip3 install -r requirements.txt` from your virtualenv before running `make`.

Running `make build` will create the required `messages` folder and run the [Protocol Buffer Compiler](https://grpc.io/docs/protoc-installation/) to generated the pb2 files.

Finally, running `make run` will start the gRPC server using the options set in the `config.py` file.

## Building with Docker
If you are looking to use Docker, you can build the container image using the `make build-docker` command.  The resulting image will be tagged as `grpc-service`.  Running it can be accomplished with `make run-docker`, the default port of `50051` will be used.

## Resources

* [GitHub CodeSpaces](https://github.com/features/codespaces)
* [Visual Studio Code Remote](https://code.visualstudio.com/docs/remote/containers)
* [GitHub Actions](https://github.com/features/actions)
* [gRCP Interceptors](https://grpc.io/blog/grpc-web-interceptor/)
* [gRPC Protobufs](https://grpc.io/docs/what-is-grpc/introduction/)

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.
