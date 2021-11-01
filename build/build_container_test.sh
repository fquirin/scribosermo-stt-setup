#!/bin/bash
# TODO: make version number variable - add '--no-cache' ?
if [ -n "$(uname -m | grep aarch64)" ]; then
	echo "Building Scribosermo Docker container for aarch64"
	sudo docker build -t sepia/scribosermo:test_aarch64 .
elif [ -n "$(uname -m | grep armv7l)" ]; then
	echo "Building Scribosermo Docker container for armv7l"
	sudo docker build -t sepia/scribosermo:test_armv7l .
else
	echo "Building Scribosermo Docker container for amd64"
	sudo docker build -t sepia/scribosermo:test_amd64 .
fi
