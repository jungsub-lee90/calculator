# docker download to win 10 home
## for win 10 home update version must be over 20H1
## open powershell with admin 

```python
# 1.allow linux in the window os
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
 
# 2.virtual machine platform activation
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 3. wsl2 download and set the default version which is 2
wsl --set-default-version 2

# 4. download ubuntu from ms store

# 5. wsl version check , if ver is not 2 run 19 line
wsl -l -v
wsl --set-version Ubuntu 2 

# 6. docker desktop for win download and check the settings
## settings > general > wsl2 checked
## settings > resources > wsl integration > enable my default wsl distro checked

#7. download image from docker hub
 docker search [term]
 docker pull [image name]
 
 #8. run container 
 docker run -d(detached) -p(mapping port between a host and a container)
 docker run --name(rename) [name]
  
 #9. commend in a container 
 docker exec -it(keep interaction with container connection) [container name] bash 
 
## docker ps -al(show all containers)


```
