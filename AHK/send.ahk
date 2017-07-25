; Send keystrokes using AHK.

Run Notepad.exe
WinWaitActive Untitled - Notepad

; The 'Send' function sends keystrokes to active control.
; The backtick acts as escape character in AHK.  Thus `n is newline.
; This allows Windows paths to be quoted without having to use \\ everywhere.
; The `n here failed though.
;
; Special keys can be send using {<key name>}.
; A list of them is here: https://autohotkey.com/docs/commands/Send.htm.
;
; Send I can type things to Notepad!`nCan you?
; Send I can type things to Notepad!{Enter}Can you?
; For some reason {Enter} does not work if embedded in the string.

Send I can type things to Notepad!
Send {Enter}
; If you need to be extra precise, you can specify virtual key and scan code.
; Send {vk0Dsc01C} ; Enter
Send Can you?
Send {Enter}

; The reason was that !{Enter} means <Ctrl + Enter>.
Send I know that an exclamation point is a metachar{!}{Enter}Do you?{Enter}

; This fails because alt key is pressed and released before F4 is pressed.
; This just triggers the application menu which then swallows the F4.
; Send {Alt}{F4}
Send {Alt down}{F4}{Alt up}

Sleep 1000
Send n ; Don't save.


