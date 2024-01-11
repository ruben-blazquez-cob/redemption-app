from google.cloud import firestore
#This code updates the status to reset them to False 

project_id = 'YOUR-GCP-PROJECT'
# Initialize Firestore
db = firestore.Client(project=project_id)
collection="codes"

# Reference to the collection
collection_ref = db.collection(collection)  # Replace 'your_collection' with your collection name

# Query documents with status == True
query = collection_ref.where('status', '==', True)
docs = query.stream()

# Update each document
for doc in docs:
    doc_id = doc.id
    doc_ref = collection_ref.document(doc_id)
    doc_ref.update({'status': False})

print("Documents updated successfully.")
