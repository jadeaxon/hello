#Requires AutoHotkey v2.0

; Register <C-S h> hotkey.
; When you press the hotkey, its code block will run.
; A script with hotkey definitions stays running permanently.
; An icon will show up for it in the Windows tray icons using the default AHK icon.
; You can right click on that icon to exit the script.
; You can have multiple AHK scripts running at the same time.
; Seems like the last started script sees the hotkey if two scripts handle the same hotkey.
^+h::
{
	MsgBox("Hello, AHK v2!")

}

; You can make hotkeys word only in certain windows.
; This one will only run in Notepad.
#HotIf WinActive("ahk_class Notepad")
^+n::
{
	MsgBox("Should only trigger in Notepad")
}

