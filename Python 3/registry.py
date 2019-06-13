#!/usr/bin/python3

# Open the Windows Registry key HKEY_LOCAL_MACHINE\SYSTEM\Keyboard Layout\Preload
# and lists all its values (as tuples: name, raw value, type).

# The default value is part of the key, not one of its entries.
# So, this only yields one entry for me.

# https://docs.python.org/3.0/library/winreg.html
# This came preinstalled for me.
import winreg

print('Hello, Windows Registry!')

hive = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

key_path = r'SYSTEM\Keyboard Layout\Preload'

key = winreg.OpenKey(hive, key_path)

i = 0
while True:
    try:
        entry = winreg.EnumValue(key, i)
        print(f'name: {entry[0]}')
        print(f'raw value: {entry[1]}')
        print(f'type: {entry[2]}')
        i += 1
    except EnvironmentError:
        break

key.Close()
hive.Close()


