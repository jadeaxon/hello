; One of the main points of AutoHotkey is to let you define your own custom hotkeys.
; A hotkey is a keystroke plus modifier keys that performs some action (thus called hot) 
; beyond simply typing the symbol associated with that key.

; Hotkeys are defined as subroutine labels that indicated what key combo launches the subroutine.
; Normal subroutine labels end with one : but hotkey labels end with ::.

; ^ -- control key
; + -- shift key
; ! -- alt key
; # -- Windows key

; $ -- do not allow this hotkey to be retriggered by itself

; The directive makes it so only a single instance of this script can run at a time.
; If you launch it again, a new instance of the script replaces the existing one without asking you.
#SingleInstance Force

; <C-A h> pops up a message box.
$^!h::
	; The builtin MsgBox command displays a dialog popup.
	; When you are creating a new hotkey, it's good to use a message box to verify your hotkey gets
	; triggered when you think it should be.
	; MsgBox, <options>, <title>, <message>
	; Note that <options> is left blank.  This gives us the default OK dialog.
	; Using different options can give you OK/Cancel, Yes/No, and other dialogs.
	; Note that , and ! need to be quoted since they have special meaning otherwise.
	; AHK uses ` (backtick) to quote single characters.
	MsgBox,, Hello`, AHK hotkey`!, You have created a custom hotkey.
return ; Since a hotkey is really a subroutine, we need to return from it.



