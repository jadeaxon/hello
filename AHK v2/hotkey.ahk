#Requires AutoHotkey v2.0

; ^ -- <Control>
; # -- <Window>
; ! -- <Alt>
; + -- <Shift>

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
; The opening brace can be on the same line as the hotkey specifier.
#HotIf WinActive("ahk_class Notepad")
^+n:: {
	MsgBox("Should only trigger in Notepad")
}
; end apply hotkeys only to specific windows
#HotIf

^+k:: {
	; Report the hotkey pressed.
	MsgBox(A_ThisHotKey)
}

; You can use & to make a hotkey that combines *any* two keys.
a & o:: {
	MsgBox("Dual key hotkey")
}

; A hotkey can be a mouse button plus a key.
; Seems like you need to click the right mouse button before pressing a.
; WARNING: Yes, you have to be careful with these.
; The first key/click will get swallowed causing nothing to happen while it waits
; for the next key/click in the sequence to happen.
; You can use ~ to pass the input through to the active window.
; The events won't pass through until their up/release part.
~RButton & a:: {
	MsgBox(A_ThisHotKey)
}

; Use a hotkey to exit this app.
; You can do simple hotkeys on a single line.
^+x::ExitApp




