#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gets IDs of structures in the PDB according to an XML query using Python 2
# Based on https://www.rcsb.org/pdb/software/static.do?p=/software/webservices/search_nmr.jsp

import urllib2

url = 'http://www.rcsb.org/pdb/rest/search'
url = 'http://httpbin.org/post'

xml = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbQuery>
    <version>B0907</version>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <description>Experimental Method Search: Experimental Method=SOLID-STATE NMR</description>
    <mvStructure.expMethod.value>SOLID-STATE NMR</mvStructure.expMethod.value>
</orgPdbQuery>
"""

req = urllib2.Request(url, data = xml)

result = urllib2.urlopen(req).read()

if result:
    print result
    print "Found number of PDB entries:", result.count('\n')
else:
    print "Failed to retrieve results"
