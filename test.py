import smtplib

MY_EMAIL = "tj0695646@gmail.com"  # Replace with your email
MY_PASSWORD = "12345678Ab"      # Replace with your password

# Set up the SMTP connection
connection = smtplib.SMTP("smtp.gmail.com", 587)  # Use the correct SMTP server and port
connection.starttls()  # Upgrade the connection to secure
connection.login(MY_EMAIL, MY_PASSWORD)  # Log in to your email account

# Send the email
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
    msg="Subject: Look Up\n\nThe ISS is above your head in the sky."
)

# Close the connection
connection.close()
print("Email sent successfully!")