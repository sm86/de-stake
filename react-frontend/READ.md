React Frontend Setup Guide 

This guide provides instructions for setting up and running the React frontend of the Destake application on both RHEL/CentOS/Fedora/Amazon Linux and Ubuntu systems. 
 

Setting up the Server 

Login to the Server, Install and Start Apache HTTP Server 

   `yum install httpd` 

   `systemctl start httpd` 

   
Setting up the Frontend 

Navigate to Frontend Folder: 

`cd /var/www/destake/react-frontend` 


Install npm: 

   		`yum install npm` 


Install Dependencies and Build: 

   		`npm install` 

   		`npm run build` 


Deploy Frontend Files: 

  		`cp -r build/* /var/www/html/` 

  
Accessing the Application: 

Open a web browser and paste the public IP address of the server. You should see the frontend deployed. 

  
Additional Notes 

Setting up VirtualHost: 

Modify `/etc/apache2/sites-available/destake.conf` to include VirtualHost configuration.  
