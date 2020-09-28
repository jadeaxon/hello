; Use COM in AHK to automate Excel.
; This actually works.

excel := ComObjCreate("Excel.Application") ; Get handle for Excel application COM object.

workbook := excel.Workbooks.Open(A_Desktop . "\Test.xlsx")
excel.Visible := true

WinMaximize, ahk_exe EXCEL.EXE

worksheet := ComObjActive("Excel.Application") ; Get handle for the active worksheet.

worksheet.range("A1").value := "Hello, Excel!"

workbook.save()



