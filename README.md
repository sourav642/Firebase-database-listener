# Firebase-database-listener
A simple python script which listens to any updates to a real time data base in Fire base and sends email accordingly.

This code uses pyrebase:an efficient python module for Firebase, and smtplib for emails.

# Pre requirements:
1. A gmail account.

2. Enable this:https://www.google.com/settings/security/lesssecureapps

3. Open this link and click continue:https://accounts.google.com/DisplayUnlockCaptcha

Steps 2 and 3 may take upto 10 minutes to process.Please be patient :)


# Brief Description:
Link to the data base:https://user-database-c5688.firebaseio.com/

This is a real time database consisting of two nodes 'Users' and 'User Information'.Informations are stored in Users in the following way:

=>A serial number(starting from 1)

=>Under the serial number there are two keys 'user name' and 'user email' containing corresponding values.(These 2 keys must not have any other name)

'User Information' node just contains a copy of the information present in 'Users' node at any given time.

**Important**: Both the nodes conatin a 'Default' key and **it must not be deleted**.In case it gets deleted the code will automatically create one.

# Tutorial:
1. The code is present in the src folder and is written in Python 3.6.Please insert the **api key** or to get the key mail me at:sac642@gmail.com

2. Upon execution the listener will start running.(use any python ide or python shell)

3. The user can now make any updates in the database but it **must be in the 'Users' node only following the format specified above**.'User Information' node will automatically get populated based on the 'Users' node.

4. After updation user is asked to validate the user email(type 'Y' or 'y') and send a message by logging in with his/her email id and password.The sender's email account **must be in gmail.**

5. In case the user doesn't want to send an email he/she must type 'N' or 'n' to cancel the prompt.

6.Step 4 or 5 is essential as the session will still continue to run after user input and reccord any further changes made in the database and will also ask for sending emails again if the data is **sufficient**.The session can only be terminated manually by closing.

7. For more details please see sample_output.txt


Thank You.

