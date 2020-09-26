#SingleInstance Force

; Ask user for input and assign it to the variable 'name'.
name := ""
; InputBox, <response out>, <title>, <prompt>
InputBox, name, Name, What is your name?
MsgBox,, Greetings, Hello, %name%`!

ExitApp




