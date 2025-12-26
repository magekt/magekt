"""
Enhanced Flask Application with Dynamic File Discovery and Comprehensive Routing
Features:
- Dynamic HTML file discovery and serving
- Comprehensive error handling
- Project listing with metadata
- Responsive routing system
- Static file serving
"""

import os
import json
import mimetypes
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, send_file, jsonify, request, abort
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['JSON_SORT_KEYS'] = False

# Define project directories and metadata
BASE_DIR = Path(__file__).parent
PROJECTS_DIR = BASE_DIR / 'projects'
TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'

# Ensure directories exist
TEMPLATES_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)
PROJECTS_DIR.mkdir(exist_ok=True)


class ProjectDiscovery:
    """Handles dynamic discovery and metadata of projects"""
    
    @staticmethod
    def get_all_projects():
        """Discover all projects and their metadata"""
        projects = []
        
        if not PROJECTS_DIR.exists():
            return projects
        
        for project_path in PROJECTS_DIR.iterdir():
            if project_path.is_dir():
                project_info = ProjectDiscovery.get_project_info(project_path)
                if project_info:
                    projects.append(project_info)
        
        # Sort projects by name
        projects.sort(key=lambda x: x['name'])
        return projects
    
    @staticmethod
    def get_project_info(project_path):
        """Extract metadata from a project directory"""
        try:
            project_name = project_path.name
            
            # Check for description file
            description = "No description available"
            desc_file = project_path / 'README.md'
            if desc_file.exists():
                with open(desc_file, 'r', encoding='utf-8') as f:
                    description = f.read()[:200]  # First 200 chars
            
            # Count files in project
            file_count = sum(1 for _ in project_path.rglob('*') if _.is_file())
            
            # Get last modified time
            last_modified = datetime.fromtimestamp(project_path.stat().st_mtime)
            
            # Find main HTML file
            html_files = list(project_path.glob('*.html'))
            main_html = None
            if html_files:
                # Prefer index.html, otherwise use first HTML file
                for f in html_files:
                    if f.name == 'index.html':
                        main_html = f.name
                        break
                if not main_html:
                    main_html = html_files[0].name
            
            return {
                'name': project_name,
                'path': str(project_path.relative_to(BASE_DIR)),
                'description': description,
                'file_count': file_count,
                'last_modified': last_modified.isoformat(),
                'main_html': main_html,
                'has_html': bool(html_files),
                'html_files': [f.name for f in html_files]
            }
        except Exception as e:
            print(f"Error discovering project {project_path}: {e}")
            return None


@app.route('/')
def index():
    """Main index page - displays all projects"""
    try:
        projects = ProjectDiscovery.get_all_projects()
        return render_template('index.html', 
                             projects=projects,
                             total_projects=len(projects),
                             generated_at=datetime.utcnow().isoformat())
    except Exception as e:
        return render_template('error.html', 
                             error='Failed to load projects',
                             details=str(e)), 500


@app.route('/api/projects')
def api_projects():
    """API endpoint - returns all projects as JSON"""
    try:
        projects = ProjectDiscovery.get_all_projects()
        return jsonify({
            'success': True,
            'count': len(projects),
            'projects': projects,
            'generated_at': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/projects/<project_name>/')
@app.route('/projects/<project_name>')
def project_index(project_name):
    """Serve project index page"""
    try:
        project_path = PROJECTS_DIR / project_name
        
        if not project_path.exists() or not project_path.is_dir():
            abort(404)
        
        # Try to find index.html in the project
        index_file = project_path / 'index.html'
        if index_file.exists():
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        
        # If no index.html, list available files
        html_files = list(project_path.glob('*.html'))
        if html_files:
            # Redirect to first HTML file
            return f'<h1>Project: {project_name}</h1><p>No index.html found. Available files:</p><ul>' + \
                   ''.join([f'<li><a href="/projects/{project_name}/{f.name}">{f.name}</a></li>' for f in html_files]) + \
                   '</ul>'
        
        abort(404)
    except HTTPException:
        raise
    except Exception as e:
        return render_template('error.html',
                             error=f'Failed to load project: {project_name}',
                             details=str(e)), 500


@app.route('/projects/<project_name>/<path:file_path>')
def serve_project_file(project_name, file_path):
    """Serve files from project directories"""
    try:
        # Security: prevent directory traversal attacks
        if '..' in file_path or file_path.startswith('/'):
            abort(403)
        
        project_path = PROJECTS_DIR / project_name
        file_full_path = project_path / file_path
        
        # Ensure the file is within the project directory
        try:
            file_full_path.relative_to(project_path)
        except ValueError:
            abort(403)
        
        if not file_full_path.exists():
            abort(404)
        
        if file_full_path.is_file():
            # Determine mime type
            mime_type, _ = mimetypes.guess_type(str(file_full_path))
            
            # Serve the file
            return send_file(str(file_full_path), 
                           mimetype=mime_type,
                           as_attachment=False)
        
        abort(404)
    except HTTPException:
        raise
    except Exception as e:
        return render_template('error.html',
                             error='Failed to serve file',
                             details=str(e)), 500


@app.route('/api/project/<project_name>')
def api_project_info(project_name):
    """API endpoint - returns specific project information"""
    try:
        project_path = PROJECTS_DIR / project_name
        
        if not project_path.exists() or not project_path.is_dir():
            return jsonify({
                'success': False,
                'error': 'Project not found'
            }), 404
        
        project_info = ProjectDiscovery.get_project_info(project_path)
        
        if not project_info:
            return jsonify({
                'success': False,
                'error': 'Failed to retrieve project information'
            }), 500
        
        return jsonify({
            'success': True,
            'project': project_info
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'projects_count': len(ProjectDiscovery.get_all_projects())
    })


# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('error.html',
                         error='Page Not Found',
                         details='The requested page or resource could not be found.',
                         error_code=404), 404


@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 errors"""
    return render_template('error.html',
                         error='Forbidden',
                         details='You do not have permission to access this resource.',
                         error_code=403), 403


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('error.html',
                         error='Internal Server Error',
                         details='An unexpected error occurred on the server.',
                         error_code=500), 500


@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all other exceptions"""
    if isinstance(e, HTTPException):
        return e
    
    return render_template('error.html',
                         error='Error',
                         details=str(e),
                         error_code=500), 500


@app.context_processor
def inject_globals():
    """Inject global variables into templates"""
    return {
        'app_name': 'Project Portfolio',
        'app_version': '2.0.0',
        'current_year': datetime.utcnow().year
    }


if __name__ == '__main__':
    # Development server
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=debug_mode
    )
