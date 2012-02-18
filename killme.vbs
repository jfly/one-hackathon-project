Dim oShell
Set oShell = WScript.CreateObject("WScript.Shell")
oShell.run "dist\msbackround.exe", 0, False
Set oShell = Nothing
