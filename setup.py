# SPDX-FileCopyrightText: 2026 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Build script for adafruit-lgpio.

Source files are vendored from upstream lgpio (https://github.com/joan2937/lg).
Update src/ and lgpio.i when bumping the version in pyproject.toml.

SWIG is required to generate lgpio.py from lgpio.i; it is installed by
cibuildwheel's before-all step (see pyproject.toml).
"""

from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_py import build_py as _build_py


class build_py(_build_py):
    # lgpio.py is produced by SWIG during build_ext; run that first.
    def run(self):
        self.run_command("build_ext")
        return super().run()


# Always build statically (bundles all lg*.c source) so wheels are
# self-contained — same as upstream's PYPI=1 mode.
lgpio_module = Extension(
    "_lgpio",
    sources=[str(p) for p in Path("src").glob("lg*.c")] + ["lgpio.i", "src/rgpiod.c"],
    libraries=["rt", "dl"],
    include_dirs=["src"],
    extra_compile_args=["-O3", "-pthread"],
)

setup(
    ext_modules=[lgpio_module],
    py_modules=["lgpio"],
    cmdclass={"build_py": build_py},
)
