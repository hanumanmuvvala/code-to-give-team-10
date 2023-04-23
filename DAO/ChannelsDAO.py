from __main__ import app
from models.Channels import Channels
from DAO.BaseDAO import BaseDAO
import logging
logger = logging.getLogger(__name__)

class ChannelsDAO():
    def __init__(self,model = None) -> None:
        self.model = model
        self.table = "channels"
    
    def create_channel(self):
        query = "INSERT INTO {} (`wish_maker`, `wish_coordinator`, `channel_name`, `status`) " \
                "VALUES ('{}', '{}', '{}', '{}')".format(self.table, self.model.wish_maker, self.model.wish_coordinator, self.model.channel_name,
                                                               self.model.status)
        if BaseDAO().insert(query):
            return True
        else:
            return False 
    
