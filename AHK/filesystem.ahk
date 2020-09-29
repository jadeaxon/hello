
#Warn
#NoEnv
#SingleInstance Force

; Copy files.
; FileCopy, <source glob>, <dest dir>, <overwrite: 0 or 1>
; <dest dir> is A_WorkingDir by default.
; Copy this script to the temp dir.
FileCopy, %A_ScriptFullPath%, %A_Temp%, 1
tempFile := A_Temp . "\" . A_ScriptName
if (FileExist(tempFile)) {
	MsgBox, Copy successful!
}

; Delete files.
; FileDelete, <glob>
FileDelete, %tempFile%
if (not FileExist(tempFile)) {
	MsgBox, Delete successful!
}



