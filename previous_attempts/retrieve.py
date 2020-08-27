from Bio.PDB import PDBList

list = ["6B8A", "6Q7W", "1FAT", "1JOY"]

pdbl = PDBList()

for id in list:
    pdbl.retrieve_pdb_file(id, pdir="files", file_format="pdb")
    pass
