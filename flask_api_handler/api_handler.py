from flask import Flask


class ApiHandler(object):
    """
        A Helper class to abstract the Flask endpoint creation

    """

    def __init__(self, app):
        """

        Args:
            app(Flask): The flask app instance

        """
        self.app = app

    def add_handler(self, url, cls, methods=None):
        """
            Add the Handler with the correct form to the flask app

        Args:
            url: The endpoint
            cls: The Handler
            methods (list): Allowed Methods (['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])

        Returns:
            None
        """
        methods = methods if methods is not None else ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

        for m in methods:
            if not self._have_method(cls, m):
                continue
            method = m.upper()
            action = getattr(cls, m.lower())
            name = "{class_name}.{method}".format(class_name=cls.__name__, method=m.lower())
            self.app.add_url_rule(url, name, action, methods=[method])

    @staticmethod
    def _have_method(class_name, method):
        """

        Args:
            class_name: The name of the class
            method: The method needed to be checked

        Returns:
            bool: True in case there is a method with the given name to the class passed
        """
        method = method.lower()
        return hasattr(class_name, method) and callable(getattr(class_name, method))
