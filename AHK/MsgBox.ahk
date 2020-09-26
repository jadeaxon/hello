#SingleInstance Force

; A simple OK message box.
MsgBox,, OK, This is a message.

MsgBox, 4, Yes/No, Did you like the last message?
IfMsgBox, No
	MsgBox,,, You are hard to please.
Else
	MsgBox,,, You are easily amused.




