# Import modules
from pymongo import MongoClient
from flask import Flask, request, jsonify
from send_email import send_email
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins='*')

# Set up the MongoDB client and connect to the database
client = MongoClient("mongodb+srv://irfanrasheedkc:gTo5RnpsY7mpL2BZ@cluster0.mznznpy.mongodb.net/?retryWrites=true&w=majority")
db = client['Gmail']  # Replace 'my_youtube_db' with your preferred database name
customers = db['Customers']

@app.route('/add_customer', methods=['POST'])
def add_customer():
    # Get customer data from the request
    customer_data = request.json  # Assuming the request is sending JSON data
    print("data is :")
    print(customer_data)
    if customer_data:
        # Insert customer data into the 'Customers' collection
        result = customers.insert_one(customer_data)
        if result.acknowledged:
            return jsonify({"message": "Customer added successfully"}), 201
        else:
            return jsonify({"message": "Failed to add customer"}), 500
    else:
        return jsonify({"message": "Invalid customer data"}), 400

@app.route('/send_emails', methods=['POST'])
def send_emails():
    data = request.json
    subject = data.get('subject')
    message_template = data.get('message')

    if not subject or not message_template:
        return jsonify({"message": "Subject and message are required"}), 400

    customer_list = list(customers.find({}, {'_id': 0}))
    print(customer_list)
    if not customer_list:
        return jsonify({"message": "No customers found"}), 404

    for customer in customer_list:
        customer_name = customer.get('name', 'Customer')
        personalized_message = message_template.replace('{customer_name}', customer_name)
        customer_email = customer.get('email')
        print(customer_email)
        send_email(subject, personalized_message, customer_email)

    return jsonify({"message": "Emails sent successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)