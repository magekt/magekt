from flask import Flask, send_from_directory, render_template_string, request
import os
import time

app = Flask(__name__)

# Simple counter using URL parameter
HTML_LIST_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{% if content_loaded %}Available HTML Files{% else %}Loading Page...{% endif %}</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            color: white;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }
        .loading-container {
            text-align: center;
            padding: 50px;
        }
        .spinner {
            width: 50px;
            height: 50px;
            border: 5px solid rgba(255, 255, 255, 0.3);
            border-top: 5px solid #00ff00;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .countdown {
            font-size: 36px;
            color: #00ff00;
            font-weight: bold;
            text-shadow: 0 0 20px #00ff00;
            margin: 20px 0;
        }
        .loading-message {
            font-size: 24px;
            margin: 20px 0;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }
        .status-info {
            font-size: 16px;
            opacity: 0.8;
            margin: 10px 0;
        }
        .content-loaded {
            animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            color: #00ff00;
            text-align: center;
            text-shadow: 0 0 20px #00ff00;
            margin-bottom: 30px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            border-left: 4px solid #00ff00;
            transition: all 0.3s ease;
        }
        li:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateX(10px);
        }
        a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            font-weight: 500;
        }
        a:hover {
            color: #00ff00;
            text-shadow: 0 0 10px #00ff00;
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not content_loaded %}
            <div class="loading-container">
                <div class="spinner"></div>
                <div class="loading-message">
                    <h2>🚀 Page Will Load In No Time!</h2>
                </div>
                <div class="countdown" id="countdown">{{ next_refresh }}</div>
                <div class="status-info">
                    <p>Refreshing in <span id="timer">{{ next_refresh }}</span> seconds</p>
                </div>
            </div>
            
            <script>
                let timeLeft = {{ next_refresh }};
                const timerElement = document.getElementById('timer');
                const countdownElement = document.getElementById('countdown');
                
                const timer = setInterval(() => {
                    timeLeft--;
                    timerElement.textContent = timeLeft;
                    countdownElement.textContent = timeLeft;
                    
                    if (timeLeft <= 0) {
                        clearInterval(timer);
                        timerElement.textContent = "Refreshing...";
                        countdownElement.textContent = "⟳";
                    }
                }, 1000);
                
                setTimeout(() => {
                    window.location.href = "/?step={{ next_step }}";
                }, {{ next_refresh * 1000 }});
            </script>
        {% else %}
            <div class="content-loaded">
                <h1>📁 Available HTML Files</h1>
                <ul>
                    {% for html_file in html_files %}
                    <li><a href="/view/{{ html_file }}">📄 {{ html_file }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def list_html_files():
    step = int(request.args.get('step', 0))
    refresh_intervals = [3, 5, 8]
    
    if step >= len(refresh_intervals):
        html_files = [f for f in os.listdir('.') if f.lower().endswith('.html')]
        return render_template_string(HTML_LIST_TEMPLATE, 
                                    content_loaded=True, 
                                    html_files=html_files)
    
    current_interval = refresh_intervals[step]
    next_step = step + 1
    
    return render_template_string(HTML_LIST_TEMPLATE,
                                content_loaded=False,
                                next_refresh=current_interval,
                                next_step=next_step)

@app.route('/view/<path:filename>')
def serve_html(filename):
    if os.path.isfile(filename) and filename.lower().endswith('.html'):
        return send_from_directory('.', filename)
    else:
        return "File not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
