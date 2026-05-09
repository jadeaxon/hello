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

MsgBox(Format("{} {}", sum, max_index))


