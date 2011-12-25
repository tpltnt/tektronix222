Feature: Use serial port
	In order to use the code
	the USB serial port should be used


	Scenario: Open with given serial port
		Given there is a working serial port
		When the object is initialized
		Then it should open the given serial port

	Scenario: Disconnect oscilloscope
		Given there is an initialized object
		When the oscilloscope is disconnected
		Then the serial port should be closed

	Scenario: Unplug oscilloscope
		Given there is an initialized object
		When the oscilloscope is unplugged
		Then an exception should be raised
