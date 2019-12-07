### Getting the class docker image
```
docker pull cs186/environment
```
This will download the class image onto your computer. When it completes, try the following to make sure everything is working:
```
docker run cs186/environment echo "hello from cs186"
```

### Mounting your shared drive
```
docker run -v "<pathname-to-directory-on-your-machine>:/cs186" -it cs186/environment /bin/bash
```
For example, if the directory you created was /Users/pusheen/Desktop/cs186, then you would run:
```
docker run -v "/Users/pusheen/Desktop/cs186:/cs186" -it cs186/environment /bin/bash
```
(Remember: if you're running Docker Toolbox on Windows, <pathname-to-directory-on-your-machine> should start with //c/Users/)
Once you have verified that your directory was mounted correctly, run the following command:
```
docker run --name cs186 -v "<pathname-to-directory-on-your-machine>:/cs186" -it cs186/environment /bin/bash
```
and then exit from the container. This names the container cs186, so that you can start it up without having to fetch maven dependencies every time you work on a CS 186 homework. If you get an error like Conflict. The container name "/cs186" is already in use by container, run docker container rm cs186 and try again.

You can now start your container whenever you want by running:
```
docker start -ai cs186
```

Other instructions about Docker could also search in : https://yeasy.gitbooks.io/docker_practice/container/run.html
