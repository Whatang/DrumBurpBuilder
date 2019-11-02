pyinstaller -w -D -y --distpath dist -i DrumBurp\src\GUI\Icons\drumburp.ico DrumBurp\src\DrumBurp.py
Copy-Item DrumBurp\COPYING.txt dist
Set-Location dist
$version = Get-Content DrumBurp\DrumBurp.exe.manifest | where { $_ -match "DrumBurp.*version" } | % { $_ -replace ".*version=", "" } | % { $_ -replace "/>", "" } | % { $_ -replace '"', '' }
Get-Content DrumBurp.nsi | % { $_ -replace "__VERSION_TOKEN__", "${version}" } > DrumBurp-now.nsi
& "C:\Program Files (x86)\NSIS\makensis.exe" .\DrumBurp-now.nsi
Copy-Item  *.exe ..\output
Set-Location ..
