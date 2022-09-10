# - create imagen
```bash
cd (path of repository)
docker build -t my-python-app .
```
# - create container
## -- create container and enable port
```bash
docker run -p 8000:8000 -it --rm --name my-running-app my-python-app
```
## -- create container and and show console
If you want to go to the console inmediately after the container was created use
this command. This is usefull when you container doesn't initialize.
```bash
docker run -it --rm --name my-running-app my-python-app bash
```
## -- if container starts correctly and you want to use the bash anyway
```bash
docker exec -it my-running-app bash
```
## -- comments
- requirements not installed in venv. We have to correct it.
# - a more simple way to create image and container
```bash
cd (path of repository)
docker-compose up -d
```
luego probar contener yendo a la siguiente direccion http://127.0.0.1:8000/app/?name=josue&age=123


# - doc
- https://redis.io/
- https://pypi.org/project/redis/
- https://www.djangoproject.com/
- https://docs.djangoproject.com/en/4.1/topics/cache/#redis
- https://flask.palletsprojects.com/en/2.2.x/
- https://hub.docker.com/_/python

