#SingleInstance Force

; If MsgBox is called with only one arg, it uses it as the message.
; Also, the comma is optional between command and first arg unless the first arg is empty.
MsgBox Called with one arg.
MsgBox,,, Same thing using 3 args.

; A simple OK message box.
MsgBox,, OK, This is a message.

MsgBox, 4, Yes/No, Did you like the last message?
IfMsgBox, No
	MsgBox,,, You are hard to please.
Else
	MsgBox,,, You are easily amused.




