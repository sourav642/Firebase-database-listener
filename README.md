# Firebase-database-listener
A simple python script which listens to any updates to a real time data base in Fire base and sends email accordingly.

#PRE REQUIREMENTS:
1.A gmail account
2.Enable ths:https://www.google.com/settings/security/lesssecureapps
3.Open this link and click continue:https://accounts.google.com/DisplayUnlockCaptcha
Steps 2 and 3 may take upto 10 mins to process.Please be patient.

#BRIEF DESCRIPTION:
Link to the data base:https://user-database-c5688.firebaseio.com/
This is a real time database consisting of two nodes 'Users' and 'User Information'.Informations are stored in Users in the following way:
=>A serial number(starting from 1)
=>Under the serial number there are two keys 'user name' and 'user email' as keys containing corresponding values.(The name of the keys should not be different)
User Information node just contains a copy of the information present in Users node at any given time.
**Important**:Both the nodes conatin a 'Default' key and **it must not be deleted**.In case it gets deleted the code will automatically create one.

#TUTORIAL:
1.The code is present in the src folder and is written in Python 3.6.Please insert the api key or to get the key mail me at:sac642@gamil
2.Upon execution the listener will start running.(use anty python ide or pyhton shell)
3.The user can now make any updates but it smust be in the 'Users' node only following the format specified above.User Information node will automatically get populated.
4.After updation user is asked to validate the email and send the email by logging in with his/her email id.
5.In case the user doesn't want to send an email he/she must type 'N' or 'n' to get out of email service.
6.**Further modifications/updations are allowed only after he/she completes step 5.**
7.The session will still continue to run after step 5 and reccord any further changes made.It can only be terminated manually.
8.For more details please see sample_output.txt

Thank You.

