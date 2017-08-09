import datetime

class Call(object):
    def __init__ (self, id, name, phone_number, reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        self.reason = reason

    def display(self):
        print "id: ", self.id
        print 'Name: ', self.name
        print 'Phone#: ', self.phone_number
        print 'Time of call: ', self.time
        print 'Reason for call: ', self.reason

class CallCenter(object):
    def __init__ (self):
        self.calls = []
        self.queue_size = len(self.calls)

    def add(self, new_call):
        self.calls.append(new_call)

    def remove(self):
        self.calls.pop(0)

    def info(self):
        for i in range(len(self.calls)):
            print self.calls[i][0]
            print self.calls[i][1]

call1 = Call(1, 'Frank', '416-777-1234', 'Quote')
call2 = Call(2, 'Bob', '647-222-2222', 'Claim')
call3 = Call(3, 'Ed', '905-456-3214', 'Update Info')
call4 = Call(4, 'Sanchez', '619-345-6789', 'Claim')

today = CallCenter()
today.add(call1)
today.add(call2)
today.add(call3)
today.add(call4)
today.info()