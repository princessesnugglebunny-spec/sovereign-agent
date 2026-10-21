from helpers.extension import Extension
from plugins._sov_connector.helpers.file_browser import Provider


class HostFolders(Extension):
    def execute(self, providers, **kwargs):
        providers[Provider.id] = Provider()
