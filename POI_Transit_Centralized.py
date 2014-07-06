import urllib2
from types import *
from pywps.Process import WPSProcess

class Process(WPSProcess):

    """Main process class"""
    def __init__(self):
        """Process initialization"""
        # init process
        WPSProcess.__init__(self,
            identifier = "POI_Transit_Centralized", # must be same, as filename
            title="POI WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for retrieving POI data")

	self.walkshed = self.addLiteralInput(identifier="Walkshed",
                    title = "Walkshed polygon", type=StringType)	
	
	self.poiResult = self.addLiteralOutput(identifier="POIResults",
                title="POI results", type=StringType)

    def execute(self):

	poi_service_url = "http://127.0.0.1:9365/poi?walkshed="+urllib2.quote(self.walkshed.getValue())

	try:
		poi_data = urllib2.urlopen(poi_service_url).read()
		self.poiResult.setValue(poi_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
