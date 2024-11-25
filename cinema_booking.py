class CinemaBooking():

	def __init__(self):

		self.movies = {

		'1': {'name': 'Inception', 'seats': 10},

		'2': {'name': 'The Matrix', 'seats': 8},

		'3': {'name': 'Interstellar', 'seats': 15}

		}

		self.bookings = {}

	def show_movies(self):

		print("\nAvailable Movies:")

		for movie_id, movie_info in self.movies.items():

			print(f"{movie_id}. {movie_info['name']} (Available seats: {movie_info['seats']})")
	
	def book_seat(self):

		self.show_movies()

		choice = input("\nEnter the movie number to book a seat: ")

		if choice in self.movies:

			if self.movies[choice]['seats'] > 0:

				name = input("Enter your name: ")

				self.movies[choice]["seats"] -= 1

				self.bookings[name] = self.movies[choice]["name"]

				print(f"\nSeat booked successfully for {name} in {self.movies[choice]['name']}.")

			else:

				print("Sorry, no seats available for this movie.")

		else:
		
			print("Invalid choice! Please try again.")

	def cancel_booking(self):
		
		name = input("\nEnter your name to cancel the booking: ")

		if name in self.bookings:

			movie_name = self.bookings[name]

			for movie_id, movie_info in self.movies.items():

				if movie_info["name"] == movie_name:

					self.movies[movie_id]["seats"] += 1

					break

			del self.bookings[name]
			
			print(f"\nBooking cancelled for {name}.")	

		else:
			
			print("No booking found under that name.")		

	def view_booking(self):
		
		name = input("\nEnter your name to view your booking: ")	

		if name in self.bookings:
			
			print(f"\n{name}, you have a seat booked for {self.bookings[name]}.")

		else:

			print("No booking found under that name.")

	def menu(self):
		
		while True:
			
			print("\n --- Cinema Booking Menu ---")

			print("1. View Movies")

			print("2. Book a seat")

			print("3. Cancel Booking")

			print("4. View Booking")

			print("5. Exit")

			choice = input("\nEnter your choice: ")

			if choice == "1":

				self.show_movies()

			elif choice == "2":

				self.book_seat()

			elif choice == "3":

				self.cancel_booking()	

			elif choice == "4":

				self.view_booking()		

			elif choice == "5":

				print("Thank you for using the cinema booking system!")	

				break

			else:

				print("Invalid choice! Please try again.")	

if __name__ == "__main__":
	
	cinema = CinemaBooking()

	cinema.menu()			

						

					

				
					

