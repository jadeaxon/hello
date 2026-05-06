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

; You can call a function w/o ()s if it is the first thing on a line.
add 1, 2


; A function can have default args.
; This essentially turns them into optional parameters.
; You can have an optional parameter be unset.
; You can also just use <param>? instead of <param> := unset.
add_three(x, y := 3, save_to_file := unset) {
	r := x + y
	if IsSet(save_to_file) {
		; Note that blocks can be empty (unlike in Python where you need the pass nullop).
		; save result to given file
	}
	return r
}

; You can pass potentially unset vars to a function using ?.
add_three(5, not_sure_if_set?)

; You can return an array from a function.
; This might be better than using & for pass by ref to create output vars.
return_array() {
	return [1, 2, 3]
}


; You can have variadic functions.
join(separator, strings*) {
	for i, s in strings {
		; join the strings together
	}
	return "joined"
}

; Use * to unpack args into a variadic function from an iterable.
r := join("--", return_array()*)

g := "global var"
locals_and_globals() {
	; AHK v2 also has static variables.
	static times_called := 0
	times_called++

	; A function can have global vars.
	; If you need to assign to a global var, declare it as global (like in Python).
	; Like in Python, you can use the value of an unshadowed global without declaring it global.
	; But, you can't assign to a global without declaring it global.
	global g
	prefix := "hello " ; local var
	g .= prefix 
}

; Using an indirect var works for function calls.
func_name := "locals_and_globals"
%func_name%()

my_function()
my_second_function("Hi")


