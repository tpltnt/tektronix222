#!/usr/bin/env python

class Tek222:

	def __init__(self):
		__title__ = 'tek222'
		__version__ = '0.0.1'
		__author__ = 'tpltnt'
		__license__ = 'ISC'
		__copyright__ = 'Copyright 2011 tpltnt'
		self.usbdevice = '/dev/ttyUSB0'

	def get_serial_port(self):
		return self.usbdevice
