; Demonstrates reading from a file.

EnvGet, home, USERPROFILE

; Read =-separated fields from each line.
; Trim any whitespace from extracted fields.
Loop, read, %home%\.properties 
{
	; In a read loop, each line is read into A_LoopReadLine w/o newline chars.
	Loop, parse, A_LoopReadLine, = 
	{
		; In a parse loop, each field is read into A_LoopField.
		; The 1-based index of the field is assigned to A_Index.
		;
		; Trimming of spaces happens automatically on assignment.
		field = %A_LoopField%
		MsgBox, Field number %A_Index% is '%field%'.
	} ; next field
} ; next line

