PYTHONDONTWRITEBYTECODE=1 uvicorn core_service.src.main.main:app --host 0.0.0.0 --port 8080

# docker build -t your-app-name .
# docker run -p 4000:80 your-app-name