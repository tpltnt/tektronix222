Feature: Use serial port
	In order to use the code
	the USB device file should be used


	Scenario: Open without devicefile given
		Given there is no file named
		When the object is initialized
		Then it should open the first file

	Scenario: Disconnect oscilloscope
		Given there is an initialized object
		When the oscilloscope is disconnected
		Then the serial port should be closed

	Scenario: Unplug oscilloscope
		Given there is an initialized object
		When the oscilloscope is unplugged
		Then an exception should be raised
