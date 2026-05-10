#Requires AutoHotkey v2.0

; You can create objects on the fly.
o := {name: "Jimmy", age: 37, nickname: "The Hand"}

o.name := "Johnny"

o.gold := 520 ; You can add new properties.

message := Format("{} '{}' has {} gold.", o.name, o.nickname, o.gold)
MsgBox(message)


