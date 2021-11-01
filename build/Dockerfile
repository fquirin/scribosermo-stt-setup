FROM debian:buster-slim

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# Files
#ADD share/wheels-pip-21_3_1/* /home/installer/

# Run 1
RUN echo 'Installing dependencies...' && \
#
#   Dependencies
    apt-get update && \
    apt-get install -y --no-install-recommends \
    sudo git wget curl nano unzip zip procps \
    build-essential \
    python3-pip python3-dev python3-setuptools python3-wheel libsndfile1 && \
    pip3 install --upgrade pip && \
    pip3 install wheel setuptools && \
    mkdir -p /home/installer && cd /home/installer && \
    if [ -n "$(uname -m | grep aarch64)" ]; then \
        echo "Downloading and installing Scribosermo aarch64 requirements"; \
        wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/ds_ctcdecoder-0.10.0a3-cp37-cp37m-linux_aarch64.whl; \
        wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/tflite_runtime-2.5.0.post1-cp37-cp37m-linux_aarch64.whl; \
        wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/numpy-1.20.3-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl; \
        wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/regex-2021.10.23-cp37-cp37m-linux_aarch64.whl; \
        wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/tokenizers-0.10.3-cp37-cp37m-linux_aarch64.whl; \
        wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/transformers-4.12.2-py3-none-any.whl; \
        pip3 install numpy-1.20.3-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl; \
        pip3 install tflite_runtime-2.5.0.post1-cp37-cp37m-linux_aarch64.whl; \
        pip3 install ds_ctcdecoder-0.10.0a3-cp37-cp37m-linux_aarch64.whl; \
        pip3 install regex-2021.10.23-cp37-cp37m-linux_aarch64.whl; \
        pip3 install tokenizers-0.10.3-cp37-cp37m-linux_aarch64.whl; \
        pip3 install transformers tqdm librosa dataset jiwer; \
    elif [ -n "$(uname -m | grep armv7l)" ]; then \
        echo "UNDER CONSTRUCTION - Downloading and installing Scribosermo armv7l requirements"; \
		wget https://github.com/fquirin/scribosermo-stt-setup/releases/download/v0.0.1/ds_ctcdecoder-0.10.0a3-cp37-cp37m-linux_armv7l.whl; \
		pip3 install transformers tqdm librosa dataset jiwer; \
        pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime; \
        pip3 install ds_ctcdecoder-0.10.0a3-cp37-cp37m-linux_armv7l.whl; \
    else \
        echo "Downloading and installing Scribosermo x86_64 requirements"; \
		pip3 install transformers tqdm librosa dataset jiwer; \
        pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime; \
        pip3 install ds-ctcdecoder==0.10.0a3; \
    fi && \
    cd /home && \
    sudo rm -rf installer && \
#
#   Clean up
    apt-get remove -y build-essential && \
    apt-get clean && apt-get autoclean && apt-get autoremove -y && \
#
#   Create user
    useradd --create-home --shell /bin/bash admin && \
    adduser admin sudo && \
    echo "admin ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
#
#   ENV
#SOME_ENV_VAR=/...my-stuff

#   USER
USER admin

# Run 1
RUN echo "Installing Scribosermo scripts ..." && \
    cd /home/admin && \
    git clone --single-branch --depth 1 -b main https://github.com/fquirin/scribosermo-stt-setup.git && \
    mkdir -p scribosermo-stt-setup/tests/model && \
    echo "#!/bin/bash" > on-docker.sh && echo "cd scribosermo-stt-setup/tests && python3 testing_tflite.py" >> on-docker.sh
	
# Start
WORKDIR /home/admin
CMD bash on-docker.sh
