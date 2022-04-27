#!/usr/bin/env bash

set -xe
    
# Add a test user under debian/ubuntu (remove any existing test user first)
getent passwd test-cbc && userdel --remove test-cbc
adduser test-cbc --disabled-password --gecos "Testing CBC"

conda=./miniconda3/bin/conda

sudo --user test-cbc --login -- <<EOF
# Echo commands and abort on errors
set -xe

# Install miniconda
bash /Miniconda3-latest-Linux-x86_64.sh -b

# Setup conda without default activation
$conda init

# Install conda-bash-completion into the XDG directory outside of miniconda3 
mkdir -p .local/share/bash-completion/completions
pushd .local/share/bash-completion/completions || exit
curl -sO https://raw.githubusercontent.com/tartansandal/conda-bash-completion/master/conda
popd || exit

EOF

# Get a new shell with the above enviroment
su -l test-cbc
