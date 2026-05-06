#Requires AutoHotkey v2.0

; Note that for function calls that are the first thing on a line, you don't have to use ()s.
; Other than that, you do.

; You can run Windows commands from AHK.
Run "Notepad.exe"

; You can also open up websites.
Run "https://www.autohotkey.com"

; You can open directories.
; There is a builtin variable set to your desktop folder.
Run(A_Desktop) ; use explicit ()s


