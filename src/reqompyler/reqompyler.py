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
"""Use `pip-tools <https://github.com/jazzband/pip-tools>`_ to compile the requirements files."""

import subprocess
from pathlib import Path
from typing import List, Optional

__ALL__ = ["reqcompyle"]


def reqcompyle(
    in_folder: Path,
    out_folder: Path,
    tld: Optional[Path],
    ignore: Optional[List[Path]],
) -> None:
    """
    Compile requirements files using `pip-tools <https://github.com/jazzband/pip-tools>`_.

    Args:
        in_folder (:obj:`pathlib.Path`): Path to the folder with your requirements.in files.
        out_folder (:obj:`pathlib.Path`): Path to the folder were the pinned requirements
            file will be saved.
        tld (:obj:`pathlib.Path`): Top level directory of your package, if passed, copies pinned
            the ``dev.txt`` as ``requirements.txt`` to this location.
        ignore (:obj:`list` of [:obj:`pathlib.Path`]): Array of requirements files
            (without extension) to ignore.

    """
    if not (out_folder.exists() and out_folder.is_dir()):
        Path(out_folder).mkdir(parents=True)
    for req_file in in_folder.iterdir():
        if ignore and req_file.stem in ignore:
            continue
        subprocess.run(
            [
                "pip-compile",
                "--pre",
                "--annotate",
                f"--output-file={out_folder.joinpath(req_file.name)}",
                f"{in_folder.joinpath(req_file.name)}",
            ],
            capture_output=True,
        )
    if tld:
        subprocess.run(
            ["cp", out_folder.joinpath("dev.txt"), tld.joinpath("requirements.txt")]
        )
