Build a live visualisation of stock data ploted retrieved from the Yahoo finance public api hosted on http://thestockticker.pythonanywhere.com/

1. Install the packages listed in requirements.txt

2. Create the main python file and name it 'app.py'

3. Create a html file which will be hosted on the web including the visualisation of your python file, name it 'index.html'

4. Create a free user on https://www.pythonanywhere.com/
(You can use this manual: https://medium.com/swlh/how-to-host-your-flask-app-on-pythonanywhere-for-free-df8486eb6a42)

4.1. Create a new file and name it requirements.txt enter the packages listed in requirements.txt
4.2. Create a Beginner account which is free.
Pick a username which fits to the application you want to host as your username will be part of the URL (e.g. Username "TheStockTicker -> http://thestockticker.pythonanywhere.com/ )
4.3. Create a Web App by clicking on "Add a new web app" button
4.4. Select your Python web framework. Choose the Python Version 3.10.
4.5. Create a file named 'app.py' in the newly created folder /mysite and copy the content of your app.py into it
4.6. Create a folder called 'templates' within the folder /mysite, name it 'index.html' and copy the content of your index.html file into it
4.7. Save the file 'requirements.txt' in the folder /mysite and install all the listed packages by executing the following command in the bashconsole within the directory /mysite: pip3 install -r requirements.txt --user
4.8. Configure the root file by open the WSGI configuration file: /var/www/thestockticker_pythonanywhere_com_wsgi.py in the Web tab and change the import flask statement to 'from app import app as application'. This is needed to define the correct location of your python file.
4.9. Run the web application and and reload the URL, access it and have fun!
