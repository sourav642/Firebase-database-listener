import pyrebase
import smtplib
import re

config = {
  "apiKey": "AIzaSyBFdM-U7MYgeWmm4gLzlyDR70yOANkXoBQ",
  "authDomain":"user-database-c5688.firebaseapp.com",
  "databaseURL": "https://user-database-c5688.firebaseio.com",
  "storageBucket":"user-database-c5688.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
u_name = u_email = ""
ctr=0
data={"Deafult":"Please don't delete this key"}
db.child("Users").update(data)
def stream_handler(message):

    #Creating the User Information Node which is the exact copy of Users node
    data = db.child("Users").get().val()
    db.child("User Information").update(data)#set(data) can be used instead of update to create a fresh copy

    global u_name,u_email

    #message["data"] None signifies deletion
    if (message["data"] is not None):

        if (type(message["data"]) is dict and "user name" in message["data"].keys() ):
            u_name = message["data"].get("user name")
        elif ("user name" in message["path"]):
            u_name = message["data"]

        if (type(message["data"]) is dict and "user email" in message["data"].keys()):
            u_email = message["data"].get("user email")
        elif ("user email" in message["path"]):
             u_email = message["data"]

         # Following portion is for sending emails.Senders email id must be in gmail.
        if(u_name is not "" and u_email is not ""):
            print("Data added/modified:\nuser name: "+u_name+"\nuser email: "+u_email+"\n")
            print("Please verify the email id and ensure its correct.Once verifed press Y to send an email to the above id or N to quit:")
            st=input()
            if(st=="y" or st=="Y"):
                s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                s.ehlo()
                print("----LOGIN---\n")
                print("Email id:")
                id=input()
                print("\nPassword:")
                password=input()
                s.login(id, password)
                message= "Dear "+u_name+",Welcome to our app."
                s.sendmail(id, u_email, message)
                print("\nEmail sent successfully to "+u_email+"\nSession is still running...")
                s.close()
            else:
                print("Stopped Email service.\nSession is still running....")

    else:
        temp=(re.findall('\d+',message["path"]))

        if(db.child("Users").child(temp[0]).get().val() is not None and "user name" in db.child("Users").child(temp[0]).get().val().keys() ):
            u_name=db.child("Users").child(temp[0]).get().val().get("user name")
        elif(db.child("Users").child(temp[0]).get().val() is not None and "user email" in db.child("Users").child(temp[0]).get().val().keys()):
            u_email=db.child("Users").child(temp[0]).get().val().get("user email")
        else:
            u_name=u_email=""

print("Session is running....")
my_stream = db.child("Users").stream(stream_handler)

