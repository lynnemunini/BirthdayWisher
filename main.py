import smtplib
import pandas
import random
import datetime as dt

now = dt.datetime.now()
today_month = now.month
today_day = now.day
# Tuple to store the current Month and Day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
# Used Dictionary Comprehension to create a dictionary for all the data in my birthdays.csv
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# Check if today's date is in the dictionary
if today in birthdays_dict:
    person = birthdays_dict[today]
    value = random.randint(1, 3)
    # Open a random letter from my letter_templates
    with open(f"letter_templates/letter_{value}.txt") as letter:
        # Read from the letter
        letter = letter.read()
        new_letter = letter.replace("[NAME]", person["name"])
        my_email = "misslynnemunini@gmail.com"
        # Removed my password for security purposes, for the code to work enter you account password below
        # This method only applies to gmail account
        # For Yahoo and hotmail accounts i'll share on the ReadMe
        # Very Important to Note as an error might occur
        # Google has a security feature that prevents less secure apps (The Program), from accessing your account
        # You have to turn this off manually by logging into your account, heading over to Security, Scroll down to
        # Less secure apps access and turn that on, A critical alert will be sent to your email
        # I highly recommend not using your official google account for this program,
        # make a new account to just do this.
        # If you still get errors at this point
        # Try to go through the Gmail Captcha here
        # while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
        # Also don't hesitate to shoot me a dm on Twitter incase of any questions, @lynnemunini
        # That said, enter your account password below
        password = "@26041978"
        # Make sure you've got the correct smtp address for your email provider
        # Gmail: smtp.gmail.com
        # Hotmail: smtp.live.com
        # Outlook: outlook.office365.com
        # Yahoo: smtp.mail.yahoo.com
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{person.email}",
                                msg=f"Subject:Happy Birthday\n\n{new_letter}")

            # Host on the cloud to ensure it runs daily
            # I used PythonAnywhere, link on ReadMe





