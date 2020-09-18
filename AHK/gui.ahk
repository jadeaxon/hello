; ===============================================================================
; Autoexecute 
; ===============================================================================

; Nothing autoexecutes after the first hotkey is defined.

; Add a menu item to the tray icon.
Menu, Tray, Add, blah blah, CustomTrayMenuItem


; ===============================================================================
; Hotkeys
; ===============================================================================

; Makes the insert key pop up a GUI.
Ins::
	Gui, Font, s12, Arial

	; Add a text input field.
	Gui, Add, Edit, vUserInput
	
	; Add a button.
	; g means goto.  It prefixes the label name.  
	Gui, Add, Button, default gSearch, Search

	Gui, Show
return


; ===============================================================================
; Subroutines 
; ===============================================================================

; Referenced by gSearch.
Search:

return

; This label is created by AHK.  Handles closing of the GUI.
; Like when user press Esc or hits the red X.
GuiClose:
	Gui, Destroy
return


CustomTrayMenuItem:
	MsgBox, Tray Menu Item
return



