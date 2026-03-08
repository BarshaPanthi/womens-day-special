# app.py
# ─────────────────────────────────────────────
# Responsible for ONE thing only:
# Running the web server and handling routes.
# ─────────────────────────────────────────────

from flask import Flask, request, send_file, render_template
import base64, io
from card import make_card

app = Flask(__name__)


@app.route("/")
def home():
    """Show the empty form — no card yet."""
    return render_template("index.html",
                           name="",
                           theme="rose",
                           card_data=None)


@app.route("/result")
def result():
    """Generate card and show it embedded in the page."""
    name  = request.args.get("name", "You")[:24]
    theme = request.args.get("theme", "rose")

    png_bytes = make_card(name, theme)

    # Convert image to base64 text so it embeds in HTML
    card_b64 = base64.b64encode(png_bytes).decode("utf-8")

    return render_template("index.html",
                           name=name,
                           theme=theme,
                           card_data=card_b64)


@app.route("/download")
def download():
    """Send the PNG as a file download."""
    name  = request.args.get("name", "You")[:24]
    theme = request.args.get("theme", "rose")

    png_bytes = make_card(name, theme)

    return send_file(
        io.BytesIO(png_bytes),
        mimetype="image/png",
        as_attachment=True,
        download_name=f"womens_day_{name.replace(' ', '_')}.png"
    )


if __name__ == "__main__":
    print("\n✨  Women's Day Card Generator")
    print("    Open →  http://localhost:5050\n")
    import os
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)