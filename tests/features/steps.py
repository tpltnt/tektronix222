from lettuce import *
import sys
sys.path.append('../../tektronix222/')
from tek222 import Tek222

@step(u'Given there is a working serial port')
def given_there_is_no_file_named(step):
	assert True, 'yay!'

@step(u'When the object is initialized')
def when_the_object_is_initialized(step):
	world.scope = Tek222('/dev/ttyU0')
	assert 'Tek222' in str(world.scope.__class__), "object initialized %s" % world.scope.__class__

@step(u'Then it should open the given serial port')
def then_it_should_open_the_first_file(step):
	currentport = world.scope.portstr
	assert '/dev/' in currentport, "first port taken %s" % currentport

@step(u'Given there is an initialized object')
def given_there_is_an_initialized_object(step):
    assert 'Tek222' in str(world.scope.__class__), "object initialized %s" % world.scope.__class__

@step(u'When the oscilloscope is disconnected')
def when_the_oscilloscope_is_disconnected(step):
    assert world.scope.disconnect, 'scope connection closed'

@step(u'Then the serial port should be closed')
def then_the_serial_port_should_be_closed(step):
    assert None == world.scope.portstr , 'portstring after disconnect %s' % world.scope.portstr

@step(u'When the oscilloscope is unplugged')
def when_the_oscilloscope_is_unplugged(step):
    assert False, 'This step must be implemented'

@step(u'Then an exception should be raised')
def then_an_exception_should_be_raised(step):
    assert False, 'This step must be implemented'
