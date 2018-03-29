class HandlerFactory(object):

    @classmethod
    def generate(cls, handlers):
        """
        The return value is the chain of handlers
        for example: CEOHandler(SeniorHandler(JuniorHandler(DefaultHandler())))

        :param handlers: Handler
        :return:
        """

        if handlers:
            return handlers.pop(0)(cls.generate(handlers))