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
	assert 'Tek222' in str(world.scope.__class__), "object initialized %s" % world.scope.__class__

@step(u'Then it should open the first file')
def then_it_should_open_the_first_file(step):
	currentport = world.scope.serialport
    assert '/dev/ttyUSB0' == currentport, "first port taken"

