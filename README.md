# conda-bash-completion

Bash completion support for the `conda` command.

## Installation

The easiest way to install this is via the `conda-bash-completion` package:
```
conda install -c tartansandal conda-bash-completion
````

If you have already setup conda shell initialization via `conda init bash`, then simply
restarting your shell should be sufficient to complete the integration.

For conda versions prior to 4.8, you may have to add a modified version of the following
to the end of your `~/.bashrc` file:
```
. ~/anaconda3/etc/profile.d/bash_completion.sh
```
where `~/anaconda3` is the root of you ananconda or miniconda installation.

If you already have a `bash-completion` package installed system-wide (see
[Repology](https://repology.org/project/bash-completion) for a comprehensive list of
operating system distributions, package names, and available versions), and already have
your shell set up to load completions, then you could simply copy the `conda` completion
script to the `~/.local/share/bash-completion/completions/` directory.


## Testing

The tests require `bash-completion`, `pytest`, `pexpect` installed in an active conda environment.
You could run something like:
```
conda activate devenv
conda install -c tartansandal pytest pexpect bash-completion
pytest
```
