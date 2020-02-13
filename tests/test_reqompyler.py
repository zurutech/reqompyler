#!/usr/bin/env python
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

"""Tests for `reqompyler` package."""
from pathlib import Path
from typing import List, Union

import pytest
from click.testing import CliRunner

from reqompyler import cli, reqcompyle


@pytest.fixture()
def cli_args(tmpdir) -> List[Union[Path, str]]:
    """
    Fixture simulating a set of CLI arguments.

    Returns:
        List of args.

    """
    in_folder = Path("requirements.in")
    assert in_folder.exists()
    out_folder = Path(tmpdir).joinpath("fake_requirements")
    tld = Path(tmpdir)
    ignore = "linting"
    return [in_folder, out_folder, tld, ignore]


def test_cli(cli_args):
    """
    Test the CLI with default arguments.

    GIVEN the default arguments
        THEN the ignored pip-compiled file must NOT be present in the output folder.
        THEN the pip-compiled file must be present in the output folder.

    """
    in_folder, out_folder, tld, ignore = cli_args
    command = ["-i", in_folder, "-o", out_folder, "--tld", tld, "--ignore", ignore]
    runner = CliRunner()
    result = runner.invoke(cli.main, args=command)
    assert result.exit_code == 0
    assert "Compiling requirements!" in result.output
    # Test output
    assert Path(out_folder).exists()
    for i in ignore:
        assert not Path(out_folder).joinpath(i).exists()
    assert Path(tld).joinpath("requirements.txt").exists()


def test_cli_array_ignore(cli_args):
    """
    Test the CLI with an array of ignore values.

    WHEN passing a requirements file to ignore different from the default value
        THEN the ignored pip-compiled file must NOT be present in the output folder.

    """
    in_folder, out_folder, tld, _ = cli_args
    ignore = "linting, test"
    command = ["-i", in_folder, "-o", out_folder, "--tld", tld, "--ignore", ignore]
    runner = CliRunner()
    result = runner.invoke(cli.main, args=command)
    assert result.exit_code == 0
    assert "Compiling requirements!" in result.output
    # Test output
    for i in ignore.split(", "):
        assert not Path(out_folder).joinpath(i).exists()


def test_cli_no_tld_no_ignore(cli_args):
    """
    Test the CLI by pasing None to ignore and tld args.
    """
    in_folder, out_folder, tld, _ = cli_args
    command = ["-i", in_folder, "-o", out_folder, "--tld", "", "--ignore", ""]
    runner = CliRunner()
    result = runner.invoke(cli.main, args=command)
    assert result.exit_code == 0
    assert "Compiling requirements!" in result.output
    # Test output
    assert sorted([p.name for p in Path(in_folder).iterdir()]) == sorted(
        [p.name for p in Path(out_folder).iterdir()]
    )
    assert not Path(tld).joinpath("requirements.txt").exists()


def test_reqompyle_standard(cli_args):
    """Test if reqompyle generates the correct files/directories."""
    in_folder, out_folder, tld, ignore = cli_args
    reqcompyle(in_folder=in_folder, out_folder=out_folder, tld=tld, ignore=ignore)
    assert Path(out_folder).exists()
    for i in ignore:
        assert not Path(out_folder).joinpath(i).exists()
    assert Path(tld).joinpath("requirements.txt").exists()


def test_no_ignore_no_tld(cli_args):
    """Test that if ignore is not passed everything gets compiled."""
    in_folder, out_folder, tld, _ = cli_args
    reqcompyle(in_folder=in_folder, out_folder=out_folder, tld=None, ignore=None)
    assert sorted([p.name for p in Path(in_folder).iterdir()]) == sorted(
        [p.name for p in Path(out_folder).iterdir()]
    )
    assert not Path(tld).joinpath("requirements.txt").exists()
