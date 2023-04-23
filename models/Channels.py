class Channels:
    def __init__(self, wish_maker= "", wish_coordinator= "", channel_name = "", status='Active'):
        self.wish_maker = wish_maker
        self.wish_coordinator = wish_coordinator
        self.channel_name = channel_name
        self.status = status

    # def __str__(self):
    #     return f'FirstName:{self.first_name}, LastName:{self.last_name}, Email:{self.email}, created:{self.created}, updated:{self.updated}, role:{self.role}, city:{self.city}'
    def __str__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {'wish_maker': self.wish_maker, 'wish_coordinator': self.wish_coordinator, 
                'channel_name': self.channel_name, 'status': self.status}