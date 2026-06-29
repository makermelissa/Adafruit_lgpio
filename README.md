<!--
SPDX-FileCopyrightText: 2026 Melissa LeBlanc-Williams for Adafruit Industries

SPDX-License-Identifier: MIT
-->

# Adafruit Python lgpio

Pre-built wheels for [lgpio](https://github.com/joan2937/lg) covering **Python 3.13+**
on `aarch64` and `armv7l` Linux (Raspberry Pi, BeagleBoard, Odroid, and similar SBCs).

Upstream lgpio ships wheels for Python 3.9–3.12 on PyPI, but has no pre-built wheels
for Python 3.13 and later. Building from source requires SWIG, which most users don't
have installed. This package fills that gap.

It is published to PyPI as **`adafruit-lgpio`** and is a drop-in replacement for `lgpio`
on Python 3.13+.

## Usage

In your `requirements.txt` (example from Adafruit_Blinka):

```
lgpio>=0.2.2.0; sys_platform=='linux' and python_version<'3.13' and platform_machine in ('aarch64', 'armv7l')
adafruit-lgpio>=0.2.2.0; sys_platform=='linux' and python_version>='3.13' and platform_machine in ('aarch64', 'armv7l')
```

```python
import lgpio  # same import as upstream lgpio
```

## Version scheme

The version tracks upstream lgpio exactly (e.g. `0.2.2.0`).

## Source

The C extension source (`src/`, `lgpio.i`, `lgpio_extra.py`) is vendored from
[joan2937/lg](https://github.com/joan2937/lg) under the Unlicense.

## Updating for a new lgpio release

1. Update the vendored source files from upstream.
2. Bump `version` in `pyproject.toml` to match upstream.
3. Commit, create a GitHub release tagged `vX.Y.Z.W` — CI builds and publishes automatically.
