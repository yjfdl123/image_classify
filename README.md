# How To Start Server 
## 1. install docker 
## 2. Start Containers 
### Choose Local Path
Download the homework compressed package and extract it to a local directory.
e.g. My local directory is /Users/yangjiangfeng/01_icode/leetcode/baidu/personal-code/homework_yjf/scripts. 

### start container
1. When starting the container, associate the local path with the path inside the container, use -v.
2. Associate the ip of the container with the ip of the local machine, use -p
3. Start the container with the following command.

docker run -it -v /Users/yangjiangfeng/01_icode/leetcode/baidu/personal-code/homework_yjf:/program -d -p 5000:5000 --net host --cap-add NET_ADMIN --name tf_yjf --rm tensorflow/tensorflow bash 


#docker run -it  --restart always --net host --cap-add NET_ADMIN --name desktop-connector wenjunxiao/desktop-docker-connector bash
docker run -it   --net host --cap-add NET_ADMIN --name desktop-connector wenjunxiao/desktop-docker-connector bash



## 3.Init Enviroment
Init enviroment by running the command. 
sh init_environment.sh.
If there is a problem with the network speed, you can use the local installation package to install
Local packages are stored in the directory data/download_package.

## 4.Start Server 
Start the service with the following command. 
sh start_server.sh


# How To Interact With Server 
We have prepared a client tool to interact with the server. 

- cd scripts;
- python3 client.py metadata
- python3 client.py history
- python3 client.py train
- python3 client.py predict  your_path_image
- python3 client.py upload_image your_path_image label(OK|NEG)





## problem 
1. Could not import PIL.Image.
https://stackoverflow.com/questions/51479458/getting-error-could-not-import-pil-image-the-use-of-array-to-img-requires-pi


## 
apt install curl
apt-get install net-tools
apt-get install iproute2
apt-get -y install netcat-traditional
apt-get install lsof
apt-get install telnetd
apt-get install telnet
apt-get install iputils-ping
apt install sqlite3