import __main__
import pymol

__main__.pymol_argv = ['pymol', '-qc']  # Quiet and no GUI

pymol.finish_launching()

# Load structure
pymol.cmd.load("files/pdb1joy_aligned.ent")

# Make png
pymol.cmd.png("my_image.png")

# Get out!
pymol.cmd.quit()
