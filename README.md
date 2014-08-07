Moteino Wireless Programming library
=======

 * Library for facilitating wireless programming using RFM12B/RFM69 transceivers (get libraries here: [RFM12B](https://github.com/LowPowerLab/RFM12B) and [RFM69](https://github.com/LowPowerLab/RFM69))
 * and the SPI Flash memory library for arduino/moteino (get library here: [SPIFlash](http://github.com/LowPowerLab/SPIFlash))
 * DEPENDS ON the two libraries mentioned above
 * Install all three of these libraries in your Arduino/libraries folder ([Arduino > Preferences] for location of Arduino folder)
 
 You will need a Moteino loaded with DualOptiboot bootloader (they all come with it except some early R1 units).
 Depending which Moteino revision it is install the library you need in your Arduino/libraries folder:
 - for Moteinos with RFM12B transceiver - use/copy WirelessHEX
 - for Moteinos with RFM69W/RFM69HW/RFM69CW transceivers - use/copy WirelessHEX69
 
 Examples for how to wirelessly program Moteino are found under the RFM12B and RFM69 libraries.

###License
Copyright (c) 2013 by Felix Rusu <felix@lowpowerlab.com>
<br/>
This library is free software; you can redistribute it and/or modify it under the terms of either the GNU General Public License version 2 or the GNU Lesser General Public License version 2.1, both as published by the Free Software Foundation.
<br/>
This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details
