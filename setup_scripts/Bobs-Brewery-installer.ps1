$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath


$python3Check = Get-Command python -all 2>$null | Where-Object {$_.Version -Like "3.*"} 2>$null


function Install-Python {
    $pythonInstallerURL = "https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe"
    $downloadsPath = (New-Object -ComObject Shell.Application).Namespace('shell:Downloads').Self.Path
    $installerFilePath = "$($downloadsPath)\bb-pyinstaller.exe"
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


function Install-BBDependencies {
    python -m pip install -r "$($dir)\requirements.txt"
    python -m pip freeze
}


Install-BBDependencies


function Create-DesktopShortcut {
    $ShortcutTarget= "powershell.exe"
    $ShortcutArgs = "-NoExit -File ""$($dir)\..\Bob's Brewery.ps1"""
    $ShortcutFile = (New-Object -ComObject Shell.Application).Namespace('shell:Desktop').Self.Path + "\Bob's Brewery.lnk"
    $WScriptShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WScriptShell.CreateShortcut($ShortcutFile)
    $Shortcut.TargetPath = $ShortcutTarget
    $Shortcut.Arguments = $ShortcutArgs
    $Shortcut.IconLocation = "$($dir)\..\desktop.ico"
    $Shortcut.Save()
    "created shortcut"
}


Create-DesktopShortcut


