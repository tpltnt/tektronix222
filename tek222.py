#!/usr/bin/env python

"""
Copyright (c) 2011, tpltnt
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of tpltnt nor the
      names of his contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL TPLTNT BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import serial

class Tek222(object):
	"""This is a class for interfacing to the Tektronix 222 oscilloscope.

	It uses FTDI-based USB to serial converters and pySerial for
	communication, since drivers should be readily available.
	"""
	
	def __init__(self,portstring):
		__title__ = 'tek222'
		__version__ = '0.0.1'
		__author__ = 'tpltnt'
		__license__ = 'Modified BSD License'
		__copyright__ = 'Copyright 2011 tpltnt'
		
		# list of buttons
		self.button = {	'CLEAR' : '1',
						'Menu Item 0' : '2',
						'Menu Item 1' : '3',
						'Menu Item 2' : '4',
						'Menu Item 3' : '5',
						'OFF' : '6',
						'Trigger SOURCE' : '9',
						'Trigger MODE' : 'A',
						'Trigger SLOPE' : 'B',
						'CH2 SELECT' : 'C',
						'CH1 SELECT' : 'D',
						'AUTO SETUP' : 'E',
						'Front-Panel Setup Menu' : '11',
						'Trigger Position Menu' : '12',
						'Auxiliary Functions Menu' : '13',
						'Display Mode Menu' : '14',
						'Save Waveform Menu' : '19',
						'Recall Waveform Menu' : '1A',
						'STORE/NONSTORE' : '1B',
						'Acq Mode Menu' : '1C',
						'X10 Mag' : '20',
						'Variable Gain' : '21',
						'AUTO LVL:PUSH' : '22'}
		try:
			self.portstr = portstring
			"""
			RS232 parameters:
			startbit: 1
			stopbit: 1
			parity: none
			flowcontrol: xon/xoff
			data: 8bit
			rates: 300, 1200, 2400, 9600
			"""
			__serialport__ = serial.Serial(self.portstr, 9600, timeout=None, xonxoff=1)

		except serial.SerialException:
			self.portstr = None
			raise

	def press_button(buttoncode):
		"""simulates pressing a button. returns number of bytes written."""
		return __serialport__.write("BUT %s\r", buttoncode)
		
	def disconnect():
		""" Disconnect the serial port."""
		return __serialport__.close
	
	def close():
		""" alias for disconnect() """
		return self.disconnect
