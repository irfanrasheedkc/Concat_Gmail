# Customer Mailer
Customer Mailer is a powerful and intuitive web application designed to enhance your email marketing strategies. Seamlessly send personalized emails to your customer base and manage email campaigns with ease. Craft engaging email templates tailored to your audience, and efficiently organize customer details for targeted communications. Customer Mailer simplifies the process of maintaining customer relationships through efficient email campaigns. Elevate your marketing efforts and foster stronger customer engagement with Customer Mailer. Stay connected and deliver impactful messages effortlessly.

# Team Members
1) Irfan Rasheed    ->  https://github.com/irfanrasheedkc
2) Aparna Sunil    ->  https://github.com/AparnaSunil17
3) Shezma Bijumon    ->  https://github.com/shezmabijumon
4) Alfina S    ->  Github ID

# Team Name - Team #10

# Link To Video - 

# How the tool works

1) Add Email Template:

    Users create an email template with placeholders like {customer_name} or {customer_email}.

2) Fetch Customer Data:

    When initiating an email campaign, the system retrieves customer data from the database.
    This data includes customer names, email addresses, and other relevant information.

3) Dynamic Personalization:

    The application replaces placeholders in the template with actual customer data for each recipient.
    {customer_name} transforms into "John" for one customer and "Jane" for another.

4) Efficient Bulk Sending:

    The tool employs the Gmail API to send emails seamlessly on the user's behalf.
    Each email is tailored for individual customers, utilizing their specific email address and personalized content.

# Libraries Used
1) Python Flask
2) Pymongo
3) smtplib

# How to configure and Run
1. Clone the repository
    
        git clone https://github.com/irfanrasheedkc/Customer_Mailer

2. Create .env file inside server folder<br>
    Obtain gmail application password<br>
    Obtain Mongo_uri<br>
        
        GMAIL_APP_PASSWORD=your_gmail_app_password <br>
        MONGO_URI=your_mongodb_uri

3. Start the server

        python server.py

4. Open landing page

        frontend/landing.html


