from __future__ import annotations

import importlib.metadata as metadata
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

from commitizen.version_schemes import SCHEMES_ENTRYPOINT

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _git_env() -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join([str(PROJECT_ROOT / "src"), env.get("PYTHONPATH", "")])
    # Avoid user/system git config (e.g., gpg signing) interfering with tests.
    env.setdefault("GIT_CONFIG_GLOBAL", os.devnull)
    env.setdefault("GIT_CONFIG_SYSTEM", os.devnull)
    return env


def _run(cmd: list[str], cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess:
    result = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise AssertionError(
            f"Command {' '.join(cmd)} failed ({result.returncode})\nstdout: {result.stdout}\nstderr: {result.stderr}"
        )
    return result


@pytest.fixture(scope="session")
def ensure_entry_point() -> metadata.EntryPoint:
    eps = metadata.entry_points().select(group=SCHEMES_ENTRYPOINT, name="mono")
    if not eps:
        pytest.skip(
            "mono version scheme entry point not installed; "
            "install the project (e.g. `pip install -e .`) to run e2e tests."
        )
    return next(iter(eps))


def _init_repo(repo_path: Path, env: dict[str, str]) -> None:
    _run(["git", "init", "-q"], cwd=repo_path, env=env)
    _run(["git", "config", "user.email", "test@example.com"], cwd=repo_path, env=env)
    _run(["git", "config", "user.name", "Commitizen Tester"], cwd=repo_path, env=env)
    _run(["git", "config", "commit.gpgsign", "false"], cwd=repo_path, env=env)

    (repo_path / "pyproject.toml").write_text(
        textwrap.dedent(
            """
            [tool.commitizen]
            name = "cz_conventional_commits"
            version = "1"
            version_scheme = "mono"
            tag_format = "v$version"
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    _run(["git", "add", "pyproject.toml"], cwd=repo_path, env=env)
    _run(["git", "commit", "-m", "chore: init"], cwd=repo_path, env=env)


def test_cli_bump_uses_mono_scheme(tmp_path: Path, ensure_entry_point: metadata.EntryPoint) -> None:
    env = _git_env()
    repo_path = tmp_path / "repo"
    repo_path.mkdir()
    _init_repo(repo_path, env)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commitizen",
            "bump",
            "--yes",
            "--increment",
            "PATCH",
            "--dry-run",
            "--get-next",
        ],
        cwd=repo_path,
        env=env,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr
    output = result.stdout.strip().splitlines()
    assert output, "Expected bump output"
    assert output[-1] == "2", f"Unexpected bump output: {result.stdout}"
