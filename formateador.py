import argparse
from pathlib import Path
import os

import pandas as pd

parser = argparse.ArgumentParser(description="Formateador de la lista de estudiantes")
parser.add_argument("--infile", "-f", help="Archivo excel que se bajo de ematricula administrativa.")
args = parser.parse_args()

def format(
	in_file: os.PathLike, 
	columnas = ["nombre", "carné", "correo institucional"]
) -> None:
	out_file_name = in_file.stem + "_formateada.csv"
	out_file = (
		in_file.parents[1] / 
		"Output" / 
		out_file_name
	)
	# Antes lo hacía por medio de un archivo de texto, pero
	# ahora debería funcionar de una forma más estable.
	#
	# in_file_txt = in_file.stem+".txt"
	# (
	# 	pd.read_excel(in_file, usecols=columnas)
	# 		.to_csv(in_file_txt, sep='\t', index=False)
	# )
	# with open(in_file_txt, 'r') as f, out_file.open('w') as o:
	# 	for line in f:
	# 		if line.strip():
	# 			o.write(line)
	(
		pd.read_excel(in_file, usecols=columnas)
		.dropna(how='any')
		.to_csv(out_file)
	)

if __name__ == "__main__":
	in_file = Path(args.infile)
	format(in_file)

