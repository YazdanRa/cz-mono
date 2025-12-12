import pytest
from commitizen.config import BaseConfig
from commitizen.defaults import DEFAULT_SETTINGS


@pytest.fixture()
def config():
    _config = BaseConfig()
    _config.settings.update({"name": DEFAULT_SETTINGS["name"]})
    return _config
