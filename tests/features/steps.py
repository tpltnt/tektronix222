from lettuce import *
import sys
sys.path.append('../../tektronix222/')
from tek222 import Tek222

@step(u'Given there is no file named')
def given_there_is_no_file_named(step):
	assert True, 'yay!'

@step(u'When the object is initialized')
def when_the_object_is_initialized(step):
	world.scope = Tek222()
	assert world.scope, "object initialized %d" % world.scope

@step(u'Then it should open the first file')
def then_it_should_open_the_first_file(step):
	currentdevice = world.scope.get_serial_port()
        if '/dev/ttyUSB0' == currentdevice :
                assert True, 'yay!'
        else:
                assert False, 'not first device'
