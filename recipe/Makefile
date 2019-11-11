# aliases for maintaining this conda package

.PHONY: build install convert

VERSION=1.3-1
PACKAGE=conda-bash-completion-$(VERSION).tar.bz2

build:
	conda build .

install:
	conda install -c local --yes --force-reinstall conda-bash-completion

convert:
	conda convert -p all -o ~/anaconda3/conda-bld ~/anaconda3/conda-bld/linux-64/$(PACKAGE)
	anaconda upload --skip-existing ~/anaconda3/conda-bld/*/$(PACKAGE)
