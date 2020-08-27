# Task

- Take pdb ID

- Download file and related files from pdb

- Align them

# Method

- A search for similar structures is performed using the PDB Search API https://search.rcsb.org/index.html#search-api, using the query in query.json

- The list of similar structures is iterated through, using pymol commands to:
    - download the file
    - align it to the original protein
    - export a png of the alignment