from mongoengine import connect


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DB = connect('picket_lite')

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''
