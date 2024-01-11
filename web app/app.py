from flask import Flask, render_template
from google.cloud import firestore
import os

# Initialize Flask
app = Flask(__name__)

# Initialize Firestore
project_id = 'YOUR-GCP-PROJECT'
db = firestore.Client(project=project_id)
collection = "codes"

#currentStatus=False
currentStatus = os.getenv('currentStatus', 'False')
currentStatus = True if currentStatus.lower() == 'true' else False

newStatus = os.getenv('newStatus', 'True')
newStatus = True if newStatus.lower() == 'true' else False

#newStatus=True
# Get a unique code from Firestore


def get_and_update_code():
    @firestore.transactional
    def update_in_transaction(transaction, doc_ref):
        try:
            snapshot = doc_ref.get(transaction=transaction)
            if snapshot.exists and snapshot.get('status') == currentStatus:
                transaction.update(doc_ref, {'status': newStatus})
                return snapshot.id
            else:
                return None
        except Exception as e:
            print(f"Error in transaction for document {doc_ref.id}: {e}")
            raise

    codes_collection = db.collection(collection)
    attempts = 0
    max_attempts = 20

    while attempts < max_attempts:
        query = codes_collection.where('status', '==', currentStatus).limit(1).stream()
        for doc in query:
            code_id = update_in_transaction(db.transaction(), doc.reference)
            if code_id:
                print(f'Updated code: {code_id} status to True')
                return code_id
        attempts += 1

    print("No document with status False found or all attempts failed.")
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-code', methods=['POST'])
def get_code():
    unique_code = get_and_update_code()
    if unique_code:
        return render_template('code.html', code=unique_code)
    else:
        return render_template('error.html')  # A template to show if no code is available

if __name__ == '__main__':
    
    app.run(debug=False, host='0.0.0.0', port=8080)
