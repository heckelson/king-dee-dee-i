import random
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

    return {
        "searchTerm": search_term,
        "searchResults": sorted(
            [
                "POLYETHYLENE GLYCOL 3350",
                "polyethylene glycol 9000",
                "polyethylene glycol 4000",
                "Polyethylene Glycol 400",
                "Methoxy polyethylene glycol-epoetin beta",
            ]
        ),
    }


@app.route("/mock-interactions")
def mock_interactions():
    # http://localhost:8000/mock-interactions?selectedMeds=peg%2010%2Cpeg%2020

    selected_meds = request.args.get("selectedMeds")

    if selected_meds is None:
        return {}, 400
    if len(selected_meds) < 2:
        return {"selectedMeds": selected_meds}, 400

    selected_meds = selected_meds.split(",")
    certainty = round(random(), 3)

    return {
        "selectedMeds": selected_meds,
        "interactions": [
            {
                "drug1": "POLYETHYLENE GLYCOL 3350",
                "drug2": "polyethylene glycol 9000",
                "sideEffect": "death",
                "certainty": certainty,
            },
            {
                "drug1": "POLYETHYLENE GLYCOL 3350",
                "drug2": "Polyethylene Glycol 400",
                "sideEffect": "diarrhea",
                "certainty": certainty,
            },
        ],
    }
