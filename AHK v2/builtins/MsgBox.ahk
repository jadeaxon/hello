#Requires AutoHotkey v2.0

; MsgBox(<message>, [<title>, <options>])
; <title> defaults to A_ScriptName
MsgBox("A simple message box")
MsgBox("The message", "Message") ; with title
MsgBox("This message will self destruct . . .", "Volatile Message", "T2") ; with timeout

; You can combine hex values into button(s), icon, and default button options.
; https://www.autohotkey.com/docs/v2/lib/MsgBox.htmGroup_1_Buttons
; Yes/No/Cancel + Question Icon + 2nd button default: 0x123
; You don't so much use hex as add strings to your options string.
MsgBox("Do you enjoy taxes?", "Taxes", "YNC Icon? Default2")

; MsgBox returns a string based on what user did. Or "Timeout" if they didn't act.
response := MsgBox("Click OK before message box times out", "Click Me", "T4")
MsgBox("Response from last message box: " . response)


