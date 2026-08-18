class Seat():
    def __init__(self, seat_number):
        self.seat_number=seat_number
        self.is_booked=False
    def mark_booked(self):
        self.is_booked=True
    def is_available(self):
        return not self.is_booked
    def cancel_ticket(self):
        self.is_booked=False
        
class Movie:
    def __init__(self, name, showtime, price):
        self.name=name
        self.showtime=showtime
        self.price=price
        self.seats=[Seat(i) for i in range(1, 101)]

class Theater():
    def __init__(self, theater_name):
        self.theater_name=theater_name
        self.movies=[
                     Movie("Spiderman", "Morning" ,120),
                     Movie("Dragon", "Afternoon", 120),
                     Movie("Lucy", "Evening", 120)
                    ]
class Customer:
    def book_seats(self, theater, nam):
        movie_found=False
        for find in theater.movies:
            if find.name==nam:
                movie_found=True
                seat_booked=False
                for seat in find.seats:
                    if seat.is_available():
                        seat.mark_booked()
                        self.movie=find
                        self.seat=seat
                        seat_booked=True
                        return find, seat
                        
                if not seat_booked:
                    print("Housefull")
                    return None, None
        if not movie_found:
            print("No movie")
            return None, None
        
class Booking(Customer):
    def __init__(self, movie, seat):

        self.movie=movie
        self.seat=seat
        self.is_paid=False

    def make_payment(self):
        self.is_paid=True
        
    def cancel_ticket(self):
        self.seat.cancel_ticket()
        print("Ticket cancalled for", self.movie.name, "- Seat ", self.seat.seat_number)
        self.seat=None
        self.movie=None

t=Theater("National Theater")
all_bookings=[]

print("Welcome to National Theater")
while True:
    
    choice=int(input("1. View Movies || 2. Book Seats || 3. Cancel Ticket || 4. Payment || 0. Exit: "))
    if choice == 1:
        for movie in t.movies:
            print(movie.name, " - " , movie.showtime, " - ", movie.price) 

    if choice == 2:
        nam=input("Enter the name of the movie to book: ")
        num_seat=int(input("Please enter the number of seats to book: "))
        new=[]
        for i in range(num_seat):
            movie, seat = Customer().book_seats(t, nam)
            if movie is not None and seat is not None:
                new_booking=Booking(movie, seat)
                all_bookings.append(new_booking)
                new.append(new_booking)
            else:
                break

        if len(new)>0:
            print(len(new), "seats booked for", nam)
            pay=input("pay now? (y/n): ")
            if pay=="y":
                for n in new:
                    n.make_payment()
                print("Payment successful for", len(new), "tickets")
    if choice == 3:
        if len(all_bookings)==0:
            print("No booking")
            
        else:
            for i in range(len(all_bookings)):
                print(i + 1, " - ", all_bookings[i].movie.name, "Seat", all_bookings[i].seat.seat_number)
            pick=int(input("Enter the booking number to cancel: "))
            if pick<1 or pick>len(all_bookings):
                print("Invalid booking number")
            else:

                selected=all_bookings[pick-1]
                selected.cancel_ticket()
                all_bookings.remove(selected)

    if choice == 4:
        if len(all_bookings)==0:
            print("Please book to pay")
        else:
            for i in range(len(all_bookings)):
                print(i + 1, " - ", all_bookings[i].movie.name, "Seat", all_bookings[i].seat.seat_number)
            pick=int(input("Enter the booking number to pay: "))
            selected=all_bookings[pick-1]
            if selected.is_paid:
                print("You have already paid")
            else:
                selected.make_payment()
                print("Ticket booked for", selected.movie.name, "payment success")


    if choice == 0:
        print("Thank you")
        break