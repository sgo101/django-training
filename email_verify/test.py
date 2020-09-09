# from django.core import validators
# from django.core import exceptions
# from django.core.mail import EmailMessage

# def email_validation_function(value):
#     valid = False
#     try:
#         validators.validate_email(value)
#         print('in try')
#         valid = True
#     except exceptions.ValidationError:
#         valid = False
#     except Exception as e:
#         valid = False
#         print('Something went wrong --> ', e)

#     return valid

# # def send_email():
# #     attachments = []  # start with an empty list
# #     for filename in filenames:
# #         # create the attachment triple for this filename
# #         content = open(filename, 'rb').read()
# #         attachment = (filename, content, 'application/pdf')
# #         # add the attachment to the list
# #         attachments.append(attachment)

# #     # Send the email with all attachments
# #     email = EmailMessage('Hello', 'Body goes here', 'from@example.com',
# #             ['to1@example.com', 'to2@example.com'], attachments=attachments)
# #     email.send()

# # email with attaching an image
# def send_email():
#     email = EmailMessage(
#     'Hello',
#     'Body goes here',
#     'saeidtempmail@gmail.com',
#     ['saeidgholami101@gmail.com'],
#     headers={'Message-ID': 'foo'},
# )

#     img = open('pic.jpg', 'rb').read()
#     email.attach('pic.jpg', img, 'image/jpg')
#     email.send()

def bread(path):
    path_dict = {}
    paths = path.split('/')
    paths = [path for path in paths if path != '']
    # path_dict = dict.fromkeys(paths)
    for i in range(len(paths)):
        p = ('/'.join(paths[:i+1]) + '/')
        key = [s for s in p.split('/') if s != ''][-1]
        path_dict[key] = p
    return path_dict




location = '127.0.0.1:8000/users/register/'
ps = bread(location)
print(ps)