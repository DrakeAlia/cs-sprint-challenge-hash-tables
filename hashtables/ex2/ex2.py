#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
     # Hash table to store route's airport source and destination info
    cache = {}
    # Initialize route array, to add to the original source airport
    route = [None] * length

    # Iterate thru each ticket and store it in its destination 
    for t in tickets:
        cache[t.source] = t.destination

    # First ticket along the route has a NONE source, start there
    dest = cache["NONE"]

    # Each ticket's next destination will be added to the destinations array
    # Flight is current ticket
    for flight in range(length):
        # Record the value of next destination
        route[flight] = dest
        # The next destination is the value, the key is the destination just added to the array 
        # The next flight in the trip, will continue until its completed
        dest = cache[dest]

    return route


# testing tickets:
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

length = len(tickets)

print(reconstruct_trip(tickets, length))

