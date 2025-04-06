from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time

# - config -
PROJECT_ID = "mynewcloud-455911"  
ZONE = "us-central1-a"
REGION = "us-central1"
VM_NAME = "my-ubuntu-vm"
IP_NAME = "my-static-ip"
FIREWALL_NAME = "allow-http-ssh"
MACHINE_TYPE = f"zones/{ZONE}/machineTypes/e2-standard-2"
IMAGE_PROJECT = "ubuntu-os-cloud"
IMAGE_FAMILY = "ubuntu-2004-lts"
DISK_SIZE_GB = "250"

# - auth & api -
credentials = GoogleCredentials.get_application_default()
compute = discovery.build("compute", "v1", credentials=credentials)

# -step 1: reserve static ip -
def reserve_static_ip():
    config = {"name": IP_NAME}
    request = compute.addresses().insert(project=PROJECT_ID, region=REGION, body=config)
    response = request.execute()
    print("Reserving static IP...")
    wait_for_region_operation(response['name'])
    result = compute.addresses().get(project=PROJECT_ID, region=REGION, address=IP_NAME).execute()
    return result['address']

# - stpe 2: create vm -
def create_vm_instance(static_ip):
    image_response = compute.images().getFromFamily(project=IMAGE_PROJECT, family=IMAGE_FAMILY).execute()
    source_disk_image = image_response['selfLink']

    config = {
        "name": VM_NAME,
        "machineType": MACHINE_TYPE,
        "tags": {"items": ["http-server", "ssh"]},
        "disks": [{
            "boot": True,
            "autoDelete": True,
            "initializeParams": {
                "sourceImage": source_disk_image,
                "diskSizeGb": DISK_SIZE_GB,
            },
        }],
        "networkInterfaces": [{
            "network": "global/networks/default",
            "accessConfigs": [{
                "name": "External NAT",
                "type": "ONE_TO_ONE_NAT",
                "natIP": static_ip,
            }]
        }]
    }

    request = compute.instances().insert(project=PROJECT_ID, zone=ZONE, body=config)
    response = request.execute()
    print("Creating VM instance...")
    wait_for_zone_operation(response['name'])

# - STEP 3: create firewall rule -
def create_firewall_rule():
    firewall_body = {
        "name": FIREWALL_NAME,
        "allowed": [
            {"IPProtocol": "tcp", "ports": ["22"]},
            {"IPProtocol": "tcp", "ports": ["80"]}
        ],
        "direction": "INGRESS",
        "sourceRanges": ["0.0.0.0/0"],
        "targetTags": ["http-server", "ssh"],
    }

    try:
        request = compute.firewalls().insert(project=PROJECT_ID, body=firewall_body)
        response = request.execute()
        print("Creating firewall rule...")
    except Exception as e:
        if "alreadyExists" in str(e):
            print("Firewall rule already exists.")
        else:
            raise

# - helper -
def wait_for_zone_operation(operation):
    print("Waiting for zone operation to finish...")
    while True:
        result = compute.zoneOperations().get(project=PROJECT_ID, zone=ZONE, operation=operation).execute()
        if result['status'] == 'DONE':
            print("xone operation complete.")
            return
        time.sleep(1)

def wait_for_region_operation(operation):
    print("Waiting for region operation to finish...")
    while True:
        result = compute.regionOperations().get(project=PROJECT_ID, region=REGION, operation=operation).execute()
        if result['status'] == 'DONE':
            print("region operation complete.")
            return
        time.sleep(1)

# - main -
def main():
    static_ip = reserve_static_ip()
    create_vm_instance(static_ip)
    create_firewall_rule()
    print(" vm complete deplment!")

if __name__ == '__main__':
    main()
