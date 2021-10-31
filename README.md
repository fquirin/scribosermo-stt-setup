# Scribosermo STT Setup

[Scribosermo](https://gitlab.com/Jaco-Assistant/Scribosermo) is a LGPL licensed, open-source speech recognition engine to "Train fast Speech-to-Text networks in different languages".  
  
[Evaluation tests for German language](https://github.com/domcross/german-stt-evaluation) suggest that it's currently one of the fastest and most accurate open-source STT systems.
  
This repository trys to offer build scripts to run and test Scribosermo on different platforms focussing on Raspberry Pi SBC.
Ultimately the goal is to build a module for [SEPIA STT-Server](https://github.com/SEPIA-Framework/sepia-stt-server).

## Build wheels on Debian 10 x86 64bit (the long way)

- Install required packages: `apt-get update && apt-get install -y --no-install-recommends sudo git wget curl nano unzip zip procps build-essential cmake python3-pip python3-dev python3-setuptools python3-wheel python3-venv libsndfile1`
- Install Rust compiler (might be required): `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and refresh terminal `source $HOME/.cargo/env`
- Create and activate Python virtual env: `mkdir -p install && cd install && python3 -m venv env && source env/bin/activate`
- Make sure pip is updated (tested v21.3.1): `pip3 install --upgrade pip`
- Install part 1: `pip3 install wheel setuptools setuptools_rust transformers tqdm librosa datasets jiwer`
- Install part 2: `pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime`
- Install part 3: `pip3 install ds-ctcdecoder==0.10.0a3;`
- Create wheels as needed: `pip3 wheel [package]`

# Credits

- [DanBmh](https://github.com/DanBmh) - Development and maintaining of Scribosermo
- [Domcross](https://github.com/domcross) - German STT evaluation, scripts and packages
- [SEPIA Framework](https://github.com/SEPIA-Framework) - Open assistant and STT server stuff
