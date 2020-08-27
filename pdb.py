#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import __main__
import pymol

# Initialise PyMol

__main__.pymol_argv = ['pymol', '-qc']  # Quiet and no GUI
pymol.finish_launching()
pymol.cmd.set('fetch_path', "files/")

# Search for similar proteins using PDB API

url = "http://search.rcsb.org/rcsbsearch/v1/query"

with open('query.json') as json_file:
    json = json.load(json_file)

result = requests.post(url, json=json)
matches = result.json()['result_set']

if result:
    # Iterate throught the results list
    for match in matches:
        # Set variables
        id = match['identifier']
        aligned_png_filename = "files/" + id.lower() + "_aligned.png"

        # Fetch the file
        pymol.cmd.fetch(id)

        # Align the similar protein against the original protein
        alignment = pymol.cmd.align("6B8A", id)

        # Export a png of the alignment
        pymol.cmd.png(aligned_png_filename)

        # Print alignment scores
        print(
            match['identifier']
            + ", score: "
            + str(round(match['score'], 3))
            + ", original_score: "
            + str(round(match['services'][0]['nodes'][0]['original_score'], 1))
            + ", alignment: "
            + str(alignment)
        )
        pass
    print("Found number of PDB entries:", len(matches))
else:
    print("Failed to retrieve results")
