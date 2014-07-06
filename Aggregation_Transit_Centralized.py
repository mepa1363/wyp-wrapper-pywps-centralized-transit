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
            identifier = "Aggregation_Transit_Centralized", # must be same, as filename
            title="Aggregation WPS",
            version = "0.1",
            storeSupported = "true",
            statusSupported = "true",
            abstract="Process for aggregating data")

	self.start_point = self.addLiteralInput(identifier="StartPoint",
                    title = "walking start point", type=StringType)

	self.walkshed_collection = self.addLiteralInput(identifier="WalkshedCollection",
                    title = "walkshed collection", type=StringType)

	self.walkshed_union = self.addLiteralInput(identifier="WalkshedUnion",
                    title = "a merged walkshed", type=StringType)

	self.poi = self.addLiteralInput(identifier="POI",
                    title = "poi data", type=StringType)

	self.crime = self.addLiteralInput(identifier="Crime",
                    title = "Crime data", type=StringType)

	self.transit = self.addLiteralInput(identifier="Transit",
                    title = "transit data", type=StringType)

	self.walking_time_period = self.addLiteralInput(identifier="WalkingTimePeriod",
                    title = "walking time period", type=StringType)

	self.distance_decay_function = self.addLiteralInput(identifier="DistanceDecayFunction",
                    title = "use distance decay function or not", type=StringType)
	
	self.result = self.addLiteralOutput(identifier="AggregationResult",
                title="Aggregation results", type=StringType)

    def execute(self):

	start_point = self.start_point.getValue()
	walkshed_collection = self.walkshed_collection.getValue()
	walkshed_union = self.walkshed_union.getValue()
	poi = self.poi.getValue()
	crime = self.crime.getValue()
	transit = self.transit.getValue()
	walking_time_period = self.walking_time_period.getValue()
	distance_decay_function = self.distance_decay_function.getValue()
	
	params = urllib.urlencode({'start_point': start_point, 'walkshed_collection': walkshed_collection, 'walkshed_union': walkshed_union, 'poi': poi, 'crime': crime, 'transit': transit, 'walking_time_period': walking_time_period ,'distance_decay_function': distance_decay_function})
	
	aggregation_service_url = "http://127.0.0.1:9364/aggregation"

	try:
		aggregation_data = urllib2.urlopen(aggregation_service_url, params).read()
		self.result.setValue(aggregation_data)
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except  urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

        return
