from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'AC11351b994d08af0b4c7de7db5ad2eed8'
auth_token = '04178dc9afd5a3d3de5bec70d4f67775'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Fatema, Sinthiya, mariya, Azad, Samiul, Hadiul, Aslam , nayem, salma.",
                     from_='+13342491806',
                     to='+8801765542693'
                 )

print(message.sid)