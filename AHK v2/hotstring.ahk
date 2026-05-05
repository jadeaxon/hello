#Requires AutoHotkey v2.0

; Simple hotstring on the same line.
; When you type 'brb' it will be expanded to 'be right back'
; By default, you have to follow the hotstring by space or enter before it triggers.
::brb::be right back

; A hotstring can also trigger arbitrary code to run.
::mbox::
{
	MsgBox("Message box summoned by hotstring")
}





