from flask import render_template, request, jsonify
from agents.index import rag_answer

def index():
    return render_template("index.html")

def ask_rag():
    data = request.get_json(silent=True) or {}
    question = data.get("query")

    if not question:
        return jsonify({"response": "Empty question"}), 400

    answer = rag_answer(question)

    return jsonify({
        "response": answer
    })
