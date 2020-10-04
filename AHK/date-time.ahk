date := A_Now ; Get a YYYYMMDDhhmmss current timestamp.
date += 7, days ; A strange AHK-ism where an operator has extra args.

; It is not trivial to change the message box font to fixed-width to make this line up.
MsgBox % "YYYYMMDDhhmmss`n" . date

date_str := ""
FormatTime, date_str, %date%, yyyy-MM-dd

MsgBox % date_str
MsgBox % ("Thank God it's " . A_DDDD . "`!") ; A_DDDD is the full name of the day.

; I believe all the A_* date/time vars are string values.
; So, abs() it to get a number.
if (abs(A_YYYY) == 2020) {
	MsgBox % "I am sorry that 2020 is not over yet."
}


