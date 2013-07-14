Moteino Wireless Programming library
=======

 * Library for facilitating wireless programming using RFM12B/RFM69 transceivers (get libraries here: [RFM12B](https://github.com/LowPowerLab/RFM12B) and [RFM69](https://github.com/LowPowerLab/RFM69))
 * and the SPI Flash memory library for arduino/moteino (get library here: [SPIFlash](http://github.com/LowPowerLab/SPIFlash))
 * DEPENDS ON the two libraries mentioned above
 * Install all three of these libraries in your Arduino/libraries folder ([Arduino > Preferences] for location of Arduino folder)
 
 You will need a Moteino loaded with DualOptiboot bootloader (they all come with it except some early units).
 Depending which Moteino revision it is install the library you need in your Arduino/libraries folder:
 - for Moteino R2 (RFM12B transceiver) - copy WirelessHEX
 - for Moteino R3 (RFM69W/RFM69HW transceiver) - copy WirelessHEX69
 
 Examples for how to wirelessly program Moteino are found under the RFM12B and RFM69 libraries.