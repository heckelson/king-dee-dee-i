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
