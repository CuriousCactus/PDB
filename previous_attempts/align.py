# #! /usr/bin/env python3

import __main__
import pymol

__main__.pymol_argv = ['pymol', '-qc']  # Quiet and no GUI

pymol.finish_launching()

list = ["6B8A", "6Q7W", "1FAT", "1JOY"]
pymol.cmd.set('fetch_path', "files/")

for id in list:
    pymol.cmd.fetch(id)
    pass

alignment = pymol.cmd.align("6B8A", "6Q7W")
print(alignment)
