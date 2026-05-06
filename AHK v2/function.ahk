#Requires AutoHotkey v2.0

my_function() {
	; The T1 arg times out the message box in 2 seconds.
	MsgBox("Hello, functions!", "Message", "T2")
}

my_second_function(greeting) {
	MsgBox(greeting . ", functions!", "Message", "T2")

}

; A function can have parameters and return a value.
add(x, y) {
	r := x + y
	return r
}
sum := add(1, 2)

my_function()
my_second_function("Hi")


