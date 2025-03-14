# Execute the bob's brewery program without all the compilation hassle
$scriptPath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptPath

$BBEntryPoint = "main.py"

python "$($dir)\\$($BBEntryPoint)"