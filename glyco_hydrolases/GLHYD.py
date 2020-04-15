#!/usr/bin/env python
"""
GLHYD is a command line program takes forward and reverse reads in fastq format and processes them with trimmomatic and quality reports are generated. Then the paired reads from the trimmomatic are used for spades.py assembly.

"""
import sys
import argparse
import subprocess
import os

import annotate
import assemble

RESULTS_DIR = "glhyd_output/"
ANNOTATE_DIR = RESULTS_DIR+"anno/"

def main():
	parser = argparse.ArgumentParser(description="Assembles and annotates genome given a set of proteins.")
	parser.add_argument("F",
				type=str,
				metavar="<foward reads>",
				help="Forward reads in FastQ format."
				)
	parser.add_argument("R",
				type=str,
				metavar="<reverse reads>",
				help="Reverse reads in FastQ format."
				)
	parser.add_argument("dbname",
				type=str,
				meavar="<database name>",
				help="Name for the blast database."
	parser.add_argument("dbseqs",
				type=str,
				metavar="<database sequences>",
				help="Set of reference proteins."

	args = parser.parse_args()


	assemble.assemble_genome(
		args.F,
		args.R,
		RESULTS_DIR
	)

	annotate.annotate_proteins(
		RESULTS_DIR+'spades_output/contigs.fasta',
		ANNOTATE_DIR,
		args.dbname,
		args.dbseqs
	)

if _name_== "_main_":
	main()
