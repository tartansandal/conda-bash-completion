import pytest


class TestConda:
    @pytest.mark.complete("conda")
    def test_base_command(self, completion):
        assert completion

    @pytest.mark.complete("conda -", require_cmd=True)
    def test_top_level_options(self, completion):
        assert completion
        assert completion == ['--help', '--version']

    @pytest.mark.complete("conda ")
    def test_top_level_commands(self, completion):
        assert completion
        assert completion == [
            'activate',
            'build',
            'clean',
            'compare',
            'config',
            'convert',
            'create',
            'deactivate',
            'debug',
            'develop',
            'env',
            'help',
            'index',
            'info',
            'init',
            'inspect',
            'install',
            'list',
            'metapackage',
            'pack',
            'package',
            'remove',
            'render',
            'run',
            'search',
            'server',
            'skeleton',
            'uninstall',
            'update',
            'upgrade',
            'verify',
        ]

    @pytest.mark.complete("conda d")
    def test_top_level_partial_cmds(self, completion):
        assert completion
        assert completion == [
            'deactivate',
            'debug',
            'develop',
        ]

    @pytest.mark.complete("conda develop --")
    def test_comand_options(self, completion):
        assert completion
        assert completion == [
            '--build_ext',
            '--clean',
            '--help',
            '--name',
            '--no-pth-file',
            '--prefix',
            '--uninstall',
        ]

    @pytest.mark.complete("conda env ")
    def test_sub_comands(self, completion):
        assert completion
        assert completion == [
            'config',
            'create',
            'export',
            'list',
            'remove',
            'update',
            'vars',
        ]

    @pytest.mark.complete("conda activate ")
    def test_environments(self, completion):
        assert completion
        assert 'conda-bash-comp-testing' in completion

    @pytest.mark.complete("conda env create --")
    def test_sub_comand_options(self, completion):
        assert completion
        assert completion == [
            '--dry-run',
            '--file',
            '--force',
            '--help',
            '--insecure',
            '--json',
            '--name',
            '--no-default-packages',
            '--offline',
            '--prefix',
            '--quiet',
            '--use-index-cache',
            '--verbose',
        ]

    @pytest.mark.complete("conda build ")
    def test_build_sub_comands(self, completion):
        assert completion
        assert 'purge' in completion
        assert 'purge-all' in completion

    @pytest.mark.complete("conda build --config-file ")
    def test_filename(self, completion):
        assert completion
        assert sorted(completion) == [
            'bashrc',
            'fake-package.tar.bz2',
            'inputrc',
        ]

    @pytest.mark.complete("conda verify ")
    def test_verify(self, completion):
        assert completion
        assert completion == ['fake-package.tar.bz2']

    @pytest.mark.complete("conda config ")
    def test_config(self, completion):
        assert completion == []

    @pytest.mark.complete("conda config --")
    def test_config_options(self, completion):
        assert completion
        assert completion == [
            '--append',
            '--describe',
            '--env',
            '--file',
            '--get',
            '--help',
            '--json',
            '--prepend',
            '--quiet',
            '--remove',
            '--remove-key',
            '--set',
            '--show',
            '--show-sources',
            '--stdin',
            '--system',
            '--validate',
            '--verbose',
            '--write-default',
        ]
