from flask import Blueprint
from controllers.agents import index, ask_rag

agents_bp = Blueprint("agents", __name__)

# Page HTML
agents_bp.route("/", methods=["GET"])(index)

# API Chat
agents_bp.route("/conversation", methods=["POST"])(ask_rag)
