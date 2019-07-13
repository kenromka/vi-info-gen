from flask import render_template
from app import app
from .routes import last_update

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(408)
@app.errorhandler(429)
@app.errorhandler(500)
@app.errorhandler(501)
@app.errorhandler(502)
@app.errorhandler(503)
def any_error(error):
    return render_template("error.html"), getattr(error, "code", 520)