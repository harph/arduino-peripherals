Arduino Peripherals
====


Arduino demo about how to build Arduino-based peripheral devices.


## Installation

To install the Python requirements run the following commands inside the project folder:

	cd <PATH_TO_PERIPHERALS_PROJECT>
	virtual env --system-site-packages
	source env/bin/activate
	pip install -r requirements.txt
	
## Running The Project

The first thing you have to do is upload the Arduino Sketch to the board. For this open the following file *src/arduino/peripherals/peripherals.ino* using the Arduino IDE. Connect the Arduino to the computer and upload the Sketch. Let the Arduino connected, after all it should be connected somehow to the computer if is going to be a peripheral (I know, Bluetooth is another option but we are not talking about that right now).

Now, it's time to run the Python program. This program is in-charge of handling the interaction with the Arduino. To run the program execute the following commands:

	cd <PATH_TO_PERIPHERALS_PROJECT>
	source env/bin/activate
	cd src/python
	python peripherals.py
