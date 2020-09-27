; An object is mainly just an associative array.
; member == property

; You can create an object using {member: value, ...} literals.
; Or with the Object() function.
; Each key can be an expression result.
o := {value: "Value of the value member.", trash: "Delete me."}
o := Object("value", "Value of the value member.", "trash", "Delete me.") ; same thing

; Access a member using <object ref>.<member name>.
MsgBox, % format("o.value = {1}", o.value)

; Check if a variable is an object ref.
check := isObject(o)
if (check) {
	MsgBox, o is an object (reference).
}

; Set a member's value.
o.trash := "total garbage"
o["trash"] := "absolute junk"

; Delete a member.
o.delete("trash")

; Iterate over an object's members.
message := "Members:`r`n"
for k, v in o {
	message .= k . " => " v . "`r`n"
}
MsgBox, % message



ExitApp



