class Configuration:
    def __init__(self, **kwargs):
        self.application_info = None
        self.__dict__.update(**kwargs)
