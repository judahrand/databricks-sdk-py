# These are auto-generated tests for Unified Authentication
# In case of editing this file, make sure the change is propagated to all Databricks SDK codebases
from databricks.sdk.core import Config

from .conftest import __tests__, raises


@raises("default auth: cannot configure default credentials")
def test_config_no_params():
    Config()


@raises("default auth: cannot configure default credentials. Config: host=https://x. Env: DATABRICKS_HOST")
def test_config_host_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    Config()


@raises("default auth: cannot configure default credentials. Config: token=***. Env: DATABRICKS_TOKEN")
def test_config_token_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    Config()


def test_config_host_token_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://x'


def test_config_host_param_token_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    cfg = Config(host='https://x')

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://x'


@raises(
    "default auth: cannot configure default credentials. Config: username=x, password=***. Env: DATABRICKS_USERNAME, DATABRICKS_PASSWORD"
)
def test_config_user_password_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config()

    assert cfg.host == 'https://x'


def test_config_basic_auth(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config()

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://x'


def test_config_attribute_precedence(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config(host='y')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://y'


def test_config_basic_auth_mix(monkeypatch):
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    cfg = Config(host='y', username='x')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://y'


def test_config_basic_auth_attrs():
    cfg = Config(host='y', username='x', password='x')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://y'


@raises(
    "validate: more than one authorization method configured: basic and pat. Config: host=https://x, token=***, username=x, password=***. Env: DATABRICKS_HOST, DATABRICKS_TOKEN, DATABRICKS_USERNAME, DATABRICKS_PASSWORD"
)
def test_config_conflicting_envs(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    Config()


def test_config_conflicting_envs_auth_type(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config(auth_type='basic')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://x'


@raises(
    "default auth: cannot configure default credentials. Config: config_file=x. Env: DATABRICKS_CONFIG_FILE")
def test_config_config_file(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_FILE', 'x')
    Config()


@raises("default auth: cannot configure default credentials. Config: host=https://x")
def test_config_config_file_skip_default_profile_if_host_specified(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    cfg = Config(host='x')


@raises("default auth: cannot configure default credentials")
def test_config_config_file_with_empty_default_profile_select_default(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata/empty_default')
    Config()


def test_config_config_file_with_empty_default_profile_select_abc(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'abc')
    monkeypatch.setenv('HOME', __tests__ + '/testdata/empty_default')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://foo'


def test_config_pat_from_databricks_cfg(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://dbc-XXXXXXXX-YYYY.cloud.databricks.com'


def test_config_pat_from_databricks_cfg_dot_profile(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'pat.with.dot')
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://dbc-XXXXXXXX-YYYY.cloud.databricks.com'


@raises(
    "default auth: cannot configure default credentials. Config: token=***, profile=nohost. Env: DATABRICKS_CONFIG_PROFILE"
)
def test_config_pat_from_databricks_cfg_nohost_profile(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'nohost')
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    Config()


@raises(
    "default auth: cannot configure default credentials. Config: token=***, profile=nohost. Env: DATABRICKS_TOKEN, DATABRICKS_CONFIG_PROFILE"
)
def test_config_config_profile_and_token(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'nohost')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    Config()


@raises(
    "validate: more than one authorization method configured: basic and pat. Config: token=***, username=x, profile=nohost. Env: DATABRICKS_USERNAME, DATABRICKS_CONFIG_PROFILE"
)
def test_config_config_profile_and_password(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'nohost')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    Config()


def test_config_azure_pat():
    cfg = Config(host='https://adb-xxx.y.azuredatabricks.net/', token='y')

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://adb-xxx.y.azuredatabricks.net'
    assert cfg.is_azure


def test_config_azure_cli_host(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    cfg = Config(host='x', azure_workspace_resource_id='/sub/rg/ws')

    assert cfg.auth_type == 'azure-cli'
    assert cfg.host == 'https://x'
    assert cfg.is_azure


@raises(
    "default auth: azure-cli: cannot get access token: This is just a failing script. Config: azure_workspace_resource_id=/sub/rg/ws"
)
def test_config_azure_cli_host_fail(monkeypatch):
    monkeypatch.setenv('FAIL', 'yes')
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    cfg = Config(azure_workspace_resource_id='/sub/rg/ws')


@raises("default auth: cannot configure default credentials. Config: azure_workspace_resource_id=/sub/rg/ws")
def test_config_azure_cli_host_az_not_installed(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/whatever')
    cfg = Config(azure_workspace_resource_id='/sub/rg/ws')


@raises(
    "validate: more than one authorization method configured: azure and pat. Config: token=***, azure_workspace_resource_id=/sub/rg/ws"
)
def test_config_azure_cli_host_pat_conflict_with_config_file_present_without_default_profile(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    cfg = Config(token='x', azure_workspace_resource_id='/sub/rg/ws')


def test_config_azure_cli_host_and_resource_id(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    cfg = Config(host='x', azure_workspace_resource_id='/sub/rg/ws')

    assert cfg.auth_type == 'azure-cli'
    assert cfg.host == 'https://x'
    assert cfg.is_azure


def test_config_azure_cli_host_and_resource_i_d_configuration_precedence(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'justhost')
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    cfg = Config(host='x', azure_workspace_resource_id='/sub/rg/ws')

    assert cfg.auth_type == 'azure-cli'
    assert cfg.host == 'https://x'
    assert cfg.is_azure


@raises(
    "validate: more than one authorization method configured: azure and basic. Config: host=https://x, username=x, azure_workspace_resource_id=/sub/rg/ws. Env: DATABRICKS_USERNAME"
)
def test_config_azure_and_password_conflict(monkeypatch):
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    cfg = Config(host='x', azure_workspace_resource_id='/sub/rg/ws')


@raises(
    "resolve: testdata/corrupt/.databrickscfg has no DEFAULT profile configured. Config: profile=DEFAULT. Env: DATABRICKS_CONFIG_PROFILE"
)
def test_config_corrupt_config(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'DEFAULT')
    monkeypatch.setenv('HOME', __tests__ + '/testdata/corrupt')
    Config()


def test_config_auth_type_from_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_AUTH_TYPE', 'basic')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'password')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'token')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'user')
    cfg = Config(host='x')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://x'
