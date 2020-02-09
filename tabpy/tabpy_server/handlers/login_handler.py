"""
This is the login page for the tabpy app 
http://myserver:9004/login
"""

from tabpy.tabpy_server.handlers.management_handler import ManagementHandler
import logging
import json


class LoginHandler(ManagementHandler):
    def initialize(self, app):
        super(LoginHandler, self).initialize(app)

    def get(self):
        self.clear_all_cookies()
        self.clear()
        self.render("login.html", items=self.items)

    def post(self):
        body = json.loads(self.request.body)
        self.username = body["username"]
        self.password = body["password"]
        self.logger.log(logging.DEBUG, f"Attempted Sign-in by {self.username}")
        
        if self._validate_basic_auth_credentials():
            #Default cookie expiration is 30 days
            self.set_secure_cookie("username", self.username)
            self.set_secure_cookie("password", self.password)
            self.redirect("/")
        else:
            self.error_out(400, "Invalid username or password")
