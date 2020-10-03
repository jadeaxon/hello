; An associative array is a collection of key/value pairs.
; Generally, the keys are stings (not numbers like in normal arrays).
; Keys are unique; values are not.
a := {price: 5, color: "green", quantity: 20}
component := {name: "wheel", position: "front left"}
colors := ["red", "blue", "green", "yellow"]

; Access the value of a key by either . or [].
MsgBox % a.color " == " a["color"]

; Assign a value for a key.
; The advantage of [] is that you can do [<expression>].
; Also they allow key names that contain spaces.
a["color"] := "yellow"
a.color := "yellow"
a["col" . "or"] := "yellower"
a["secondary color"] := "brown"

if (a.hasKey("secondary color")) {
	MsgBox % "My secondary color is " . a["secondary color"] . "."
}

; You can nest arrays.  References are stored.
a.wheel := component
a.allowedColors := colors

; Chain the . operator.
MsgBox % a.wheel.position

; Loop over an associative array.
string := ""
for key, value in a {		
	string .= key . " => " . (isObject(value) ? "{...}" : value) . "`n"
}
MsgBox % string

; Delete a key/value pair.
a.delete(wheel)


