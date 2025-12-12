# [Commitizen](https://github.com/commitizen-tools/commitizen) Mono Versioning Plugin

## Overview

This is a dead simple [Commitizen](https://github.com/commitizen-tools/commitizen) plugin that provides
mono versioning scheme.

If you're just using a single number as your version (e.g., `1`, `2`, `3`), this plugin will help you manage version
bumps and create changelogs accordingly.

## Installation

Using uv (recommended):

```shell
uv add cz-mono
```

or

Using pip:

```shell
pip install cz-mono
```

## Usage

In your `pyproject.toml`, set the `version_scheme` field to `mono` under the `[tool.commitizen]` section:

```toml
[tool.commitizen]
version_scheme = "mono"
```

Now, when you run `cz bump` or `cz ch`, it will use the mono versioning scheme to determine the next version.
