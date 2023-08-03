# Import modules
from pymongo import MongoClient
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up the MongoDB client and connect to the database
client = MongoClient("mongodb+srv://irfanrasheedkc:gTo5RnpsY7mpL2BZ@cluster0.mznznpy.mongodb.net/?retryWrites=true&w=majority")
db = client['Gmail']  # Replace 'my_youtube_db' with your preferred database name
customers = db['Customers']

@app.route('/add_customer', methods=['POST'])
def add_customer():
    # Get customer data from the request
    customer_data = request.json  # Assuming the request is sending JSON data

    if customer_data:
        # Insert customer data into the 'Customers' collection
        result = customers.insert_one(customer_data)
        if result.acknowledged:
            return jsonify({"message": "Customer added successfully"}), 201
        else:
            return jsonify({"message": "Failed to add customer"}), 500
    else:
        return jsonify({"message": "Invalid customer data"}), 400

if __name__ == '__main__':
    app.run()