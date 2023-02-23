from threading import current_thread,Thread

class FlightTicket:
    def __init__(self,AvailableSeats):
        self.AvailableSeats = AvailableSeats

    def reserve(self,BookSeat):
        if (self.AvailableSeats >= BookSeat):
            name = current_thread().name
            print(f'{self.AvailableSeats} seat is alloted for name {name}')
            self.AvailableSeats -= BookSeat
        else:
            print("All seats are alloted ")


f = FlightTicket(3)

t1 = Thread(target=f.reserve,args=(1,),name='AkashSonal')
t2 = Thread(target=f.reserve,args=(1,),name='SonalAkash')
t3 = Thread(target=f.reserve,args=(1,),name='Sonal')

t1.start()
t2.start()
t3.start()