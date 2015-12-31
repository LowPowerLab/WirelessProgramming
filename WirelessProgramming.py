#**********************************************************************************
# This script will handle the transmission of a compiled sketch in the
# form of an INTEL HEX flash image to an attached gateway/master Moteino node,
# for further wireless transmission to a target Moteino node that will receive it de-HEXified and
# store it in external memory. Once received by the target (which is also loaded with a custom bootloader
# capable of reading back that image) it will reset and reprogram itself with the new sketch
#
# EXAMPLE command line: python WirelessProgramming.py -f PathToFile.hex -s COM100 -t 123
# where -t is the target ID of the Moteino you are programming
# and -s is the serial port of the programmer Moteino (on linux/osx it is something like ttyAMA0)
# To get the .hex file path go to Arduino>file>preferences and check the verbosity for compilation
#   then you will get the path in the debug status area once the sketch compiles
#**********************************************************************************
# Copyright Felix Rusu, LowPowerLab.com
# Library and code by Felix Rusu - felix@lowpowerlab.com
#**********************************************************************************
# License
#**********************************************************************************
# This program is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General    
# Public License as published by the Free Software       
# Foundation; either version 3 of the License, or        
# (at your option) any later version.                    
#                                                        
# This program is distributed in the hope that it will   
# be useful, but WITHOUT ANY WARRANTY; without even the  
# implied warranty of MERCHANTABILITY or FITNESS FOR A   
# PARTICULAR PURPOSE. See the GNU General Public        
# License for more details.                              
#                                                        
# You should have received a copy of the GNU General    
# Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#                                                        
# Licence can be viewed at                               
# http://www.gnu.org/licenses/gpl-3.0.txt
#
# Please maintain this license information along with authorship
# and copyright notices in any redistribution of this code
# **********************************************************************************
import time, sys, serial
import collections
import re

### GENERAL SETTINGS ###
SERIALPORT = "COM101"  # the default com/serial port the receiver is connected to
BAUDRATE = 115200      # default baud rate we talk to Moteino
TARGET=0
DEBUG = False
HEX = "flash.hex"
retries = 2

# Read command line arguments
if (sys.argv and len(sys.argv) > 1):
  if len(sys.argv)==2 and (sys.argv[1] == "-h" or sys.argv[1] == "-help" or sys.argv[1] == "?"):
    #print " -d or -debug         Turn debugging ON (verbose output)"
    print " -f or -file          HEX file to upload (Default: ", HEX, ")"
    print " -t or -target {ID}   Specify WirelessProgramming node target"
    print " -s or -serial {port} Specify serial port of WirelessProgramming gateway (Default: ", SERIALPORT, ")"
    print " -b or -baud {baud}   Specify serial port baud rate (Default: ", BAUDRATE, ")"
    print " -h or -help or ?     Print this message"
    exit(0)
    
  for i in range(len(sys.argv)):
    #if sys.argv[i] == "-d" or sys.argv[i] == "-debug":
    #  DEBUG = True
    if (sys.argv[i] == "-s" or sys.argv[i] == "-serial") and len(sys.argv) >= i+2:
      SERIALPORT = sys.argv[i+1]
    if (sys.argv[i] == "-b" or sys.argv[i] == "-baud") and len(sys.argv) >= i+2:
      BAUD = sys.argv[i+1]
    if (sys.argv[i] == "-f" or sys.argv[i] == "-file") and len(sys.argv) >= i+2:
      HEX = sys.argv[i+1].strip()
    if (sys.argv[i] == "-t" or sys.argv[i] == "-target") and len(sys.argv) >= i+2:
      if sys.argv[i+1].isdigit() and int(sys.argv[i+1])>0 and int(sys.argv[i+1])<=255:
        TARGET = int(sys.argv[i+1])
      else:
        print "TARGET invalid  (", sys.argv[i+1], "), must be 1-255."
        exit(1)

def millis():
  return int(round(time.time() * 1000)) 

def waitForHandshake(isEOF=False):
  now = millis()
  while True:
    if millis()-now < 4000:
      if isEOF:
        ser.write("FLX?EOF" + '\n')
      else:
        ser.write("FLX?" + '\n')
        print "FLX?\n"
      ser.flush()
      rx = ser.readline().rstrip()
      if len(rx) > 0:
        print "Moteino: [" + rx + "]"
        if rx == "FLX?OK":
          print "HANDSHAKE OK!"
          return True
        elif rx == "FLX?NOK":
          print "HANDSHAKE NOK [IMG REFUSED BY TARGET]"
          return False
    else: return False

def waitForTargetSet(targetNode):
  now = millis()
  to = "TO:" + str(TARGET)
  print to
  ser.write(to + '\n')
  ser.flush()
  while True:
    if millis()-now < 3000:
      rx = ser.readline().rstrip()
      if len(rx) > 0:
        print "Moteino: [" + rx + "]"
        if rx == to + ":OK":
          return True
        else: return False
  return False
    
# return 0:timeout, 1:OK!, 2:match but out of synch
def waitForSEQ(seq):
  now = millis()
  while True:
    if millis()-now < 3000:
      rx = ser.readline()
      if len(rx) > 0:
        rx = rx.strip()
        print "Moteino: " + rx
        result = re.match("FLX:([0-9]*):OK", rx)
        if result != None:
          if int(result.group(1)) == seq:
            return 1
          else: return 2
    else: return False

    
# MAIN()
if __name__ == "__main__":
  try:
    # open up the FTDI serial port to get data transmitted to Moteino
    ser = serial.Serial(SERIALPORT, BAUDRATE, timeout=1) #timeout=0 means nonblocking
    time.sleep(2) #wait for Moteino reset after port open and potential bootloader time (~1.6s) 
    ser.flushInput();
  except IOError as e:
    print "COM Port [", SERIALPORT, "] not found, exiting..."
    exit(1)
  
  try:
    if not 0<TARGET<= 255:
      print "TARGET not provided (use -h for help), now exiting..."
      exit(1)
    
    #send target ID first
    if waitForTargetSet(TARGET):
      print "TARGET SET OK"
    else:
      print "TARGET SET FAIL, exiting..."
      exit(1)
    
    with open(HEX) as f:
      print "File found, passing to Moteino..."
      
      if waitForHandshake():
        seq = 0
        content = f.readlines()

        while seq < len(content):
          tx = "FLX:" + str(seq) + content[seq].strip()
          isEOF = (content[seq].strip() == ":00000001FF") #this should be the last line in any valid intel HEX file
          
          if isEOF==False:
            print "TX > " + tx
            ser.write(tx + '\n')
            result = waitForSEQ(seq)
          elif waitForHandshake(True):
            print "SUCCESS!"
            exit(0);
          else:
            print "FAIL, IMG REFUSED BY TARGET (size exceeded? verify target MCU matches compiled target)"
            exit(99);

          if result == 1: seq+=1
          elif result == 2: continue # out of synch, retry
          else:
            if retries > 0:
              retries-=1
              print "Timeout, retry...\n"
              continue
            else:
              print "TIMEOUT, aborting..."
              exit(1);

        while 1:
          rx = ser.readline()
          if (len(rx) > 0): print rx.strip()
      else:
        print "No response from Moteino, exiting..."
        exit(1);

  except IOError:
    print "File [", HEX, "] not found, exiting..."