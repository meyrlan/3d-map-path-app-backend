# Deploying with Docker

1. Run services:
```bash
docker-compose -f deployment/docker-compose.yml build
docker-compose -f deployment/docker-compose.yml up -d
```
2. Create superuser in web server's container:
```bash
docker exec -it deployment_web_1 bash
python manage.py createsuperuser
```
