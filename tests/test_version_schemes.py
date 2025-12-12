from typing import NamedTuple

from commitizen.config.base_config import BaseConfig
from commitizen.version_schemes import get_version_scheme, Increment, Prerelease

from cz_mono.mono_version_scheme import MonoVersion


class VersionSchemeTestArgs(NamedTuple):
    current_version: str
    increment: Increment | None
    prerelease: Prerelease | None
    prerelease_offset: int
    devrelease: int | None


def test_version_scheme_mono(config: BaseConfig):
    config.settings["version_scheme"] = "mono"
    scheme = get_version_scheme(config.settings)
    assert scheme is MonoVersion
