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

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    README = readme_file.read()

setup(
    author="Zuru Tech HK Limited, All rights reserved.",
    author_email="ml@zuru.tech",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Systems Administration",
    ],
    description="Use pip-tools to compile a requirements.in folder into pinned dependencies.",
    entry_points={"console_scripts": ["reqompyler=reqompyler.cli:main"]},
    python_requires=">=3.7",
    install_requires=["Click>=7.0", "pip-tools>=4.4.1"],
    license="Apache License, Version 2.0",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=["reqompyler", "pip-tools", "dependencies"],
    name="reqompyler",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/zurutech/reqompyler",
    version="0.1.0",
    zip_safe=False,
)
