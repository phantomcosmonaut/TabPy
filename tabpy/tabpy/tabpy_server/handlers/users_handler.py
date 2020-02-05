"""
This is the users page for the tabpy app 
http://myserver:9004/users
"""

from tabpy.tabpy_server.handlers.management_handler import ManagementHandler
from tabpy.tabpy_server.app.SettingsParameters import SettingsParameters
from tabpy.tabpy_server.handlers.base_handler import authentication_wrapper

import logging


class UsersHandler(ManagementHandler):
    def initialize(self, app):
        super(UsersHandler, self).initialize(app)

    @authentication_wrapper
    def get(self):
    	self.clear()
    	self.items["users"] = self.get_users()
    	self.render("users.html", items=self.items)