# NEWSFARS Backend

Django backend for the NEWSFARS newspaper application.

## System Requirements

### For macOS:
```bash
# Install system dependencies for pdf2image
brew install poppler
```

### For Ubuntu/Debian:
```bash
# Install system dependencies for pdf2image
sudo apt-get install poppler-utils
```

### For Windows:
Download and install [poppler for Windows](http://blog.alivate.com.au/poppler-windows/)

## Installation

1. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Run the development server:**
```bash
python manage.py runserver
```

## Production Deployment

### Using Gunicorn:

1. **Install gunicorn:**
```bash
pip install gunicorn
```

2. **Run with gunicorn:**
```bash
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

3. **With environment variables:**
```bash
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3 --env DJANGO_SETTINGS_MODULE=backend.settings
```

### Using systemd (Linux):

Create `/etc/systemd/system/newsfars.service`:
```ini
[Unit]
Description=NEWSFARS Django Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/your/project/backend
Environment="PATH=/path/to/your/venv/bin"
ExecStart=/path/to/your/venv/bin/gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
ExecReload=/bin/kill -s HUP $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable newsfars
sudo systemctl start newsfars
```

## Development

For development with additional tools:
```bash
pip install -r requirements-dev.txt
```

## API Endpoints

- `GET /api/pdfs/` - List all PDFs
- `POST /api/pdfs/upload/` - Upload a new PDF (admin only)
- `GET /api/pdfs/{id}/` - Get PDF details
- `DELETE /api/pdfs/{id}/` - Delete PDF (admin only)
- `POST /api/admin/logout/` - Admin logout
- `POST /api/token/` - Get JWT token
- `POST /api/token/refresh/` - Refresh JWT token

## Features

- PDF upload and management
- Automatic PDF to image conversion
- JWT authentication
- Jalali (Persian) date support
- CORS enabled for frontend integration 