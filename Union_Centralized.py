import urllib2
import urllib
from types import *
from pywps.Process import WPSProcess

class Process(WPSProcess):

    """Main process class"""
    def __init__(self):
        """Process initialization"""
        # init process
        WPSProcess.__init__(self,
            identifier = "Union_Centralized", # must be same, as filename
            title="Union WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for merging several polygons")

	self.walkshed = self.addLiteralInput(identifier="WalkshedCollection",
                    title = "Walkshed polygons", type=StringType)	
	
	self.unionResult = self.addLiteralOutput(identifier="UnionResults",
                title="a merged polygon", type=StringType)

    def execute(self):
	walkshed_collection = self.walkshed.getValue()
	
	params = urllib.urlencode({'walkshed_collection': walkshed_collection})

	union_service_url = "http://127.0.0.1:9368/union"
	
	try:
		union_data = urllib2.urlopen(union_service_url, params).read()
		self.unionResult.setValue(union_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
