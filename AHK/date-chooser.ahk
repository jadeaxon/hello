; Pops up a calendar widget when <Ctrl + Win d> pressed.
#^d::
	Gui, Add, MonthCal, vDayPick ; Add a MonthCal widget named 'DayPick'.
	Gui, Add, Button, Default, Submit ; Add a submit button.	
	Gui, Show ; Display the GUI.
return

; Responds to submit button.  Emits selected date as text.
ButtonSubmit:
	Gui, Submit
	FormatTime, DayPick, %DayPick%, MMMM d, yyyy
	Send, %DayPick%
	Gui, Destroy
return


