Creating a development environment for DrumBurp
===============================================

This file contains instructions on creating an environment for development of
the DrumBurp drum music editor. DrumBurp is available from www.whatang.org.

Install Python
==============

Install the latest version of Python 2.7 from www.python.org, or from your
Linux distribution's package manager. DrumBurp uses Python 2, not Python 3.

If on Windows, note whether you have installed the 32 bit or 64 bit version
of Python.

Install pip
===========

The latest versions of python include pip in their distribution. If pip is not
included in the version of python you installed, run the get-pip.py script in
this directory using the python you just installed.

Install PyQt4
=============

Windows
~~~~~~~

According to the version of Python that you installed earlier, run either the 
x32 or x64 installer for PyQt4 in this directory. Newer versions of PyQt4 are
available from http://www.riverbankcomputing.co.uk/software/pyqt/download, but
these installers are the specific version that DrumBurp is built and tested 
against.

Linux
~~~~~

You can either build PyQt4 from source, or install it from your distribution's
package manager. Installing from a package manager means you may not have the
same versions of Qt and PyQt which are used to create DrumBurp.

To install from source:

1. Download the Qt 4.8.6 source from 
   http://download.qt.io/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.tar.gz
2. Follow the instructions on installing Qt given at 
   http://qt-project.org/doc/qt-4.8/install-x11.html
3. Download PyQt 4.11 from http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11/PyQt-x11-gpl-4.11.tar.gz/download
   This file is also available in this directory.
4. Unzip the PyQt4 package and do
	python configure-ng.py
	make
	make install

Mac
~~~

Follow the instructions to build from source as for Linux, but make the 
following changes:

1. Follow the instructions on installing Qt given at
   http://qt-project.org/doc/qt-4.8/install-mac.html
2. Instead of downloading the x11 PyQt4 package, get the mac version. This file 
   is also available in this directory.  

Install pygame
==============

DrumBurp uses pygame to work with MIDI. If pygame is not installed, DrumBurp
will still work, but no MIDI functionality will be available.

Windows
~~~~~~~

Use the 32 or 64 bit installer available in this directory to install pygame.

Linux
~~~~~

Your distribution may have a version of pygame available to be installed. You
want at least version 1.9.1. If this is not available, you can build from source
using the pygame-1.9.1release.tar.gz file in this directory. Unzip the archive
and do python setup.py install.

Mac
~~~

There are some compiled versions of pygame for Mac available from 
http://www.pygame.org/download.shtml.

If these do not work, you can try building from source as for Linux above.

Install Python packages
=======================

Using pip, do

pip install -r frozen_pip

This will install various packages which are necessary for developing and
building DrumBurp, including pylint and pyinstaller.
 

Developing
==========

DrumBurp source should be checked with pylint. There is a pylintrc file in the
root directory which sets the correct options for checking.

DrumBurp has been mostly developed using Eclipse + PyDev.

Building
========

See the build directory for instructions on building a DrumBurp release.
