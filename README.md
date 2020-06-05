![GUI v2.0](https://raw.githubusercontent.com/LowPowerLab/WirelessProgramming/master/OTAGUI_v2.png)
# Wireless Programming GUI for Moteinos (aka OTA programming)

## Note: This repository used to reside in the [RFM69 library](https://github.com/LowPowerLab/RFM69/tree/master/Examples/WirelessProgramming_OTA).

## v2.0 Changes
- various bugs fixed
- support for on-the-fly change of Programmer RF settings: **networkID**, **nodeID**, **frequency** (in Hz), **EncryptionKey** (either blank for no encryption, or 16-character key), **BitRate** (either default or 300KBPS). Existing RF Settings can also be read from the OTA Programmer.
- Note: for the settings feature to work, the laest [OTA Programmer sketch](https://github.com/LowPowerLab/RFM69/blob/master/Examples/WirelessProgramming_OTA/Programmer/Programmer.ino) is required
- UI no longer locks during transfer, window can be moved, log can be cleared at any time
- ability to CANCEL a transfer
- ability to refresh the COM ports dropdown
- updated instructions
- backward compatible with older programmer/target code

## v1.6 Changes
- various bugs fixed
- protocol improved to support variable HEX record length
- removed the delay logging since it was causing some glitching

## v1.5 Changes
Since v1.5 you can now run this app in several ways:
- natively via the WirelessProgramming.exe GUI app
- the windows GUI can also invoke the OTA.py script via embedded IronPython engine (parameters from GUI pass to the OTA.py script)
- cross platform straight from Python (2.7 runtime) by supplying parameters (run `python OTA.py -h` for details)
<br/>
You must download pythonLibs.zip and OTA.py and place them in the same directory as WirelessProgramming.exe if you plan to run the protocol via the OTA.py script.
You may need to download the entire repository as a ZIP file.
