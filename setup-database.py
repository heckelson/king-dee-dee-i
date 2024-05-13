#!/usr/bin/env python

from os import chdir as cd
from os.path import exists as path_exists
from os.path import getsize
from subprocess import run as sh

FILENAME = "TWOSIDES.csv.gz"
DECOMPRESSED_FILENAME = "TWOSIDES.csv.gz"


if not path_exists(FILENAME):
    sh(
        "wget https://tatonettilab-resources.s3.us-west-1.amazonaws.com/nsides/TWOSIDES.csv.gz",
        shell=True,
    )

if getsize(FILENAME) != 738463578:
    raise Exception("Invalid file size. Delete incomplete download and try again.")

if path_exists(FILENAME) and not path_exists(DECOMPRESSED_FILENAME):
    sh(f"gzip -d {FILENAME}", shell=True)

# TODO: SQLite stuff
