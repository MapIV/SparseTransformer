#!/bin/bash

set -e

export TORCH_CUDA_ARCH_LIST="6.0;6.1;7.0;7.5;8.0;8.6+PTX;8.7;8.9;9.0+PTX;12.0+PTX"
export SPTR_VERSION="1.0.0+cu128"

# python 3.9
uv python pin 3.9
uv build --wheel --extra-index-url https://download.pytorch.org/whl/cu128 --verbose

# python 3.10
uv python pin 3.10
uv build --wheel --extra-index-url https://download.pytorch.org/whl/cu128 --verbose

# python 3.11
uv python pin 3.11
uv build --wheel --extra-index-url https://download.pytorch.org/whl/cu128 --verbose

# python 3.12
uv python pin 3.12
uv build --wheel --extra-index-url https://download.pytorch.org/whl/cu128 --verbose
