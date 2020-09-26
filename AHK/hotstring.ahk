; A hostring is a sequence of keystrokes that triggers some action, whereas a hotkey
; is one keystroke (or mouse click) plus modifiers that triggers some action.

; AHK hotstrings are active globally--in every application running on your machine.
; This is nice in that you can define abbreviations, spelling corrections, etc. in just one spot and
; have them available everywhere.

; The simplest action a hostring can trigger is to just emit a different sequence of keystrokes.

; :<options>:<hotstring>::<action>

; Let's have abbreviations followed by x expand to their full name.  For example, USAx => United
; States of America.

; Allow only one instance of this script to run at a time.
#SingleInstance Force

; By default, a hotkey will trigger after a space, tab, or a punctuation character is entered.
; If we use the * option, then the hostring will trigger immediately.
; If we use the c option, then the hostring will be case sensitive.  Thus, usax won't trigger it.
:*c:USAx::United States of America

:*c:AHKx::AutoHotkey

; Hotstrings are not limited to simply emitting a different sequence of keystrokes; they can trigger
; arbitrary code to execute.
; Note that the hotstring can contain spaces when using the * option.
:*c:show me a message box::
	MsgBox,,, Here is your message box.
return


