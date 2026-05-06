#Requires AutoHotkey v2.0

; This should just loop 3 times.
s := ""
Loop(3) {
	s .= "loop`n"
}

MsgBox(s)

