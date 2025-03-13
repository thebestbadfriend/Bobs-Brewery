$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath

$python3Check = Get-Command python -all 2>$null | Where-Object {$_.Version -Like "3.*"} 2>$null

if ($python3Check) {
    "Python 3 is already installed and in the path"
}
else {
    "Python 3 is either not installed or not in the path"
}
