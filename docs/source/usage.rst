=====
Usage
=====

To use ``reqompyler`` in a project:

.. code-block:: console

    $ reqompyler --help

    Usage: reqompyler [OPTIONS]

      Console script for reqompyler.

    Options:
      -i, --in PATH      Path to requirements.in folder  [default:
                        ./requirements.in]
      -o, --output PATH  Path to pinned requirements folder  [default:
                        ./requirements]
      --tld PATH         Ideally the top-level-directory of the package (ie, were
                        there is a setup.py). If not None will be used to export
                        a copy of your dev.txt as requirements.txt  [default: .]
      --ignore TEXT      Requirements.in file (without extension) to ignore,
                        if they are required by another they will be used but no dedicated
                        .txt file will be generated.  [default: linting]
      --help             Show this message and exit.


----

.. click:: reqompyler.cli:main
   :prog: reqompyler
