#Requires AutoHotkey v2.0

; The default input box is large, so we bass it width and height.
ib := InputBox("Enter a value: ", "Input Value", "w200 h100")
MsgBox("You entered: " . ib.value)


