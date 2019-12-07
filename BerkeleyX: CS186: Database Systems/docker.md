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
