$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath

$python3Check = Get-Command asdf -all 2>$null | Where-Object {$_.Version -Like "3.*"} 2>$null


if ($python3Check) {
    "Python 3 is already installed and in the path"
}
else {
    "installing python"
    Install-Python
    "python installed"
}


function Install-Python {
    Invoke-WebRequest https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe -OutFile C:\Users\bt-se\Downloads\my-py-installer.exe
}
