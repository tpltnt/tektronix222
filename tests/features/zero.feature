Feature: Open serial port
	In order to use the code
	the USB device file should be used

	Scenario: Open without devicefile given
		Given there is no file named
		When the object is initialized
		Then it should open the first file
