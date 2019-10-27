# Install packages to create a Windows environment for building DrumBurp
Start-Process msiexec.exe -Wait -ArgumentList '/I python-2.7.17.amd64.msi /quiet /a /passive /qn'
Start-Process PyQt4-4.11-gpl-Py2.7-Qt4.8.6-x64.exe -Wait -ArgumentList '/S'
Start-Process pip -Wait -ArgumentList 'install -r frozen_pip'
