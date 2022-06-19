# How To Start Server 
## 1. install docker 
Please open the official website of docker and follow the prompts to install docker.
The official website of docker is as follows https://docs.docker.com/desktop/mac/install/. 
## 2. Start Containers 
### Choose Local Path
1. Download the compressed file in the mail and extract it to a local directory.
2. e.g. My local directory is /Users/yangjiangfeng/01_icode/leetcode/baidu/personal-code/homework_yjf/scripts. 

### start container
1. When starting the container, associate the local path with the path inside the container, use -v.
2. Associate the ip of the container with the ip of the local machine, use -p
3. Start the container with the following command.

4. docker run -it -v /Users/yangjiangfeng/01_icode/leetcode/baidu/personal-code/homework_yjf:/program -d -p 5000:5000 --net host --cap-add NET_ADMIN --name tf_yjf --rm tensorflow/tensorflow bash 

## 3.Init Enviroment
- Init enviroment by running the command. 
- sh init_environment.sh.
- If there is a problem with the network speed, you can use the local installation package to install
- Local packages are stored in the directory data/download_package.

## 4.Start Server 
- Start the service with the following command. 
- sh start_server.sh


# How To Interact With Server 
We have prepared a client tool to interact with the server. 

- cd scripts;
- python3 client.py metadata
- python3 client.py history
- python3 client.py train
- python3 client.py predict  your_path_image
- python3 client.py upload_image your_path_image label(OK|NEG)



