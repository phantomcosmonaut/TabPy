"""
This is the users page for the tabpy app 
http://myserver:9004/users
PUT and POST methods will return json data for javascript requests
"""

from tabpy.tabpy_server.handlers.management_handler import ManagementHandler
from tabpy.tabpy_server.handlers.base_handler import authentication_wrapper
from tabpy.utils import tabpy_user
from tabpy.tabpy_server.app.util import parse_pwd_file
import json


class UsersHandler(ManagementHandler):
    def initialize(self, app):
        super(UsersHandler, self).initialize(app)

    @authentication_wrapper
    def get(self):
        self.clear()
        self.items["users"] = self.get_users()
        self.render("users.html", items=self.items)

    @authentication_wrapper
    def post(self):
        """
        Will handle new user request. 
        Log messages written vicariously through tabpy_user function.
        """
        if self._process_user_request(option="add") == False:
            self.finish("Cannot Add User")

    @authentication_wrapper
    def put(self):
        """
        Will handle update user request. 
        Log messages written vicariously through tabpy_user function.
        """
        if self._process_user_request(option="update") == False:
            self.finish("Cannot Update User")

    def _process_user_request(self, option):
        """
        Scans the password file and then invokes tabpy_user function to add 
        or update user accordingly.
        """
        body = json.loads(self.request.body)

        if "TABPY_PWD_FILE" in self.tabpy_state.settings:
            succeeded, credentials = parse_pwd_file(
                self.tabpy_state.settings["TABPY_PWD_FILE"])
            if not succeeded:
                return False 

            user_data = {
            f"{option}":True, 
            "--username": body["username"], 
            "--password": body["password"],
            }
            if tabpy_user.process_command(user_data, credentials):
                self.finish("User Added Successfully!")
                
        self.error_out(400, "No Password File in Settings.")
