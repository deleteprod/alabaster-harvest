# alabaster-harvest

A script that was originally put together in order to pull data out of Splunk via the REST API and then throw it into a new Splunk environment - the underlying reason for this being that the origin environment was a cluster that was not site aware, and we needed the data to exist in its entirety in a site aware manner. Before Splunk 7.2 there wasn't an easy way to do this. However, I've put this script together for reasons of posterity and in case anyone can make use of it for other purposes that I haven't actually thought of.
