# We need to encode our user pk
            # to do that we have to convert pk to byte string
            # to convert anything type to byte we use force_bytes
            # then we pass the result of force_bytes to urlsafe_base64_encode
            # to get encoded string to use in url.
            #####
            # force_bytes(1) == str(1).encode()  ==> b'1'
            # urlsafe_base64_encode('1'.encode()) == urlsafe_base64_encode(force_bytes(1)) ==> MQ
            # urlsafe_base64_decode('MQ') ==> b'1'

 # this is on django 3 # https://github.com/django/django/blob/master/django/contrib/auth/tokens.py
            # use token.py if your user django < 3.0