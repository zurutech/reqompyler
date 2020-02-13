# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/zurutech/reqompyler/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitLab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitLab issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Reqompyler could always use more documentation, whether as
part of the official Reqompyler docs, in docstrings,
or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/zurutech/reqompyler/issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `reqompyler` for local development.

1. Clone `reqompyler` from the GitHub repository:

    ```console
    $ git clone https://github.com/zurutech/reqompyler.git
    ```

2. Install your local copy into a virtualenv. Assuming you have `virtualenvwrapper` installed, this is how you set up your fork for local development:

    ```console
    $ mkvirtualenv reqompyler
    $ cd reqompyler/
    $ python setup.py develop
    ```

3. To get the dev toolchain just pip install the provided requirements into your virtualenv.

    ```console
    $ pip install -r requirements/dev.txt
    ```

4. Create a branch for local development:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass [flake8], [pylint], [black] and the tests, including testing other Python versions with [tox]:

    - Automatically run the pipeline with `tox`.

        ```console
        $ tox
        ```
        **Note:** `tox` can be run parallely with `tox -p auto -o`

    - Manually run them:

        ```console
        $ pytest -x -s -vvv --doctest-modules reqompyler tests --cov=reqompyler
        $ black reqompyler tests
        $ isort reqompyler tests
        $ flake8 reqompyler tests
        $ pylint reqompyler tests
        ```

6. Commit your changes and push your branch to GitLab:

    ```console
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitLab website.


## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for the specified Python Versions.
4. If you have made change to the CI Pipeline test them locally

## Tips

To run a subset of tests:

```console
$ pytest -x -s -vvv --doctest-modules WHAT_MODULE/TEST_SUBSET_TO_TEST --cov=ashpy
```


## Deploying
<!-- TODO: Redo this section -->

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.md).
Then run:

```console
$ bumpversion patch # possible: major / minor / patch
$ git push
$ git push --tags
```

Travis will then deploy to PyPI if tests pass.

<!-- Links -->
[black]: https://github.com/psf/black
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8]: https://github.com/PyCQA/flake8
[pylint]: https://github.com/PyCQA/pylint
[pytest-cov]: https://github.com/pytest-dev/pytest-cov
[pytest]: https://github.com/pytest-dev/pytest
[tox]: https://github.com/tox-dev/tox
