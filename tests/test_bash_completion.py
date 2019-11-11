import pytest


class TestBashCompletion:
    @pytest.mark.complete("conda")
    def test_base_command(self, completion):
        assert completion

    @pytest.mark.complete("conda -", require_cmd=True)
    def test_top_level_options(self, completion):
        assert completion
        assert completion == ['--help', '--version']

    @pytest.mark.complete("conda ", require_cmd=True)
    def test_top_level_commands(self, completion):
        assert completion
        assert completion == [
            'activate',
            'build',
            'clean',
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

    @pytest.mark.complete("conda d", require_cmd=True)
    def test_top_level_partial_cmds(self, completion):
        assert completion
        assert completion == [
            'deactivate',
            'debug',
            'develop',
        ]

    @pytest.mark.complete("conda develop --", require_cmd=True)
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

    @pytest.mark.xfail()
    @pytest.mark.complete("conda env ", require_cmd=False)
    def test_sub_comands(self, completion):
        assert completion == [
            'create',
            'export',
            'list',
            'remove',
            'update',
        ]

    @pytest.mark.complete("conda env create --", require_cmd=True)
    def test_sub_comand_options(self, completion):
        assert completion
        assert completion == [
            '--file',
            '--force',
            '--help',
            '--json',
            '--name',
            '--prefix',
            '--quiet',
            '--verbose',
        ]

    @pytest.mark.complete("conda build ", require_cmd=True)
    def test_build_sub_comands(self, completion):
        assert completion
        assert 'purge' in completion
        assert 'purge-all' in completion
