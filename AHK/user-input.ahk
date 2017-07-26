; An input box can be used to get user input.
InputBox, name, Question, What is your name?
if (name = "Jeff")
	; MsgBox does not use {} values like Send.  Thus no need for {!}.
	MsgBox Hello, %name%!
else
	MsgBox Go away!



