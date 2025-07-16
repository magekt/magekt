from flask import Flask, send_from_directory, render_template_string, request
import os

app = Flask(__name__)

HTML_LIST_TEMPLATE = """  <!-- full HTML string here like in the above index.html, omitted for brevity --> """

@app.route('/')
def list_html_files():
    step = int(request.args.get('step', 0))
    refresh_intervals = [3, 5, 8]

    if step >= len(refresh_intervals):
        html_files = [
            f for f in os.listdir('.') 
            if f.lower().endswith('.html') and f.lower() != 'index.html'
        ]
        return render_template_string(
            HTML_LIST_TEMPLATE,
            content_loaded=True,
            html_files=html_files
        )

    current_interval = refresh_intervals[step]
    next_step = step + 1

    return render_template_string(
        HTML_LIST_TEMPLATE,
        content_loaded=False,
        next_refresh=current_interval,
        next_step=next_step
    )

@app.route('/view/<path:filename>')
def serve_html(filename):
    if os.path.isfile(filename) and filename.lower().endswith('.html'):
        return send_from_directory('.', filename)
    else:
        return "File not found.", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
