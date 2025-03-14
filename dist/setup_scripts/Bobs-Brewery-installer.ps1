$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath


$python3Check = Get-Command python -all 2>$null | Where-Object {$_.Version -Like "3.*"} 2>$null
$postgresql17Check = Get-Command psql -all 2>$null | Where-Object {$_.Version -Like "17.*"} 2>$null


function Install-Python {
    $pythonInstallerURL = "https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe"
    $downloadsPath = (New-Object -ComObject Shell.Application).Namespace('shell:Downloads').Self.Path
    $installerFilePath = "$($downloadsPath)\bb-pyinstaller.exe"
    Invoke-WebRequest $pythonInstallerURL -OutFile $installerFilePath

    cmd /c $installerFilePath /passive PrependPath=1
}


function Install-Postgresql {
    
}


function Install-BBDependencies {
    python -m pip install -r "$($dir)\requirements.txt"
    python -m pip freeze
}


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


if ($python3Check) {
    "Python 3 is already installed and in the path"
}
else {
    "installing python"
    Install-Python
    "python installed"
}


if ($postgresql17Check) {
    "postgresql 17 is already installed and in the path"
}
else {
    # Download postgresql 17
    # Install postgresql 17
    # Add C:\Program Files\PostgreSQL\17\bin to the path
}


"installing python libraries"
Install-BBDependencies
"python libraries installed"


"creating desktop shortcut"
Create-DesktopShortcut
"desktop shortcut created"