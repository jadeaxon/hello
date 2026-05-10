#Requires AutoHotkey v2.0

form := Gui(, "Form")
form.addText(, "First name:")
form.addText(, "Last name:")
form.addEdit("vfirst_name ym")  ; The ym option starts a new column of controls.
form.addEdit("vlast_name")
form.addButton("default", "OK").OnEvent("Click", process_form)
form.OnEvent("Close", process_form)
form.show()

process_form(*) {
    submission := form.submit()  ; Save the contents of named controls into an object.
    MsgBox("You entered '" submission.first_name " " submission.last_name "'.")
}

