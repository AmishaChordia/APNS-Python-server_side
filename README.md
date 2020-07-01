## APNS-Python-serverside


# Creating the virtual environment:
  1. cd ~/To the project path
  2. python3 -m venv venv
  3. source venv/bin/activate
  4. pip install -r requirements.txt
  
# Creating the .p8 key:
  1. You can create the .p8 file - https://developer.apple.com/account/
  2. Then go to Certificates, Identifiers & Profiles > Keys > add
  3. Select Apple Push Notification service (APNs), put a Key Name (whatever).
  4. Then click on "continue", after "register" and you get it and you can download it.
  
# Getting the key_id and team_id from Apple developer Portal
  1. You can get the Team Id from under your profile in Apple Developer portal
  2. Key Id is generated when creating .p8 file


Obtain the device token from Xcode

