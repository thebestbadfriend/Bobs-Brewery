# Check if running as admin and  prompt for admin privileges if not
if(!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
 Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList "-File `"$($MyInvocation.MyCommand.Path)`"  `"$($MyInvocation.MyCommand.UnboundArguments)`""
 Exit
}


$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath
$downloadsPath = (New-Object -ComObject Shell.Application).Namespace('shell:Downloads').Self.Path


$python3Check = Get-Command python -all 2>$null | Where-Object {$_.Version -Like "3.*"} 2>$null
$postgresql17Check = Get-Command asdf -all 2>$null | Where-Object {$_.Version -Like "17.*"} 2>$null
$postgresInstalledPath = "C:\Program Files\PostgreSQL\17asdfasdf"


function Install-Python {
    # Download Python 13
    $pythonInstallerURL = "https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe"
    $installerFilePath = "$($downloadsPath)\bb-pyinstaller.exe"
    Invoke-WebRequest $pythonInstallerURL -OutFile $installerFilePath

    # Install Python 13
    cmd /c $installerFilePath /passive PrependPath=1
}


function Install-Postgresql {
    # Download PostgreSQL 17
    $postgresInstallerURL = "https://sbp.enterprisedb.com/getfile.jsp?fileid=1259403"
    $installerFilePath = "$($downloadsPath)\bb-postgres17installer.zip"

    "Downloading PostgreSQL 17 installer"
    Invoke-WebRequest $postgresInstallerURL -OutFile $installerFilePath
    "Installer downloaded"

    # Install PostgreSQL 17
    ## Create PostgreSQL 17 filepath
    if (Test-Path -PathType Container $postgresInstalledPath) {
        """$($postgresInstalledPath)"" already exists"
    }
    else {
        "creating ""$($postgresInstalledPath)"""
        New-Item -ItemType Directory -Force -Path $postgresInstalledPath
        "created ""$($postgresInstalledPath)"""
    }

    # Extract PostgreSQL 17 to its proper path
    Expand-Archive -Path $installerFilePath -DestinationPath $postgresInstalledPath
    
    
    # Add C:\Program Files\PostgreSQL\17\bin to the path
    $pathBackupDir = "C:\Temp"
    "Ensuring $($pathBackupDir) exists"
    if (Test-Path -PathType Container $pathBackupDir) {
        """$($pathBackupDir)"" already exists"
    }
    else {
        """$($pathBackupDir)"" does not exist"
        "creating ""$($pathBackupDir)"""
        New-Item -ItemType Directory -Force -Path $pathBackupDir
        "created ""$($pathBackupDir)"""
    }
    "backing up system path"
    $env:Path > "$($pathBackupDir)\system_path_backup.bak"
    "system path backed up"

    "adding PostgreSQL 17 to path"
    setx PATH "$($env:Path);\$($postgresInstalledPath)\pgsql\lib"
    "PostgreSQL 17 added to path"
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
    "installing PostgreSQL 17"
    Install-Postgresql
    "PostgreSQL 17 installed and added to path"
}


"installing python libraries"
Install-BBDependencies
"python libraries installed"


"creating desktop shortcut"
Create-DesktopShortcut
"desktop shortcut created"