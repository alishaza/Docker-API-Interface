# Docker API
this is a sample project that helps you to abstract the functionality of docker in a simple manner. In this sample project, you can create an app and run it from the container. In this design, the user sends his request to the endpoint, and then our Python code sshes to the server installed on Docker and executes the user's request.
this would be the architecture how we implemented this :
![Capture](https://user-images.githubusercontent.com/53411387/198748839-b85c023d-e967-44d7-821b-d5dabed33c19.PNG)
Although such an assumption may not be true in actual design, it gives you a good idea to understand the performance of cloud companies that try to abstract the DevOps processes.



In many scenarios, you need to measure the performance of the system, for this purpose, you should measure the system by monitoring systems such as ELK or Prometheus when logging events.However, in this scenario we did not consider them but they are very important and they must be considered in implementations.


