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
-------

According to the version of Python that you installed earlier, run either the 
x32 or x64 installer for PyQt4 in this directory. Newer versions of PyQt4 are
available from http://www.riverbankcomputing.co.uk/software/pyqt/download, but
these installers are the specific version that DrumBurp is built and tested 
against.

Linux
-----

You can either build PyQt4 from source, or install it from your distribution's
package manager. Installing from a package manager means you may not have the
same versions of Qt and PyQt which are used to create DrumBurp.

To install from source:

1. Download the Qt 4.8.6 source from 
   http://download.qt.io/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.tar.gz

2. Follow the instructions on installing Qt given at 
   http://qt-project.org/doc/qt-4.8/install-x11.html
   
   You should make sure that you have the make, gcc, g++ and libxext-dev 
   packages installed before trying to install Qt.

3. Download SIP from http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.8/sip-4.16.8.tar.gz/download
   This file is also available in this directory. Unpack the SIP archive. Do
   
     python configure.py
     make
     make install
   
   You may need to install the python-dev package with your package manager
   for this step to work.

4. Download PyQt 4.11 from http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11/PyQt-x11-gpl-4.11.tar.gz/download
   This file is also available in this directory. Unzip the PyQt4 package and do
	
	python configure-ng.py
	make
	make install

  For this step to work you may need to specify the --qmake and --sip-incdir
  options to the first command (python configure-ng.py). You should give these
  options the paths where qmake and sip.h were installed by steps 2 and 3 above.

Mac
---

Follow the instructions to build from source as for Linux, but make the 
following changes:

1. Follow the instructions on installing Qt given at
   http://qt-project.org/doc/qt-4.8/install-mac.html
2. Instead of downloading the x11 PyQt4 package, get the mac version. This file 
   is also available in this directory.  

I've never built DrumBurp for a Mac so I've got no proof that it will work at 
all. 

Install pygame
==============

DrumBurp uses pygame to work with MIDI. If pygame is not installed, DrumBurp
will still work, but no MIDI functionality will be available.

Windows
-------

Use the 32 or 64 bit installer available in this directory to install pygame.

Linux
-----

Your distribution may have a version of pygame available to be installed. You
want at least version 1.9.1. If this is not available, you can build from source
using the pygame-1.9.1release.tar.gz file in this directory. Unzip the archive
and do python setup.py install.

Mac
---

There are some compiled versions of pygame for Mac available from 
http://www.pygame.org/download.shtml.

If these do not work, you can try building from source as for Linux above.


Install pywin
=============

This step only applies for Windows systems. It is necessary for pyinstaller to
work when building a DrumBurp release.

Runn the appropriate 32 or 64 bit pywin32 installer available in this directory.
Newer versions of pywin may be available from 
http://sourceforge.net/projects/pywin32/files/


Install Python packages
=======================

Using pip, do

pip install -r frozen_pip

This will install various packages which are necessary for developing and
building DrumBurp, including pylint and pyinstaller.
 


Fix Pyinstaller
===============

Pyinstaller has a bug on Windows which leads to an annoying error popup whenever
a built version of DrumBurp starts. To remove this error the following change
needs to be made after pyinstaller has been installed by pip.

Find the Lib/site-packages/Pyinstaller directory. Open the file build.py and
change line 1587 from

            if tpl[2] == "BINARY":
            
to

            if tpl[2] in ("BINARY", "DATA"):


Developing
==========

DrumBurp source should be checked with pylint. There is a pylintrc file in the
root directory which sets the correct options for checking.

DrumBurp has been mostly developed using Eclipse + PyDev.

Building
========

See the build directory for instructions on building a DrumBurp release.
