; ===============================================================================
; Autoexecute 
; ===============================================================================

; Nothing autoexecutes after the first hotkey is defined.

; Creates a popup menu of possible corrections.
createCorrectionMenu(pCorrections) {
	StringSplit, vMenuItems, pCorrections , `,
	Loop, %vMenuItems0% { 
		correction := vMenuItems%A_Index%
		Menu, CorrectionMenu, Add, %correction%, MenuAction
	}
	Menu, CorrectionMenu, Show
}


; ===============================================================================
; Hotstrings
; ===============================================================================

; Autocorrect misspelling with multiple possible choices.
; Pops up a menu with the various choices.
::agin::
	createCorrectionMenu("again,a gin,aging,agin")
return


; ===============================================================================
; Subroutines 
; ===============================================================================

MenuAction:
	; Send the name of the menu item that was activated.
	SendInput, %A_ThisMenuItem%
	Menu, CorrectionMenu, DeleteAll
return




