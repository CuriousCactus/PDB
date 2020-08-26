# Task

- Take pdb ID

- Download file and related files from pdb

- Align them

# Journey

- Was first using this:

  http://www.rcsb.org/pdb/software/rest.do

  Uses xml, probably out of date, couldn't work out how to do similarity searches with it

  See /previous_attempts/pdb.pd (uses python3) and /previous_attempts/pdb2.pd (uses python2)

- These are shown in the documentation as how to do similarity searches (https://www.rcsb.org/pdb/software/rest.do#seqClust) but don't work:

  http://www.rcsb.org/pdb/explorer/structCompXMLData.jsp?method=pw_fatcat&chain=d3bmva1&page=1&rows=10&prettyXML

  http://www.rcsb.org/pdb/explorer/structCompXMLData.jsp?method=pw_fatcat&showAllResults=false&chain=d1iarb1&rows=15&page=1&sidx=probability&sord=asc

- Now using:

  https://search.rcsb.org/index.html#search-api