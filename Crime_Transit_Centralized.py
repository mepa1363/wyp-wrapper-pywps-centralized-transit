import urllib2
from types import *
from pywps.Process import WPSProcess

class Process(WPSProcess):

    """Main process class"""
    def __init__(self):
        """Process initialization"""
        # init process
        WPSProcess.__init__(self,
            identifier = "Crime_Transit_Centralized", # must be same, as filename
            title="Crime WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for retrieving crime data")

	self.walkshed = self.addLiteralInput(identifier="Walkshed",
                    title = "Walkshed polygon", type=StringType)	
	
	self.crimeResult = self.addLiteralOutput(identifier="CrimeDataResult",
                title="Crime data result", type=StringType)

    def execute(self):

	crime_service_url = "http://127.0.0.1:9366/crime?walkshed="+urllib2.quote(self.walkshed.getValue())
	

	try:
		crime_data = urllib2.urlopen(crime_service_url).read()
		self.crimeResult.setValue(crime_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
