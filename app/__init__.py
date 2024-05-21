import random
import sqlite3
from random import random

from flask import Flask, request
from flask_cors import CORS

app = Flask(
    __name__,
    static_folder="../frontend/dist",
    static_url_path="",
)

CORS(app)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/mock-search/<search_term>")
def mock_response(search_term):
    # http://localhost:5000/mock-search/Polyethylen

    print("testyyyyy")
    con = sqlite3.connect("test.db")
    con.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries

    query = "SELECT distinct drug_1_concept_name FROM drugs where drug_1_concept_name like ?;"
    search_term = f"%{search_term}%"
    cur = con.execute(query, (search_term,))
    results = cur.fetchall()
    search_results = [dict(row) for row in results]  # Convert rows to dictionaries
    print(search_results)
    con.close()
    return {
        "searchTerm": search_term,
        "searchResults": search_results[0],
    }
    # return {
    #    "searchTerm": search_term,
    #    "searchResults": sorted(
    #        [
    #            "POLYETHYLENE GLYCOL 3350",
    #            "polyethylene glycol 9000",
    #            "polyethylene glycol 4000",
    #            "Polyethylene Glycol 400",
    #            "Methoxy polyethylene glycol-epoetin beta",
    #        ]
    #    ),
    # }


@app.route("/mock-interactions")
def mock_interactions():
    # http://localhost:8000/mock-interactions?selectedMeds=peg%2010%2Cpeg%2020

    selected_meds = request.args.get("selectedMeds")
    print("Selected meds: ", selected_meds)

    if selected_meds is None:
        return {}, 400
    if len(selected_meds) < 2:
        return {"selectedMeds": selected_meds}, 400

    # selected_meds = selected_meds.split(",")
    certainty = round(random(), 3)

    con = sqlite3.connect("test.db")
    con.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries

    query = "SELECT distinct condition_concept_name FROM drugs where drug_1_concept_name like ? and drug_2_concept_name like ?;"
    drug1, drug2 = selected_meds.split(",")
    cur = con.execute(query, (drug1, drug2))
    results = cur.fetchall()
    search_results = [dict(row) for row in results]  # Convert rows to dictionaries
    print(search_results)
    con.close()

    return {
        "selectedMeds": selected_meds,
        "searchResults": search_results[0],
    }

    # return {
    #    "selectedMeds": selected_meds,
    #    "interactions": [
    #        {
    #            "drug1": "POLYETHYLENE GLYCOL 3350",
    #            "drug2": "polyethylene glycol 9000",
    #            "sideEffect": "death",
    #            "certainty": certainty,
    #        },
    #        {
    #            "drug1": "POLYETHYLENE GLYCOL 3350",
    #            "drug2": "Polyethylene Glycol 400",
    #            "sideEffect": "diarrhea",
    #            "certainty": certainty,
    #        },
    #    ],
    # }
