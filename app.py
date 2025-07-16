from flask import Flask, send_from_directory, render_template_string, session, request
import os
import time

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Add this for session management

# Enhanced HTML List Template with auto-refresh functionality
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
        .refresh-info {
            background: rgba(0, 255, 0, 0.1);
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
            border: 1px solid rgba(0, 255, 0, 0.3);
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not content_loaded %}
            <!-- Loading State -->
            <div class="loading-container">
                <div class="spinner"></div>
                <div class="loading-message">
                    <h2>🚀 Page Will Load In No Time!</h2>
                    <p>Please wait while we prepare your content...</p>
                </div>
                <div class="countdown" id="countdown">{{ next_refresh }}</div>
                <div class="status-info">
                    <p>Refreshing in <span id="timer">{{ next_refresh }}</span> seconds</p>
                    <p>Attempt: {{ refresh_attempt }}/3</p>
                </div>
                <div class="refresh-info">
                    <p><strong>Auto-Refresh Schedule:</strong></p>
                    <p>🔄 First refresh: 3 seconds</p>
                    <p>🔄 Second refresh: 5 seconds</p>
                    <p>🔄 Final refresh: 8 seconds</p>
                </div>
            </div>
            
            <script>
                // Countdown timer
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
                        countdownElement.style.animation = "spin 0.5s linear infinite";
                    }
                }, 1000);
                
                // Auto-refresh after the specified time
                setTimeout(() => {
                    window.location.reload();
                }, {{ next_refresh * 1000 }});
            </script>
        {% else %}
            <!-- Content Loaded State -->
            <div class="content-loaded">
                <h1>📁 Available HTML Files</h1>
                {% if html_files %}
                    <ul>
                        {% for html_file in html_files %}
                        <li><a href="/view/{{ html_file }}">📄 {{ html_file }}</a></li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <div class="refresh-info">
                        <p>No HTML files found in the current directory.</p>
                        <p>Add some .html files to see them listed here!</p>
                    </div>
                {% endif %}
                
                <div class="refresh-info">
                    <p>✅ Page loaded successfully!</p>
                    <p>🔄 <a href="/" style="color: #00ff00;">Refresh page</a> to check for new files</p>
                </div>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

def check_content_ready():
    """
    Function to determine if the page content is ready to display
    Modify this function based on your specific needs
    """
    # Check if HTML files exist and are accessible
    try:
        html_files = [f for f in os.listdir('.') if f.lower().endswith('.html')]
        
        # You can add additional checks here:
        # - Check if files are not empty
        # - Check if specific files exist
        # - Check external dependencies
        # - Check database connections
        # etc.
        
        # For now, we'll consider content ready if we can list files successfully
        return True, html_files
    except Exception as e:
        print(f"Error checking content: {e}")
        return False, []

@app.route('/')
def list_html_files():
    # Initialize session variables if not present
    if 'refresh_count' not in session:
        session['refresh_count'] = 0
        session['start_time'] = time.time()
    
    # Define refresh intervals: 3s, 5s, 8s
    refresh_intervals = [3, 5, 8]
    
    # Check if content is ready
    content_ready, html_files = check_content_ready()
    
    # If content is ready, display it
    if content_ready and session['refresh_count'] >= len(refresh_intervals):
        return render_template_string(HTML_LIST_TEMPLATE, 
                                    content_loaded=True, 
                                    html_files=html_files)
    
    # If we haven't exceeded our refresh attempts, continue refreshing
    if session['refresh_count'] < len(refresh_intervals):
        current_interval = refresh_intervals[session['refresh_count']]
        session['refresh_count'] += 1
        
        return render_template_string(HTML_LIST_TEMPLATE,
                                    content_loaded=False,
                                    next_refresh=current_interval,
                                    refresh_attempt=session['refresh_count'],
                                    html_files=[])
    
    # If we've exceeded refresh attempts, show content anyway
    return render_template_string(HTML_LIST_TEMPLATE, 
                                content_loaded=True, 
                                html_files=html_files)

@app.route('/view/<path:filename>')
def serve_html(filename):
    # Serve the requested HTML file from the root directory
    if os.path.isfile(filename) and filename.lower().endswith('.html'):
        return send_from_directory('.', filename)
    else:
        return "File not found.", 404

# Route to reset the refresh cycle (useful for testing)
@app.route('/reset')
def reset_refresh():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
