#!/usr/bin/env bash

set -xe
    
# Add a test user under debian/ubuntu (remove any existing test user first)
getent passwd test-cbc && userdel --remove test-cbc
adduser test-cbc --disabled-password --gecos "Testing CBC"

conda=./miniconda3/bin/conda

sudo --user test-cbc --login -- <<EOF
# Echo commands and abort on errors
set -xe

# Download and install miniconda
curl -sO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b

# Setup conda with defaults
$conda init

# Install conda-bash-completion
$conda install -c conda-forge conda-bash-completion
EOF

# Get a new shell with the above enviroment
su -l test-cbc
