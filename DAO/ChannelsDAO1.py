from DAO.BaseDAO import BaseDAO
def get_channel_wishmaker(wish_maker):
    print("Querying for wsihmaker")
    query = f"select channel_name from channels where wish_maker = '{wish_maker}' and status ='Active'"
    print(query)
    return BaseDAO().get(query)[0]
    
def get_channel_wishcoordinator(wish_coordinator):
    query = "select channel_name from channels where wish_coordinator = {} and status = {}".format(wish_coordinator,'Active')
    return BaseDAO().get(query)[0]