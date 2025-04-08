Google Cloud VM Deployment
This project contains a Python script that automates the deployment of a virtual machine on Google Cloud.

 What This Script Does
Reserves a static external IP address

Creates a Compute Engine instance with:

OS: Ubuntu 20.04 LTS

2 vCPUs

8 GB RAM

250 GB boot disk

Static external IP

 Prerequisites
Before running the script, make sure you have the following:

A Google Cloud project with billing enabled (free tier is available)

Google Cloud SDK installed and authenticated:

bash
Copy
Edit
gcloud auth application-default login
Enable the following APIs:

Compute Engine API

IAM API

On Visual Studio Code:

Python installed

Required libraries installed:

bash
Copy
Edit
pip install google-api-python-client oauth2client
How to Run the Script
Run the script:

bash
Copy
Edit
python script_name.py
Once successfully executed, it should print the relevant output.

 After Deployment (Using Google Cloud Console)
Go to the VM Instances section – your instance should be ready to use.

Access the instance via SSH.

Inside the instance, install Apache:

bash
Copy
Edit
sudo apt update
sudo apt install apache2
Echo a simple message:

bash
Copy
Edit
echo "Hello World" > /var/www/html/index.html
In the Google Cloud Console, locate the External IP of your VM and open it in a browser.

You should see the message you echoed.
