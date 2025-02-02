from google.cloud import compute_v1
from google.oauth2 import service_account

# key that i ensured in service account , it create a json file for authentication 
key_path = r"C:\Users\thula\Downloads\tensile-reducer-449609-h8-8fed8e07eca7.json"

# Authenticate using service account credentials
credentials = service_account.Credentials.from_service_account_file(key_path) #just to check the check the key is authenticate to the credentails 

# Project ID 
PROJECT_ID = "tensile-reducer-449609-h8"

# Initialize Compute Engine clients
compute_client = compute_v1.RegionsClient(credentials=credentials)
machine_type_client = compute_v1.MachineTypesClient(credentials=credentials)

# Get all regions
def get_regions():
    regions = compute_client.list(project=PROJECT_ID)
    return [region.name for region in regions]

# Get available VM types for all regions
def list_vm_types_all_regions():
    regions = get_regions()
    all_vm_types = {}

    for region in regions:
        zone = f"{region}-a"  # Using "-a" as a common zone suffix
        print(f"\n✅ Fetching VM types in {region}...")

        try:
            request = compute_v1.ListMachineTypesRequest(project=PROJECT_ID, zone=zone)
            response = machine_type_client.list(request=request)

            vm_types = [machine.name for machine in response]
            all_vm_types[region] = vm_types

            for machine in response:
                print(f"🔹 {machine.name} - {machine.memory_mb} MB RAM, {machine.guest_cpus} vCPUs")

        except Exception as e:
            print(f"❌ Could not fetch VM types for {region}: {e}")

    return all_vm_types

# Run the function
all_vm_data = list_vm_types_all_regions()
