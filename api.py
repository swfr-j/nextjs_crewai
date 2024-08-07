from uuid import uuid4 as uuid
from threading import Thread
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


def kickoff_crew(job_id: str, companies: list[str], positions: list[str]):
    print(f"Starting job {job_id} with companies {companies} and positions {positions}")

    # TODO: Setup the crew

    # TODO: Run the crew

    # TODO: Let the app know we are done


@app.route("/api/crew", methods=["POST"])
def run_crew():
    data = request.json
    if not data or "companies" not in data or "positions" not in data:
        abort(400, description="Invalid request with missing data")

    job_id = str(uuid())
    companies = data["companies"]
    positions = data["positions"]

    thread = Thread(target=kickoff_crew, args=(job_id, companies, positions))
    thread.start()

    return jsonify({"job_id": job_id}), 200


@app.route("/api/crew/<job_id>", methods=["GET"])
def get_crew(job_id):
    return jsonify({"status": "success", "job_id": job_id}), 200


if __name__ == "__main__":
    app.run(debug=True, port=3001)
