; The point of this script is to filter selected text in various ways.
; Basically, you copy whatever text is selected to the clipboard.  Then
; alter it in some way.  Then paste it back.
;
; One example is converting text to lowercase.
;
; TO DO: Mod these to work in gVim since it does not use standard copy/paste/type-over-selected
; mechanics.

; Convert selection to uppercase.
^u::
	Clipboard := "" ; Clear the clipboard.
	Send, ^c ; Copy selection.
	ClipWait ; Wait for clipboard to settle.
	StringUpper Clipboard, Clipboard ; Convert clipboard text to uppercase.
	Send %Clipboard% ; Type back out the modified clipboard contents.
return


; Convert selection to lowercase.
^l::
	Clipboard := "" ; Clear the clipboard.
	Send, ^c ; Copy selection.
	ClipWait ; Wait for clipboard to settle.
	StringLower Clipboard, Clipboard ; Convert clipboard text to lowercase.
	Send %Clipboard% ; Type back out the modified clipboard contents.
return


; Convert selection to all words capitalized.
^k::
	Clipboard := "" ; Clear the clipboard.
	Send, ^c ; Copy selection.
	ClipWait ; Wait for clipboard to settle.
	StringUpper Clipboard, Clipboard, T ; Convert clipboard text.
	Send %Clipboard% ; Type back out the modified clipboard contents.
return


