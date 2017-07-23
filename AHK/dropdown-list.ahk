; Makes the insert key pop up a dropdown list.
Ins::
	Gui, Font, s12, Arial
	; vSelection => global var 'Selection' will contain the selected string.
	; gHandler => label 'Handler' will be jumped to when a list item is selected.
	; | separates the items in the list.
	Gui, Add, DropDownList, w275 vSelection gHandler, Eat|Sleep|Play Guitar|Read a Book 
	Gui, Show, w300 h40, Do Something
return


; Handles a selection from the dropdown list (set up via the gHandler option).
Handler: 
    Gui, Submit, NoHide
    MsgBox, You have chosen to %Selection%.
return


; This label is created by AHK.  Handles closing of the GUI.
GuiClose:
	Gui, Destroy
return


