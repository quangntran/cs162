## Software Containers

Today work is a guided exercise through docker.  You are encouraged to poke
things along the way to better understand what the different commands do (e.g
what happens if I edit this command?).  All of these commands are typed into a
shell which has changed to the `session12_1/web` directory.

### 1. Install docker
Start installing docker by following the instructions at:
https://www.docker.com/community-edition

Docker is reasonably lightweight in terms of how much memory and CPU it will use
on your laptop, but you are still encouraged to exit docker before coming to
class!

**On Windows**

Docker Desktop for Windows requires Hyper-V, which is only supported for 64-bit Windows 10 Pro, Enterprise or Education. Windows 10 Home users, as well as users of 32-bit versions and older versions of Windows have to resort to a legacy solution, and use the outdated "Docker Toolbox". See [this link](https://docs.docker.com/toolbox/toolbox_install_windows/).

### 2. Do the tutorial
First work through the 6 part tutorial on docker.  For this session focus on
sessions one and two.

### 3. Build the dockerfile:
```bash
docker build -t simple-cs162-flask:latest .
```
If anything fails here, then please ask for some technical assistance from
fellow students, and if they don't know ask your instructor.

### 4. Run an instance:
```bash
docker run --name=simple-cs162-instance -d --expose 5000 -p 5000:5000/tcp simple-cs162-flask
```
This command will run the container in detached mode, and will connect port 5000
on your local machine to port 5000 of the container.  You can verify this by
visiting `http://localhost:5000/` and you should see the interface to the
computation server.

**On Windows Running Docker Toolbox**

Find the app on the Docker Machine IP. By default, this is `http://192.168.99.100:5000/` where the port is specified after the colon). The IP can be found with the command `docker-machine ip`.

After the instance has started, then you can get a list of all running docker
instances with the command:
```bash
docker ps
```
You can also watch the logs of a docker instance by using the command:
```bask
docker logs -f simple-cs162-instance
```
Stopping or starting the container is a matter of:
```bash
docker container stop simple-cs162-instance
docker container start simple-cs162-instance
```

### 5. Tear it all down
Don't forget to clean up after yourself with the command:
```bash
docker rm -f simple-cs162-instance
```

## Questions
Bring to class a copy of the output from `docker ps` when your container is
successfully running. This needs to be in plain text, so a screenshot is
not appropriate.  Be prepared to explain your answers for the questions below.

### Q1. Bigger picture
Sketch out the bigger picture.  What parts are running on your computer, and
how do they interact with each other?  If there is terminology or acronyms that
you don't understand, search for an explanation on the internet, and bring these
explanation(s) to class to help your fellow students.

Sketch this out as a picture, in a format suitable for pasting into a group
document, and bring it to class.

### Q2. Data persistence
Does the computation server persist data if it is stopped?  How can you tell?

### Q3. Environment variables
Read up on environment variables, and how Python accesses these variables.

Change the code such that the configuration information for the
SQLALCHEMY_DATABASE_URI is given by an environment variable.  What sort of
benefit might this entail?
