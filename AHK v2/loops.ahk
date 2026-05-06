#Requires AutoHotkey v2.0

; Infinite loop.
Loop {
	; A_Index has the current loop index.
	s := "Iteration " . A_Index
	if (A_Index == 5) {
		break
	}
}

; This should just loop 3 times.
s := ""
Loop(3) {
	s .= "loop`n"
}

MsgBox(s)

; Parse a comma-separated string.
s := "one,two,three"
L := []
Loop parse, s, "," {
    L.push(A_LoopField)
}

; Read from a file.
Loop read, "loops.ahk" {
    line := A_LoopReadLine
}

; There is no builtin way to convert an array to a string.
; There is no builtin join() function.
; MsgBox(L)
