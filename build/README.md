# Building DrumBurp

DrumBurp is packaged using pyinstaller. The buildDrumBurp.py script builds the
appropriate package for the current platform and Python interpreter.

The script does 2 things:

- Creates a zip file containing all the source files needed to run DrumBurp, if
  Python, PyQt and pygame are all installed.
- Creates a zip file containing a version of DrumBurp packaged using pyinstaller
  for the current platform. The Python interpreter used to run the buildDrumBurp
  script is bundled with the package.

The resulting package is labelled according to the current platform, and whether
the Python interpreter is 32 or 64 bit.

Note: while Pyinstaller should work on a Mac, I have never tested packaging
DrumBurp on a Mac platform.
