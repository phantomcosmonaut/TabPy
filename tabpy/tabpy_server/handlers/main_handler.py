"""
This is the index page for the tabpy app 
http://myserver:9004/
"""

from tabpy.tabpy_server.handlers.management_handler import ManagementHandler
from tabpy.tabpy_server.handlers.base_handler import authentication_wrapper


class MainHandler(ManagementHandler):
    def initialize(self, app):
        super(MainHandler, self).initialize(app)


    @authentication_wrapper
    def get(self):
        self.clear()
        self.render("index.html", items=self.items)
