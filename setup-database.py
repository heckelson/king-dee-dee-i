#!/usr/bin/env python

from os import remove as rm
from os.path import exists as path_exists
from os.path import getsize
from subprocess import run as sh

FILENAME = "TWOSIDES.csv.gz"
DECOMPRESSED_FILENAME = "TWOSIDES.csv"
TABLE_NAME = "drugs"
DB_FILENAME = "test.db"

if not path_exists(FILENAME) and not path_exists(DECOMPRESSED_FILENAME):
    sh(
        "wget https://tatonettilab-resources.s3.us-west-1.amazonaws.com/nsides/TWOSIDES.csv.gz",
        shell=True,
    )

if path_exists(FILENAME):
    if getsize(FILENAME) != 738463578:
        raise Exception("Invalid file size. Delete incomplete download and try again.")

if path_exists(FILENAME) and not path_exists(DECOMPRESSED_FILENAME):
    sh(f"gzip -d {FILENAME}", shell=True)

if path_exists(DECOMPRESSED_FILENAME):
    sh(f"touch {DB_FILENAME}", shell=True)
    sh(
        f'printf ".mode csv {TABLE_NAME}\n.import {DECOMPRESSED_FILENAME} {TABLE_NAME}\n"'
        f" | sqlite3 {DB_FILENAME}",
        shell=True,
    )
    sh(
        f'printf "CREATE TABLE drug_names (name TEXT NOT NULL);'
        f"INSERT INTO drug_names "
        f"SELECT DISTINCT drug_1_concept_name AS name FROM {TABLE_NAME};"
        f'" | sqlite3 {DB_FILENAME}',
        shell=True,
    )

    # cleanup
    try:
        rm(DECOMPRESSED_FILENAME)
    except FileNotFoundError:
        pass
    try:
        rm(FILENAME)
    except FileNotFoundError:
        pass

print("All done!")
