#* ~~~ Obsolete ~~~ *
This library is obsolete and no longer supported. The Wireless Programming protocol was mergerd in the mainstream [RFM69 library](https://github.com/LowPowerLab/RFM69) and now known as **RFM69_OTA.h** - so replace/include that instead of **WirelessHEX69.h** in any new sketches. There are new [Programmer and Target examples](https://github.com/LowPowerLab/RFM69/tree/master/Examples/WirelessProgramming_OTA) in the main RFM69 lib as well.
<br>**WirelessProgramming.exe** has also been upgraded and included at the link above and the one in this directory is kept for reference but is no longer up to date to be used with the latest RFM69_OTA library.

##Moteino Wireless Programming library
 * Library for facilitating wireless programming using RFM12B/RFM69 transceivers (get libraries here: [RFM12B](https://github.com/LowPowerLab/RFM12B) and [RFM69](https://github.com/LowPowerLab/RFM69))
 * and the SPI Flash memory library for arduino/moteino (get library here: [SPIFlash](http://github.com/LowPowerLab/SPIFlash))
 * DEPENDS ON the two libraries mentioned above
 * Install all three of these libraries in your Arduino/libraries folder ([Arduino > Preferences] for location of Arduino folder)
 
 You will need a Moteino loaded with DualOptiboot bootloader (they all come with it except some early R1 units).
 Depending which Moteino revision it is install the library you need in your Arduino/libraries folder:
 - for Moteinos with RFM12B transceiver - use/copy WirelessHEX
 - for Moteinos with RFM69W/RFM69HW/RFM69CW transceivers - use/copy WirelessHEX69
 
 Examples for how to wirelessly program Moteino are found under the RFM12B and RFM69 libraries.

##License
GPL 3.0, please see the [License.txt](https://github.com/LowPowerLab/WirelessProgramming/blob/master/License.txt) file for details. Be sure to include the same license with any fork or redistribution of this library.
