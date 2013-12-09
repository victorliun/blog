class PluginMount(type):
    """docstring for PluginMount"""
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            # This branch only executes when processing the mount point itself.
            # So, since this is a new plugin type, not an implementation, this
            # class shouldn't be registered as a plugin. Instead, it sets up a 
            # list where plugins van be registered later.
            cls.plugins = []
        else:
            # This must be a plugin implementation, which should be registered.
            # Simply appending it to the list is all that's needed to keep
            # track of it later.
            cls.plugins.append(cls)
        

class PasswordValidator(object):
    """
    docstring for PasswordValidator
    plugins extending this class will be used to validate passwords.
    Valid plugins must provide the following method.

    validate(self, passwords)
        Receives a password to test, and either finishes silently or raise a
        ValueError if the password was invalid. The exception may be displayed
        to the user, so make sure it adequately describes what's wrong.
    """
    __metaclass__ = PluginMount


def is_valid_password(password):
    """
    Returns True if the password was fine, False if there is a problem.
    """

    for plugin in PasswordValidator.plugins:
        try:
            plugin().validate(password)
        except ValueError:
            return False

    return True

def get_password_errors(password):
    """
    Returns a list of message indicating any problems that were found 
    with the password. If it was fine, this returns an empty list.
    """

    errors = []
    for plugin in PasswordValidator.plugins:
        try:
            plugin().validate(password)
        except ValueError, e:
            errors.append(str(e))

    return errors

class MinimumLength(PasswordValidator):
    """docstring for MinimumLength"""
    def validate(self, password):
        """Raises ValueError if the password is too short"""
        if len(password) < 6:
            raise ValueError('Passwords must be at least 6 characters')

class SpecialCharacters(PasswordValidator):
    """docstring for SpecialCharacters"""
    def validate(self, password):
        """ Raises ValueError if the password doesn't contain one special character."""
        if password.isalnum():
            raise ValueError("Passwords must contain one special character")

 

def test():
    """plugins test"""

    passwords = ['pass', 'passwords', 'p@ssword']

    for password in passwords:
        print ("Checking %r..." % password),
        if is_valid_password(password):
            print "Valid!"
        else:
            print # new line
            for error in get_password_errors(password):
                print ' %s' %error


if __name__ == '__main__':
    test()