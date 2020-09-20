#Persistent
#SingleInstance


:*:Astrings::
	; Split a string and type each piece out on a different line.
	s := "foo|bar|baz|qux"
	StringSplit, vFragments, s, |
	; vFragments0 is the length of the array.
	; Array indexing of this kind is 1-based.
	Loop, %vFragments0% {
		; This will loop from 1 .. length.
		fragment := vFragments%A_Index%
		SendInput, %A_Index%: %fragment%{enter}
	}
return

