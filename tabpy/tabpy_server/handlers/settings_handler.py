"""
This is the settings page for the tabpy app 
http://myserver:9004/settings
"""

from tabpy.tabpy_server.handlers.management_handler import ManagementHandler
from tabpy.tabpy_server.handlers.base_handler import authentication_wrapper


class SettingsHandler(ManagementHandler):
    def initialize(self, app):
        super(SettingsHandler, self).initialize(app)

    @authentication_wrapper
    def get(self):
        self.clear()
        items = self.items
        items["settings"] = self.settings
        self.render("settings.html", items=items)
