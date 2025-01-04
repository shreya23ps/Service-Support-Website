

# Service-Support-Website

Project Overview

   The Service Support Website is an integrated digital platform aimed at revolutionizing the management of essential government services. This project provides a    
   centralized system for users to apply for various government documents, track their status, and manage updates seamlessly.

   The system enhances transparency, reduces administrative burdens, and streamlines processes such as applying for PAN cards, death certificates, and driving    
   
   licenses. Additionally, it offers robust data management, real-time status tracking, and automated electoral roll updates.

# Features
   1. User-Friendly Interface: Simplifies access to government services for citizens.
   
   2. Centralized Service Platform: Allows applications for PAN cards, death certificates, driving licenses, and more.
   
   3. Real-Time Tracking: Provides real-time updates on application statuses. 
   
   4. Automated Updates: Maintains and updates electoral rolls based on official records.
   
   5. Secure Data Management: Ensures data integrity and compliance with regulations.
   
   6. Admin Dashboard: Facilitates monitoring, approval, and reporting.

# System Requirements

   Hardware:

   •	Minimum: 4 GB RAM, 2-core processor

   •	Recommended: 8 GB RAM, higher-performance processor

   Software:

   •	Operating System: Windows 10+, macOS (latest), or Linux

   •	Browser: Latest version of Chrome, Firefox, Safari, or Edge

   •	Internet Connection: Stable, minimum 1 Mbps

# Installation and Setup
   1.	Clone the Repository:
   
      git clone https://github.com/shreya23ps/Service-Support-Website

      cd ServiceSupportWebsite

   2.	Create and Activate a Virtual Environment
  

   On Windows:

      python -m venv venv
      
      venv\Scripts\activate

   On macOS/Linux:

      python3 -m venv venv
      
      source venv/bin/activate
      
   3.	Apply Migrations


      python manage.py makemigrations
      
      python manage.py migrate
     	
   4.	Run the Development Server
   
      python manage.py runserver
      
   
   After running the above command, the server will start on http://127.0.0.1:8000/. Open this link in your browser to access the application.

         
# Usage Instructions

   1.	Apply for Services:

     	Log in, select a service (e.g., PAN Card), complete the application form, and upload required documents.
   
   3.	Track Status:

     	Go to the Status Check section, input your application ID, and view updates.
   
   5.	Admin Tools:

     	Access the Admin Dashboard to manage user applications and monitor system analytics.

# Contributors

   •	Shreya Parsewar
   
      Master of Computer Applications, MIT World Peace University.
      
   •	 Rahul Sonawane
   
      Master of Computer Applications, MIT World Peace University.





