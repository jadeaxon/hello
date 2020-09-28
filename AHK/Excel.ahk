; Use COM in AHK to automate Excel.
; This actually works.

excel := ComObjCreate("Excel.Application") ; Get handle for Excel application COM object.

workbook := excel.workbooks.open(A_Desktop . "\Test.xlsx")
excel.visible := true

WinMaximize, ahk_exe EXCEL.EXE

; This works, but there is a simpler way below.
; worksheet := ComObjActive("Excel.Application") ; Get handle for the active worksheet.
worksheet := workbook.activeSheet
ws := worksheet

ws.range("A1").value := ""
ws.range("A2").value := ""

ws.range("A1").value := "Hello, Excel!"
value := ws.range("A1").value
ws.range("A2").value := value . " (copy)"

; Copy range to clipboard.
; clipboard := ws.range("A2").value ; Copy to clipboard.
ws.range("A2").copy

; Cell addressing is (row, column) 1-based.
ws.cells(2, 2) := "cell value"

; Set a column to use the first 32 colors in the color index.
Loop, 32
{
	ws.cells(A_Index, 3).interior.colorIndex := A_Index
	ws.cells(A_Index, 4).value := "delete me"
	ws.cells(A_Index, 5).value := "column E"
}

; Delete column D.
; ws.range("D").delete ; ERROR
ws.range("D:D").delete

; Delete row 2.
; ws.range("2").delete ; ERROR
ws.range("2:2").delete

; Insert a row above row 1.
ws.rows("1:1").insert

; Insert a column to the left of column A.
ws.columns("A:A").insert

workbook.save()



