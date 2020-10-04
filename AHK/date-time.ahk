date := A_Now
date += 7, days
MsgBox % date

date_str := ""
FormatTime, date_str, %date%, yyyy-MM-dd

MsgBox % date_str


