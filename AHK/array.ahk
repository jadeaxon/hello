; Arrays are objects.  Objects who only have numeric indexes (member names).

; Note that array indexing is 1-based (unlike every other language).
; Note that arrays are not restricted to one type of value.
a := [1, 2, "three"]
a := Array(1, 2, "three") ; same thing as above
MsgBox, % format("a[1] = {1}", a[1])

; Insert values *before* the given index.
a.insertAt(1, "foo", "bar")

; Push values onto the end of the array.
a.push("baz", "qux")

MsgBox, % join(",", a*)

; Remove element at given index.
removed := a.removeAt(1) ; pop
removed := a.pop()


MsgBox, % join(",", a*)

length := a.length()
mini := a.minIndex()
maxi := a.maxIndex()

; Loop over array.
Loop % a.length()
{
	MsgBox, % a[A_Index]
}

ExitApp


; Joins strings together.
; There is no builtin StrJoin() or Array.join(), surprisingly.
join(sep, params*) {
	for index, param in params
		str .= param . sep
	return SubStr(str, 1, -StrLen(sep))
}


