# Bash completion support for the `conda` command.

We currently support completion for commands, options, sub-commands,
sub-command options.  For example:

```
$ conda <tab>
activate   convert     develop   info      list         render   skeleton    verify
build      create      env       init      metapackage  run      uninstall    
clean      deactivate  help      inspect   package      search   update       
config     debug       index     install   remove       server   upgrade      
$ conda

$ conda d<tab>
deactivate  debug  develop
$ conda de

$ conda --<tab>
--help  --version 
$ conda --

$ conda develop --<tab>
 --build_ext  --clean  --help  --name  --no-pth-file  --prefix  --uninstall
$ conda develop --

$ conda env <tab>
create  export  list    remove  update
$ conda env 

$ conda env create --<tab>
--file  --force  --help  --json --name  --prefix  --quiet  --verbose
$ conda env create --
```

Completions are dynamically determined based on the plugins you have loaded and
the help strings for the various commands. This make completion a little slower
than it could be, however, this does allows the code to automatically adjust to
future changes, and hence, minimising the need for maintenance.

## Installation

The easiest way to install this is via the `conda-bash-completion` package:
```
conda install -c tartansandal conda-bash-completion
````

If you have already setup conda shell initialization via `conda init bash`, then simply
restarting your shell should be sufficient to complete the integration.

If you have chosen to not automatically activate your default environment, then you may
have to add the following to the end of your `~/.bashrc` file:

```
source $CONDA_ROOT/etc/profile.d/bash_completion.sh
```

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

## Thanks!

Thanks to Kale Franz (@kalefranz) for encouranging me to work on this in the first place :smile:.

Thanks to Simon Frei (@imsodin) for raising and providing extensive help in debugging some difficult integration cases.

Thanks to Mike Sarahan (@msarahan) for encourangment and discusions that lead to
packaging this feature rather than hard wiring it into the bash initialization.
