class Configuration:
    """Configuration Class for Initializing Application Parameters"""

    _uniqueInstance = None

    def __new__(cls, *args, **kwargs):
        if not cls._uniqueInstance:
            cls._uniqueInstance = super().__new__(cls, *args, **kwargs)

        return cls._uniqueInstance

    def __init__(self):
        self._API_SERVER_URL = "http://data.sfgov.org/resource/bbb8-hzi6.json"
        self._RECORDS_PER_PAGE = 10

    def getApiServer(self):
        return self._API_SERVER_URL

    def getRecordsPerPage(self):
        return self._RECORDS_PER_PAGE
