from __future__ import absolute_import


class UploadContent(object):
    def __init__(self, content):
        self.content = content


class UploadFile(object):
    def __init__(self, path):
        self.path = path


"""
class UploadContent(str):
    """
    TODO: docstring
    """

    def __new__(cls, value):
        obj = str.__new__(cls, 'xxx')
        obj.raw_value = value
        return obj

    def field_tuple(self):
        # TODO: move to transport extension
        import pycurl
        return pycurl.FORM_CONTENTS, self.raw_value


class UploadFile(str):
    """
    TODO: docstring
    """

    def __new__(cls, path):
        obj = str.__new__(cls, 'xxx')
        obj.path = path
        return obj

    def field_tuple(self):
        # move to transport extension
        import pycurl
        return pycurl.FORM_FILE, self.path
"""
