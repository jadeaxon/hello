; Run this with /cygdrive/c/Program\ Files/AutoHotkey/AutoHotkey.exe stdout.ahk.
; AHK isn't really intended for making command line scripts, but it is possible.

SCITE_CHECK := false

print("Hello, AHK!")
return


;==============================================================================
; Functions
;==============================================================================

; Prints to console (stdout).
; SCITE_CHECK reduces stdout/stdin performance, so only enable if needed.
print(output:="") {	
	global ___console___
	global SCITE_CHECK

	; If script parent is scite,output to scite console & return.
	if (SCITE_CHECK && processExists("SciTE.exe") && getParentProcessName() = "SciTE.exe") {	
		FileAppend, %output%`n, *
		return
	}																												
	
	; CONOUT$ is a special file windows uses to expose attached console output
	( output ? ( !___console___? (DllCall("AttachConsole", "int", -1) 
	|| DllCall("AllocConsole")) 
	& (___console___:= true) : "" ) 
	& FileAppend(output . "`n","CONOUT$") 
	: DllCall("FreeConsole") & (___console___:= false) & StdExit() )
}


; Display prompt on console and wait for input.  Returns input.
prompt(output:="") {	
	global ___console___
	global SCITE_CHECK
	
	if (SCITE_CHECK && processExists("SciTE.exe") && getParentProcessName() = "SciTE.exe"){	;if script parent is scite,output to scite console & return
		FileAppend, %output%`n, *
		return
	}
	
	( output ? ( !___console___? (DllCall("AttachConsole", "int", -1) 
	|| DllCall("AllocConsole")) & (___console___:= true) : "" ) 
	& FileAppend(output . "`n","CONOUT$") 
	& (Stdin := FileReadLine("CONIN$",1)) 
	: DllCall("FreeConsole") & (___console___:= false) & StdExit() )
	Return Stdin
}


; Not sure exactly what this does.
StdExit() {
	; Couldn't get this: 'DllCall("GenerateConsoleCtrlEvent", CTRL_C_EVENT, 0)' to work so...
	If getParentProcessName() = "cmd.exe"		
		ControlSend, , {Enter}, % "ahk_pid " . getPPID(getPID())
}

; Appends given string to a file.
FileAppend(str, file) {
	FileAppend, %str%, %file%
}

; Reads a line from a file.
FileReadLine(file, lineNum) {
	FileReadLine, retVal, %file%, %lineNum%
	return retVal
}

; Does the given process (by name) exist?
processExists(procName) {
	Process, Exist, % procName
	Return ErrorLevel
}

; Returns the name of the parent process of this process.
getParentProcessName() {
	return getProcessName(getPPID(getPID()))
}

; Gets the parent process pid for the given pid.
getPPID(pid) {
	static function := DllCall("GetProcAddress", "ptr", DllCall("GetModuleHandle", "str", "kernel32.dll", "ptr"), "astr", "Process32Next" (A_IsUnicode ? "W" : ""), "ptr")
	if !(h := DllCall("CreateToolhelp32Snapshot", "uint", 2, "uint", 0))
		return
	VarSetCapacity(pEntry, sz := (A_PtrSize = 8 ? 48 : 36)+(A_IsUnicode ? 520 : 260))
	Numput(sz, pEntry, 0, "uint")
	DllCall("Process32First" (A_IsUnicode ? "W" : ""), "ptr", h, "ptr", &pEntry)
	loop
	{
		if (pid = NumGet(pEntry, 8, "uint") || !DllCall(function, "ptr", h, "ptr", &pEntry))
			break
	}
	DllCall("CloseHandle", "ptr", h)
	return Numget(pEntry, 16+2*A_PtrSize, "uint")
}

; Gets the process name for the given pid.
getProcessName(pid) {
	static function := DllCall("GetProcAddress", "ptr", DllCall("GetModuleHandle", "str", "kernel32.dll", "ptr"), "astr", "Process32Next" (A_IsUnicode ? "W" : ""), "ptr")
	if !(h := DllCall("CreateToolhelp32Snapshot", "uint", 2, "uint", 0))
		return
	VarSetCapacity(pEntry, sz := (A_PtrSize = 8 ? 48 : 36)+260*(A_IsUnicode ? 2 : 1))
	Numput(sz, pEntry, 0, "uint")
	DllCall("Process32First" (A_IsUnicode ? "W" : ""), "ptr", h, "ptr", &pEntry)
	loop
	{
		if (pid = NumGet(pEntry, 8, "uint") || !DllCall(function, "ptr", h, "ptr", &pEntry))
			break
	}
	DllCall("CloseHandle", "ptr", h)
	return StrGet(&pEntry+28+2*A_PtrSize, A_IsUnicode ? "utf-16" : "utf-8")
}

; Gets the pid of this process.
getPID() {
	return DllCall("GetCurrentProcessId")
}



