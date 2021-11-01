#!/bin/bash
if [ -n "$(uname -m | grep aarch64)" ]; then
	IMAGE_TAG=test_aarch64
elif [ -n "$(uname -m | grep armv7l)" ]; then
	IMAGE_TAG=test_armv7l
else
	IMAGE_TAG=test_amd64
fi
HOST_MODEL="$(realpath ~)/scribosermo/model"
HOST_SHARE="$(realpath ~)/scribosermo/share"
mkdir -p "$HOST_MODEL"
mkdir -p "$HOST_SHARE"
sudo docker run --rm --name=scribosermo -it \
	-v "$HOST_SHARE":/home/admin/share \
	-v "$HOST_MODEL":/home/admin/scribosermo-stt-setup/tests/model \
	sepia/scribosermo:$IMAGE_TAG \
	/bin/bash
