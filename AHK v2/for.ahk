#Requires AutoHotkey v2.0

sum := 0
max_index := 0

; Loop over an array.
A := [1, 2, 3, 4]
for i, v in A {
	; i is the array index
	; v is the array value at that index
	; the object you loop over must be enumerable via the __Enum special method
	sum += v
	max_index := (i > max_index) ? i : max_index
}

MsgBox(Format("{} {}", sum, max_index), "Results", "T2") ; timeout in 2 seconds

; You can iterate over the attribute values of an object.
; One-off objects aren't intrinsically iterable, so you have to call ownProps().
; Python calls them attributes whereas it looks like AHK calls them properties.
o := {name: "Bilbo", race: "hobbit", age: 111}
attributes := ""
values := ""
for a, v in o.ownProps() {
	attributes .= a . " "
	values .= v . " "
}
attributes := RTrim(attributes)
values := RTrim(values)

MsgBox(Format("{} {}", attributes, values), "Results", "T2")


