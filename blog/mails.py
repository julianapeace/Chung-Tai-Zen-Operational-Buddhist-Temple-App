from django.core.mail import send_mail

send_mail('subject', 'body of the message', 'noreply@chungtaizen.com', ['kmeinhardt7@gmail.com'], fail_silently=False,)

# HOW TO SEND MASS EMAIL
# message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
# message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
# send_mass_mail((message1, message2), fail_silently=False)

# How to use mailgun
# Your API base url will be https://api.mailgun.net/v3/mg.chungtaizen.com
#API KEY = key-94e184bcd0c2fb5090bc7b550123069c
#default pw = 3fd79cec6eb026096a45b10a2d83fcc8
