
; Read =-separated fields from each line.
; Trim any whitespace from extracted fields.
Loop, read, C:\Users\jadeaxon\.properties 
{
	Loop, parse, A_LoopReadLine, = 
	{
		; Trimming of spaces happens automatically on assignment.
		field = %A_LoopField%
		MsgBox, Field number %A_Index% is '%field%'.
	}
}

