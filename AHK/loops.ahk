; Infinite loop.  Using break and continue.
loop {
	if (A_Index <= 30) {
		continue
	}
	MsgBox loop: Iteration %A_Index%.  Breaking.
	break
}

; Count loops.
loop 2 {
	MsgBox loop 2: Iteration %A_Index%.
}

; loop % <positive integer expression>
loop % 1 + 1 {
	MsgBox loop `% 1 + 1: Iteration %A_Index%.
}

; Until loop.
i := 1
loop {
	i++
	MsgBox loop until (i == 2): Iteration %A_Index%.
}
until (i == 2)

; While loops.
i := 1
while (i <= 2) {
	i++
	MsgBox while (i <= 2): Iteration %A_Index%.
}

; String parsing loop.
; You cannot use OTB style.
record := "foo | bar |baz | qux"
loop, parse, record, |, %A_Space%%A_Tab%
{
	MsgBox %A_Index%: %A_LoopField%
} ; next field

; CSV parsing loop.
; You cannot use OTB style.
record =
( LTrim
	"foo","bar,bar","baz""baz","qux",quux
)
loop, parse, record, CSV
{
	MsgBox %A_Index%: %A_LoopField%
} ; next field


; Files loop.
; Recursively find all files and directories in System dir on desktop.
; Note that if you use just a directory (no glob) it won't recurse into it.
files := ""
loop, files, C:\Users\%A_UserName%\projects\hello\AHK\*.*, RFD
{
	; Skip any file that is either H (Hidden), R (Read-only), or S (System). Note: No spaces in "H,R,S".
	if A_LoopFileAttrib contains H,R,S  
	    continue  ; Skip this file and move on to the next one.
	files .= A_LoopFileFullPath . "`r`n"
}
MsgBox %files%


; Key/value for loop.  Array loop.
a := ["one", "two", "three"]
for k, v in a {
	MsgBox %k% => %v%
}






