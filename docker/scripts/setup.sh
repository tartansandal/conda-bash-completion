#!/usr/bin/env bash

set -xe
    
# Add a test user under debian/ubuntu (remove any existing test user first)
getent passwd test-cbc && userdel --remove test-cbc
adduser test-cbc --disabled-password --gecos "Testing CBC"

## Download and install miniconda as test-cbc
sudo --user test-cbc --login -- <<EOF
bash /Miniconda3-latest-Linux-x86_64.sh -b
EOF
