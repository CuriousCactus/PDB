#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbQuery>
    <version>B0907</version>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <description>Experimental Method Search: Experimental Method=SOLID-STATE NMR</description>
    <mvStructure.expMethod.value>SOLID-STATE NMR</mvStructure.expMethod.value>
</orgPdbQuery>
"""

req = urllib2.Request(url, data = queryText)

result = urllib2.urlopen(req).read()

if result:

    print "Found number of PDB entries:", result.count('\n')
    print result

else:

    print "Failed to retrieve results"
