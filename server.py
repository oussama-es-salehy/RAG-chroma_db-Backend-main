from flask import Flask
from routes.agents import agents_bp

app = Flask(
    __name__,
    template_folder="views",
    static_folder="static"
)

# API préfixée
app.register_blueprint(agents_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
