' Native silent launcher; canonical lifecycle entrypoint, not a legacy alias.
' Codex | GPT-6 | 2026-09-20
Option Explicit
Dim shell, fs, command, code
Set shell = CreateObject("WScript.Shell")
Set fs = CreateObject("Scripting.FileSystemObject")
command = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File """ & fs.BuildPath(fs.GetParentFolderName(WScript.ScriptFullName), "sync.ps1") & """"
code = shell.Run(command, 0, True)
WScript.Quit code
