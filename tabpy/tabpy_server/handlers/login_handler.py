"""
This is the login page for the tabpy app 
http://myserver:9004/login
"""

from tabpy.tabpy_server.handlers.management_handler import ManagementHandler
from tabpy.tabpy_server.app.SettingsParameters import SettingsParameters
from tabpy.tabpy_server.handlers.base_handler import authentication_wrapper
from tabpy.utils import tabpy_user
from tabpy.tabpy_server.app.util import parse_pwd_file
import logging


class LoginHandler(ManagementHandler):
    def initialize(self, app):
        super(LoginHandler, self).initialize(app)

    def get(self):
        self.clear()
        self.render("login.html", items=self.items)

    def post(self):
        self.username = self.get_argument("username")
        self.password = self.get_argument("password")
        self.logger.log(logging.DEBUG, f"Attempted Sign-in by {self.username}")

        if self._validate_basic_auth_credentials():
            #Default expiration is 30 days
            self.set_secure_cookie("username", self.username)
            self.set_secure_cookie("password", self.password)
            self.redirect("/")
        else:
            self.set_status(400, "Invalid username or password")
            self.redirect("/login")

    #may move to ./users/new_user
    @authentication_wrapper
    def put(self):
        """
        Will handle both new user request and update password request
        """
        if self._process_user_request(option="add") == False:
            if self._process_user_request(option="update") == False:
                self.set_status(400, "User not found.")
        self.redirect("/login")

    def _process_user_request(self, option):
        """
        Scans the password file and then invokes tabpy_user function to add user.
        """
        succeeded, credentials = parse_pwd_file(SettingsParameters["TABPY_PWD_FILE"])
        if not succeeded:
            return False 

        user_data = {
        f"{option}":True, 
        "--username":self.get_argument("username"), 
        "--password":self.get_argument("password"),
        }
        tabpy_user.process_command(user_data, credentials)
        return True
