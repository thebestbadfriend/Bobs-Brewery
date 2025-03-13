$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath

$python3Check = Get-Command python -all 2>$null | Where-Object {$_.Version -Like "3.*"} 2>$null


function Install-Python {
    $pythonInstallerURL = "https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe"
    $installerFilePath = "C:\my-py-installer.exe"
    Invoke-WebRequest $pythonInstallerURL -OutFile $installerFilePath

    cmd /c $installerFilePath /passive PrependPath=1
}


if ($python3Check) {
    "Python 3 is already installed and in the path"
}
else {
    "installing python"
    Install-Python
    "python installed"
}
