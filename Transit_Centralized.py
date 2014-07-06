import urllib2
from types import *
from pywps.Process import WPSProcess

class Process(WPSProcess):

    """Main process class"""
    def __init__(self):
        """Process initialization"""
        # init process
        WPSProcess.__init__(self,
            identifier = "Transit_Centralized", # must be same, as filename
            title="Transit WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for generating transit data")

	self.start_time = self.addLiteralInput(identifier="StartTime",
                    title = "Walking start time", type=StringType)

	self.walkshed = self.addLiteralInput(identifier="Walkshed",
                    title = "walkshed polygon", type=StringType)

	self.walking_time_period = self.addLiteralInput(identifier="WalkingTime",
                    title = "Walking time period", type=StringType)

	self.walking_speed = self.addLiteralInput(identifier="WalkingSpeed",
                    title = "Walking speed", type=StringType)

	self.bus_waiting_time = self.addLiteralInput(identifier="BusWaitingTime",
                    title = "bus waiting time", type=StringType)

	self.bus_ride_time = self.addLiteralInput(identifier="BusRideTime",
                    title = "bus ride time", type=StringType)

	self.transitResult = self.addLiteralOutput(identifier="TransitResult",
                title="transit data", type=StringType)

    def execute(self):

	start_time = self.start_time.getValue()
	walkshed = self.walkshed.getValue()
	walking_time_period = self.walking_time_period.getValue()
	walking_speed = self.walking_speed.getValue()
	bus_waiting_time = self.bus_waiting_time.getValue()
	bus_ride_time = self.bus_ride_time.getValue()
	

	transit_url = "http://127.0.0.1:9367/transit?start_time="+start_time+"&walkshed="+walkshed+"&walking_time_period="+walking_time_period+"&walking_speed="+walking_speed+"&bus_waiting_time="+bus_waiting_time+"&bus_ride_time="+bus_ride_time

	try:
		transit_data = urllib2.urlopen(transit_url).read()
		self.transitResult.setValue(transit_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
