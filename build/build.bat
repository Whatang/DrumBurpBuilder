pyinstaller -w -D -y --distpath C:\build -i C:\DrumBurp\src\GUI\Icons\drumburp.ico C:\DrumBurp\src\DrumBurp.py
copy C:\DrumBurp\DrumBurp.nsi .
"C:\Program Files (x86)\makensis.exe" DrumBurp.nsi
copy *.exe C:\output
