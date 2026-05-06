#Requires AutoHotkey v2.0

s := "" ; empty string
s := "this is a string literal"
s := 'so is this' ; no special meaning
s := "a string with `"quotes`" in it"

s := "concatenate " . "strings together"
s := "implicitly concat " "strings together"

length := StrLen(s)

; Get a substring: SubStr(<string>, <start index>, <substring length>)
ss := SubStr(s, 1, 3) ; "imp"

s := "  extra whitespace   "
s := Trim(s) ; trim off the extra whitespace

; Split string.
; 3rd arg is chars to omit from either side of fragment (so, it's like a trim).
s := "some, delimited, text."
fragments := StrSplit(s, ",", " .")
MsgBox(fragments[3]) ; should be just "text"

; Convert single char to Unicode code point integer and back.
code_point := Ord("t")
character := Chr(code_point)

; Formatting placeholders are {<arg position>:<format specifier>}.
; If no arg pos given, {} are just replaced in order of appearance.
a := "string formatting"
b := "hello"
s := Format("{2} {1}", a, b)

x := 17
s := Format("The number is {:d}.", x)
MsgBox(s)

