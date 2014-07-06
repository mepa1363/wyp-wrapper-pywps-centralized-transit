import urllib2
from types import *
from time import strftime
from pywps.Process import WPSProcess

class Process(WPSProcess):

    """Main process class"""
    def __init__(self):
        """Process initialization"""
        # init process
        WPSProcess.__init__(self,
            identifier = "Walkshed_Transit_Centralized", # must be same, as filename
            title="Walkshed WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for generating walkshed")

	self.fromPlace = self.addLiteralInput(identifier="StartPoint",
                    title = "Walking start point", type=StringType)	

	self.walkTime = self.addLiteralInput(identifier="WalkingPeriod",
                    title = "Walking time period", type=StringType)

	self.walkSpeed = self.addLiteralInput(identifier="WalkingSpeed",
                    title = "Walking speed", type=StringType)

	self.output = self.addLiteralInput(identifier="WalkshedOutput",
                    title = "Walkshed ouput", allowedValues=["SHED","EDGES","POINTS"], type=StringType)

	self.walkshedResult = self.addLiteralOutput(identifier="WalkshedResult",
                title="Walkshed result", type=StringType)

    def execute(self):

	time = strftime("%Y-%m-%dT%H:%M:%S")

	otp_url = "http://gisciencegroup.ucalgary.ca:8080/opentripplanner-api-webapp/ws/iso?layers=traveltime&styles=mask&batch=true&fromPlace="+self.fromPlace.getValue()+"&toPlace=51.09098935,-113.95179705&time="+time+"&mode=WALK&maxWalkDistance=10000&walkTime="+self.walkTime.getValue()+"&walkSpeed="+self.walkSpeed.getValue()+"&output="+self.output.getValue()
	try:
		otp_data = urllib2.urlopen(otp_url).read()
		self.walkshedResult.setValue(otp_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
