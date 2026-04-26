#Requires AutoHotkey v2.0
#SingleInstance Force

; TaiLoTyper MVP (robust file-to-file version)
; Select tone-number Tai-lo text, then press Ctrl+Alt+T.

^!t::
{
    oldClipboard := A_Clipboard
    A_Clipboard := ""

    Send "^c"

    if !ClipWait(2) {
        MsgBox "No text selected, or clipboard copy failed."
        A_Clipboard := oldClipboard
        return
    }

    selectedText := A_Clipboard

    pythonExe := "C:\Users\tommy\tailo-typer\.venv\Scripts\python.exe"
    scriptPath := "C:\Users\tommy\tailo-typer\src\tailo_converter.py"

    tempInput := A_Temp "\tailo_input.txt"
    tempOutput := A_Temp "\tailo_output.txt"

    try FileDelete(tempInput)
    try FileDelete(tempOutput)

    ; Write selected text as UTF-8
    FileAppend(selectedText, tempInput, "UTF-8")

    command := Format(
        '"{}" "{}" --file "{}" --out "{}"',
        pythonExe,
        scriptPath,
        tempInput,
        tempOutput
    )

    RunWait(command, , "Hide")

    if !FileExist(tempOutput) {
        MsgBox "Conversion failed: no output file was created.`n`nCommand:`n" command
        A_Clipboard := oldClipboard
        return
    }

    ; Read UTF-8 output explicitly
    convertedText := FileRead(tempOutput, "UTF-8")

    ; Remove BOM if present
    convertedText := RegExReplace(convertedText, "^\x{FEFF}")

    ; Trim final line breaks
    convertedText := RTrim(convertedText, "`r`n")

    if (convertedText = "") {
        MsgBox "Conversion returned empty output."
        A_Clipboard := oldClipboard
        return
    }

    A_Clipboard := convertedText
    Sleep 200
    Send "^v"
    Sleep 200

    A_Clipboard := oldClipboard
}