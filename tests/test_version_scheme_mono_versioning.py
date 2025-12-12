from __future__ import annotations

from typing import NamedTuple

import pytest
from commitizen.version_schemes import Increment, Prerelease
from commitizen.version_schemes import VersionProtocol

from cz_mono.mono_version_scheme import MonoVersion


class VersionSchemeTestArgs(NamedTuple):
    current_version: str
    increment: Increment | None
    prerelease: Prerelease | None
    prerelease_offset: int
    devrelease: int | None


@pytest.mark.parametrize(
    "version_args, expected_version",
    [
        (
            VersionSchemeTestArgs(
                current_version="1",
                increment="PATCH",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "2",
        ),
        (
            VersionSchemeTestArgs(
                current_version="2",
                increment="MINOR",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "3",
        ),
        (
            VersionSchemeTestArgs(
                current_version="3",
                increment="MAJOR",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "4",
        ),
        (
            VersionSchemeTestArgs(
                current_version="10",
                increment="PATCH",
                prerelease=None,
                prerelease_offset=0,
                devrelease=None,
            ),
            "11",
        ),
    ],
)
def test_bump_mono_version(version_args: VersionSchemeTestArgs, expected_version: str):
    assert (
        str(
            MonoVersion(version_args.current_version).bump(
                increment=version_args.increment,
                prerelease=version_args.prerelease,
                prerelease_offset=version_args.prerelease_offset,
                devrelease=version_args.devrelease,
            )
        )
        == expected_version
    )


def test_mono_scheme_property():
    version = MonoVersion("1")
    assert version.scheme is MonoVersion


def test_mono_implements_version_protocol():
    assert isinstance(MonoVersion("1"), VersionProtocol)
