# -*- coding: utf-8 -*-
#
# Copyright 2020 Zuru Tech HK Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Console script for reqompyler."""

import sys
from pathlib import Path
from typing import Iterable, Optional

import click
from reqompyler import reqcompyle


@click.command()
@click.option(
    "-i",
    "req_in",
    "--in",
    help="Path to requirements.in folder",
    default="./requirements.in",
    show_default=True,
    type=click.Path(exists=True),
)
@click.option(
    "-o",
    "req_pinned",
    "--output",
    help="Path to pinned requirements folder",
    default="./requirements",
    show_default=True,
    type=click.Path(),
)
@click.option(
    "--tld",
    "tld",
    help=(
        "Ideally the top-level-directory of the package (ie, were there is a setup.py). "
        "If not None will be used to export a copy of your dev.txt as requirements.txt"
    ),
    default=".",
    show_default=True,
    type=click.Path(),
)
@click.option(
    "--ignore",
    "ignore",
    help="Requirements.in file (without extension) to ignore,"
    "if they are required by another they will be used but no dedicate"
    ".txt file will be generated.",
    default=["linting"],
    show_default=True,
    type=click.STRING,
)
def main(
    req_in: str, req_pinned: str, tld: Optional[str], ignore: Optional[Iterable[str]]
):
    """Console script for reqompyler."""
    print("Compiling requirements!")
    if isinstance(ignore, str):
        ignore = [ignore]
    reqcompyle(
        Path(req_in),
        Path(req_pinned),
        Path(tld) if tld else None,
        [Path(i) for i in ignore] if ignore else None,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover, pylint: disable=no-value-for-parameter
