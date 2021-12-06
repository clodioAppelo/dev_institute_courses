# Air Management System
# Your goal is to build an airplanes traffic management system.
#
# 3) Airport
# Methods:

# schedule_flight(self, destination, datetime) This method finds when an available airplane from an airline that serve the origine and the destination and schedule a flight for it.
# info(self, start_date, end_date) Display every scheduled flight from start_date to end_date.
# You are free to add any class/method/attribute to your code, be sure to document everything you write.

# Write a small code to test your program.


# Your program should rely on four classes: Company, Airplane, Flight and Airport.

from typing import List
import datetime


# class Company:
#     def __init__(self, id: int, name: str, planes: List) -> None:
#         self.id = id
#         self.name = name
#         self.planes = planes
#
#
# class Airplane:
#     def __init__(self, id: int, current_location: Airport, company: Company, next_flights: list):
#         self.id = id
#         self.current_location = current_location
#         self.company = company
#         self.next_flights = next_flights
#
#     def fly(self, destination):
#         pass
#
#     def location_on_date(self, date):
#         return self.current_location
#
#     def available_on_date(self, date, location):
#         if self.current_location == location == self.next_flights is None:
#             return True
#
#
# class Flght:
#     def __init__(self, date, destination, origin, plane, id) -> None:
#         self.date = date
#         self.destination = destination
#         self.origin = origin
#         self.plane = plane
#         self.id = id
#
#     def take_off(self):
#         return f"the flight {id } is about to take off"
#
#     def land(self, destination):
#         Airplane.current_location = destination
#         return f" the flight {id} is landing"
#
#
# class Airport:
#     def __init__(self, city: str, planes: list, scheduled_flights: list, scheduled_arrivals: list):
#         self.city = city
#         self.planes = planes
#         self.scheduled_flights = scheduled_flights
#         self.scheduled_arrivals = scheduled_arrivals
#
#     def schedule_flight(self, destination, datetime):
#         if plane is self.planes:
#             if datetime not in plane.next_flights.date:
#                 new_flight = Flight(datetime, destination,
#                                     plane.current_location, plane, plane.id)
#                 plane.next_flights.append(new_flight)
#
#     def info(self, start_date, end_date):
#         for flight in self.scheduled_departures:
#             if flight.date >= start_date and flight.date <= end_date:
#                 print(flight.id)
import datetime


class Company:

	def __init__(self, company_id: str, name: str):
		self.__company_id = company_id
		self.__name = name
		self.__planes = None

	def add_plane(self, plane):
		self.__planes.append(plane)


class Airport:

	def __init__(self, city: str):
		self.__city = city

		self.__planes = None
		self.__scheduled_departures = None
		self.__scheduled_arrivals = None

	def add_plane(self, plane):
		self.__planes.append(plane)

	def schedule_flight(self, destination, datetime):
		pass

	def info(self, start_date, end_date):
		pass


class Airplane:

	def __init__(self, airplane_id: int, current_location: Airport, company: Company):
		self.airplane_id = airplane_id
		self.current_location = current_location
		self.company = company

		self.next_flights = None
		# self.next_flights = next_flights.sorted(datetime)

	def fly(self, destination) -> None:
		self.current_location = destination
		self.next_flights.pop(0)

	def location_on_date(self, date) -> datetime.date:
		for flight in self.next_flights:
			if flight.date == date:
				return flight.origin_airport

	def available_on_date(self, date, location) -> bool:
		future_location = self.location_on_date(date)

		# if future_location == location:
		# 	return True
		# else:
		# 	return False

		return future_location == location


class Flight:

	def __init__(self, date: datetime.date, destination: Airport, origin: Airport, plane: Airplane, id: str):
		self.date = date
		self.destination_airport = destination
		self.origin_airport = origin
		self.plane = plane

	def take_off(self):
		self.plane.current_location = self.origin_airport

	def land(self):
		self.plane.current_location = self.destination_airport


# creating airports
tlv_airport = Airport("TLV")
usa_airport = Airport("USA")

# creating the company
el_al = Company(company_id="c1", name="EL AL")

# creating airplane
el_al_1 = Airplane(airplane_id=1, current_location=tlv_airport, company=el_al)

d1 = datetime.date(2021, 12, 6)
usa_12_6 = Flight(date=d1, destination=usa_airport, origin=tlv_airport, plane=el_al_1, id="usa_12_6")


el_al.add_plane(plane=el_al_1)