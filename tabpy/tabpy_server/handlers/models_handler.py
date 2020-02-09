"""
This is the models page for the tabpy app 
http://myserver:9004/models
It acts as the webpage version of the endpoints handler
"""
from tabpy.tabpy_server.handlers import ManagementHandler
from tabpy.tabpy_server.handlers.base_handler import authentication_wrapper


class ModelsHandler(ManagementHandler):
    def initialize(self, app):
        super(ModelsHandler, self).initialize(app)

    @authentication_wrapper
    def get(self):
    	self.clear()
    	items = self.items
    	items["models"] = self.tabpy_state.get_endpoints()
    	self.render("models.html", items=items)