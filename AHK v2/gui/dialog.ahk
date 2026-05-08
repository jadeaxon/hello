#Requires AutoHotkey v2.0

; This is a dialog I use for handling recurring tasks.
; It basically returns the string label value of whatever button you press.
; Uses accelerator keys via & so you can just use keyboard.
; Also makes it so Esc dismisses the dialog.
dialog() {
    myGui := Gui("+AlwaysOnTop", "Defer Task")
    myGui.SetFont("s10", "Segoe UI")
    myGui.Add("Text",, "Defer for how long?")
    
    choice := ""

	myGui.OnEvent("Escape", (guiObj) => guiObj.Hide())
    myGui.Add("Button", "Default w80", "&Day?").OnEvent("Click", (btn, *) => (choice := btn.Text, myGui.Hide()))
    myGui.Add("Button", "x+10 w80", "&Week?").OnEvent("Click", (btn, *) => (choice := btn.Text, myGui.Hide()))
    myGui.Add("Button", "x+10 w80", "&Month?").OnEvent("Click", (btn, *) => (choice := btn.Text, myGui.Hide()))

    myGui.Show()
    
    ; This loop keeps the function from returning until a button or Esc is pressed.
    while (WinExist("ahk_id " myGui.Hwnd) && DllCall("IsWindowVisible", "Ptr", myGui.Hwnd))
        Sleep(50)

	choice := StrReplace(choice, "&")
	choice := StrReplace(choice, "?")
	choice := StrLower(choice)
	myGui.Destroy()
    return choice
}

choice := dialog()
MsgBox("You chose this: " choice)

