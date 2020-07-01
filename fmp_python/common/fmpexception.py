class FMPException(Exception):
    def __init__(self, *args):
        if len(args) > 1:
            self.message = args[0]
            self.function_name = args[1]
        elif len(args) == 1:
            self.message = args[0]
        else:
            self.message = None
            self.function_name = None

    def __str__(self):
        if self.message and self.function_name:
            return 'FMPException.{0}, {1}'.format(self.function_name, self.message)
        elif self.message:
            return 'FMPException: {0}'.format(self.message)
        else:
            return 'FMPException has been raised'
            