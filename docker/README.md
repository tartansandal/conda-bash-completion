# Testing installation targets and methods

Some instructins for setting up testing environments for different
targets and installation methods.

Run `make build` to build all the target Docker images.

Run `make ubuntu-focal` or similar to get a shell in the `ubuntu-focal`
environment.  The `./scripts/` directory will be mounted under `/`.

From the test environment, you can run the various scripts to:

* create a new test user
* install and init miniconda
* perform specific actions to install `conda-bash-completion`

See the various scripts and files for more details.
