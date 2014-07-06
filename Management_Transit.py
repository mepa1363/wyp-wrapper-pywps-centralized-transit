import urllib2
from types import *
from pywps.Process import WPSProcess

class Process(WPSProcess):

    """Main process class"""
    def __init__(self):
        """Process initialization"""
        # init process
        WPSProcess.__init__(self,
            identifier = "Management_Transit", # must be same, as filename
            title="Management WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for generating walkshed")

	self.start_point = self.addLiteralInput(identifier="StartPoint",
                    title = "Walking start point", type=StringType)

	self.start_time = self.addLiteralInput(identifier="StartTime",
                    title = "Walking start time", type=StringType)	

	self.walking_time_period = self.addLiteralInput(identifier="WalkingTimePeriod",
                    title = "Walking time period", type=StringType)

	self.walking_speed = self.addLiteralInput(identifier="WalkingSpeed",
                    title = "Walking speed", type=StringType)

	self.bus_waiting_time = self.addLiteralInput(identifier="BusWaitingTime",
                    title = "bus waiting time", type=StringType)

	self.bus_ride_time = self.addLiteralInput(identifier="BusRideTime",
                    title = "bus ride time", type=StringType)

	self.distance_decay_function = self.addLiteralInput(identifier="DistanceDecayFunction",
                    title = "use distance decay function or not", type=StringType)

	self.walkScore = self.addLiteralOutput(identifier="AccessiblityScore",
                title="accessiblity score", type=StringType)

    def execute(self):

	start_point = self.start_point.getValue()
	start_time = self.start_time.getValue()
	walking_time_period = self.walking_time_period.getValue()
	walking_speed = self.walking_speed.getValue()
	bus_waiting_time = self.bus_waiting_time.getValue()
	bus_ride_time = self.bus_ride_time.getValue()
	distance_decay_function = self.distance_decay_function.getValue()

	management_url = "http://127.0.0.1:9363/management?start_point="+start_point+"&start_time="+start_time+"&walking_time_period="+walking_time_period+"&walking_speed="+walking_speed+"&bus_waiting_time="+bus_waiting_time+"&bus_ride_time="+bus_ride_time+"&distance_decay_function="+distance_decay_function

	try:
		walkscore_data = urllib2.urlopen(management_url).read()
		self.walkScore.setValue(walkscore_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
