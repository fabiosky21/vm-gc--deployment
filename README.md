# Google Cloud VM Deployment                                                                                                    
This project contains a python script that automates the deployment of virtual machine 

## What this Script Does 
- Reserves a static external IP address
- creates a compute engine instance with: ubuntu 20.04 LTS -2vCPUs, 8 RAM -250GB boot disk 
- Static external IP

## Prerequisities 
Before running the scritp, make sure you have the following: 
- A google cloud project with billing enable (there is free option) 
- Google cloud SDK installed and authneticated -run:
  ````python
  gcloud auth application-defaul login 
- Enable the following APIs, compute engine and IAM
- On visual studio code make sure installed python 
- Installation of libraries

## Run the Script

- The script is ready to be used. Just copy and paste it, and install the required library:

```bash
pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
```

- Once successfully executed, it should print the relevant output.

## Google Console

- There should now be an instance ready to use.  
- Access the instance via SSH. Once inside, install Apache:

 
```bash
sudo apt update
sudo apt install apache2
```

- Then echo "Hello World" or something else. If it returns the echo, it means it was successfully executed:

```bash
echo "Hello World" > /var/www/html/index.html
```

## Then in the same Google Console

There is an option called **External IP** — click it, and it should open a webpage displaying the message you typed.  
*(If not, go back and repeat the steps.)*
