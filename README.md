# Bash completion support for the `conda` command

We currently support completion for commands, options, sub-commands,
sub-command options.  For example:

```console
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

> Note: on some systems you have to hit `<tab>` twice to trigger completion.

Completions are dynamically determined based on the plugins you have loaded and
the help strings for the various commands. This makes completion a little slower
than it could be, however, it does allows the code to automatically adjust to
future changes, and hence, minimising the need for maintenance.

> Note: MacOS has `bash-3.2` (from 2007) installed by default. The upstream
> [`bash-completion`](https://github.com/scop/bash-completion) library, which we
> depend on, requires a `bash >= 4.2`, so you will need to upgrade your bash if
> you want to use this script. Upgrading bash is possible, either via homebrew
> or conda, or other methods, but you probably want to search for how to change
> the location of your shell in MacOS.

## Installation

There are two supported ways to install this feature:

### Method 1: Using `conda`

The easiest way to install this feature is via the `conda-bash-completion`
package:

```bash
conda install -c conda-forge conda-bash-completion
```

This installs the completion code and a specially patched version of the
[`bash-completion`](https://github.com/scop/bash-completion) library into you
default environment.  If you have already set up conda shell initialization via
`conda init bash`, then simply restarting your shell should be sufficient to
complete the integration.

Some uses prefer to disable the automatic activation of their `base` environment
by setting `auto_activate_base: false` in their `~/.condarc` file.  These users
will need to append something like the following

```bash
CONDA_ROOT=~/anaconda3   # <- set to your Anaconda/Miniconda installation directory
if [[ -r $CONDA_ROOT/etc/profile.d/bash_completion.sh ]]; then
    source $CONDA_ROOT/etc/profile.d/bash_completion.sh
else
    echo "WARNING: could not find conda-bash-completion setup script"
fi
```

to their `~/.bashrc` script in order to have the completion code loaded. Note,
the above block **must** be run after any existing bash-completion setup and
after the conda initialization block.

<details>
<summary>Note for Arch linux users and AUR installation</summary>

 If you have installed Conda using AUR (Arch User Repository) please note that in some cases you should install `conda-bash-completion` as root and place following in your `~/.bashrc`
```
CONDA_ROOT=/opt/miniconda3   # <- set to your Anaconda/Miniconda installation directory
if [[ -r $CONDA_ROOT/etc/profile.d/bash_completion.sh ]]; then
    source $CONDA_ROOT/etc/profile.d/bash_completion.sh
else
    echo "WARNING: could not find conda-bash-completion setup script"
fi
```
Tested: [miniconda3](https://aur.archlinux.org/packages/miniconda3)
</details>

### Method 2: Manually

If you already have the
[`bash-completion`](https://github.com/scop/bash-completion) library installed
system-wide (see [Repology](https://repology.org/project/bash-completion) for
a comprehensive list of operating system distributions, package names, and
available versions), and already have your shell set up to load completions,
then you could simply copy the `conda` completion script to the
`~/.local/share/bash-completion/completions/` directory.

## Testing

The tests require `bash-completion`, `pytest`, `pexpect` installed in an active
conda environment.

You could run something like:

```bash
conda activate base
conda install -c tartansandal pytest pexpect bash-completion
pytest
```

Ideally would like a dev enironment to be set up and used.

Seem to have some problems with activation and changing the prompt, which
confuses pexpect.

At some point I'll figure out how to do that, but for release testing I'm just
using my current environment.

## Thanks

Thanks to Kale Franz (@kalefranz) for encouranging me to work on this in the
first place :smile:.

Thanks to Simon Frei (@imsodin) for raising and providing extensive help in
debugging some difficult integration cases.

Thanks to Mike Sarahan (@msarahan) for encourangment and discusions that lead to
packaging this feature rather than hard wiring it into the bash initialization.

Special thanks to all users who have provided feeback on issues and
bugs. :smile:
