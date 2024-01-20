# Weather-Station-Dashboard

- Load env using load_dotenv() to access environment variables, also include that file in .gitignore
# .env
- OPENWEATHERMAP_API_KEY = "your_api_key"

/Weather-Station-Dashboard
│
├── app.py         # Your main Flask application file
├── requirements.txt   # All required Python packages
├── Dockerfile     # Instructions for building the Docker image
├── .dockerignore  # (Optional) Exclude files from Docker build context
└── /templates     # (Optional) Folder for Jinja2 templates
    └── index.html