from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

HTML_LIST_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Available HTML Files</title>
</head>
<body>
    <h1>Available HTML Files</h1>
    <ul>
        {% for html_file in html_files %}
        <li><a href="/view/{{ html_file }}">{{ html_file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def list_html_files():
    # List all .html files in the root directory (where app.py is located)
    html_files = [f for f in os.listdir('.') if f.lower().endswith('.html')]
    return render_template_string(HTML_LIST_TEMPLATE, html_files=html_files)

@app.route('/view/<path:filename>')
def serve_html(filename):
    # Serve the requested HTML file from the root directory
    if os.path.isfile(filename) and filename.lower().endswith('.html'):
        return send_from_directory('.', filename)
    else:
        return "File not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
