__author__ = 'feliperc'


from geopy import geocoders

g = geocoders.GoogleV3()
#place, (lat, lng) = g.geocode("10900 Euclid Ave in Cleveland")
place, (lat, lng) = g.geocode("Campinas, Brazil")

print "%s" % place
print "%.5f" % lat
print "%.5f" % lng

print "%s: %.5f, %.5f" % (place, lat, lng)