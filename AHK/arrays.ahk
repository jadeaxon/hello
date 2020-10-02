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
removed := a.removeAt(1, 2) ; pop (but returns # of elements removed); shifts remaining elements left
removed := a.pop()

MsgBox, % join(",", a*)

length := a.length()
count := a.count() ; Arrays can be sparse.
mini := a.minIndex()
maxi := a.maxIndex()

; Loop over array.
loop % a.length()
{
	MsgBox, % a[A_Index]
}

a.delete(1) ; Deletes element.  Does not shift existing.  Results in a sparse array.

contents := ""
for k, v in a {
	contents .= format("{1} => {2}`n", k, v)
}
MsgBox %contents%


ExitApp


; Joins strings together.
; There is no builtin StrJoin() or Array.join(), surprisingly.
join(sep, params*) {
	for index, param in params
		str .= param . sep
	return SubStr(str, 1, -StrLen(sep))
}


