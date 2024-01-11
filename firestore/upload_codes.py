from google.cloud import firestore
#### This script serves to upload the codes into Firestore
project_id = 'YOUR-GCP-PROJECT'
# Initialize Firestore
db = firestore.Client(project=project_id)
collection="codes"

# Define the codes and their statuses
codes = ["a1b4x-cdb1-32c0-890b", "a1b4x-cdb1-32c0-890b"] #### Add your codes here or as a variable (These are not real codes ;) )

# Add each code to Firestore

for code in codes:
    db.collection(collection).document(code).set({'status': False})
