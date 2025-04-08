--Google Cloud VM Deployment--
This project contains a python script that automates the deployment of virtual machine

--What this Script Does--
-Reserves a static external IP address
-creates a compute engine instance with:
 -ubuntu 20.04 LTS
  -2vCPUs, 8 RAM
  -250GB boot disk
  -Static external IP

--Prerequisities
  Before running the scritp, make sure you have the following:
   -A google cloud project with billing enable (there is free option)
   -Google cloud SDK installed and authneticated
   -run: gcloud auth application-defaul login
   -enable the following APIs, compute engine and IAM
   -On visual studio code make sure installed python
   -Installation of libraries, pip install google-api-python-client oauth2client

--Run the Script 
 -Once succesfully executed should print it

--Google console
 -In there should be the instance ready to use
 -Access to the SSH, once in there install apache 
 -Then echo hello world or soemthing else, if it returns the echo means its succeddfully executed
 -Then in the same Google console there is option call external IP, click over there and should open a webpage with the echo you type (if not go back steps again)
