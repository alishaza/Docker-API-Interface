# Docker API
this is a sample project that helps you to abstract the functionality of docker in a simple manner. In this sample project, you can create an app and run it from the container. In this design, the user sends his request to the endpoint, and then our Python code sshes to the server installed on Docker and executes the user's request.
this would be the architecture how we implemented this :
![Capture](https://user-images.githubusercontent.com/53411387/198748839-b85c023d-e967-44d7-821b-d5dabed33c19.PNG)
Although such an assumption may not be true in actual design, it gives you a good idea to understand the performance of cloud companies that try to abstract the DevOps processes.
so here there are a number of examples

## Add new app
/apps/
```
{
	"name": "app",
	"image": "nginx",
	"command": "sleep 1000",
	"variables": [{
		"key1": "value1"
	}, {
		"key2": "value2"
	}]
}
```
## Run a container
in this case I tried to run two instances from my app by /apps/run/app. in the code I generate random name for these containers.
/apps/run/appname
```
alishazaee@server:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
62cae83cf832   nginx     "/docker-entrypoint.…"   7 seconds ago   Up 4 seconds   80/tcp    1827
26f3fb5ed7f8   nginx     "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   80/tcp    1336
```
## Container Status
you can also check the status of your container. R means it is running and F means it has been finished.
/apps/containers
```
[
    {
        "name": "1336",
        "Status": "R",
        "images": "app"
    },
    {
        "name": "1827",
        "Status": "R",
        "images": "app"
    },
]
```

You can also delete and edit your app settings. connect it to mysql and jump into this sample code and enjoy it :))

In many scenarios, you need to measure the performance of the system, for this purpose, you should measure the system by monitoring systems such as ELK or Prometheus when logging events.However, in this scenario we did not consider them but they are very important and they must be considered in implementations.


