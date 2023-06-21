
class Ticket:
    def __init__(self, staff_id, creator_name, contact_email, description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = None

    def submit_ticket(self):
        # Assign ticket number automatically using the counter static field plus 2000.
        # All information must be provided as input while submitting the ticket.
        self.ticket_number = Ticket.counter + 2000
        Ticket.counter += 1

    def respond_to_ticket(self):
        # If the ticket’s description of the issue contains the words “Password Change”,
        # the new password should be generated following the rule,
        # The first two characters of the staffID, followed by the first three characters of the ticket creator name.
        if "Password Change" in self.description:
            new_password = f"{self.staff_id[:2]}{self.creator_name[:3]}"
            return new_password

    counter = 1


class TicketStats:
    def __init__(self):
        self.tickets_created = 0
        self.tickets_resolved = 0
        self.tickets_open = 0

    def increment_created(self):
        self.tickets_created += 1

    def increment_resolved(self):
        self.tickets_resolved += 1

    def increment_open(self):
        self.tickets_open += 1

    def decrement_open(self):
        self.tickets_open -= 1

    def decrement_resolved(self):
        self.tickets_resolved -= 1

    def print_stats(self):
        print(f"Tickets Created: {self.tickets_created}")
        print(f"Tickets Resolved: {self.tickets_resolved}")
        print(f"Tickets To Solve: {self.tickets_open}")


if __name__ == "__main__":
    ticket_stats = TicketStats()
    tickets = [
        Ticket("staff_id_1", "creator_name_1", "contact_email_1", "Password Change"),
        Ticket("staff_id_2", "creator_name_2", "contact_email_2", "Request for a videocamera to conduct webinars"),
        Ticket("staff_id_3", "creator_name_3", "contact_email_3", "My monitor stopped working"),
    ]
    for ticket in tickets:
        ticket.submit_ticket()
        ticket_stats.increment_created()

    password_change_ticket = tickets[0]
    new_password = password_change_ticket.respond_to_ticket()
    print(f"New password generated: {new_password}")

    ticket_stats.print_stats()


class Ticket:
    counter = 0

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = Ticket.counter + 2000
        Ticket.counter += 1

    def __str__(self):
        return f"Ticket Number: {self.ticket_number}\nTicket Creator: {self.creator_name}\nStaff ID: {self.staff_id}\nEmail Address: {self.contact_email}\nDescription: {self.description}\nResponse: Not Yet Provided\nTicket Status: Open"

    def generate_password(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            return new_password


class HelpDesk:
    tickets = []
    resolved_tickets = []
    open_tickets = []

    @classmethod
    def submit_ticket(cls, ticket):
        cls.tickets.append(ticket)
        cls.open_tickets.append(ticket)

    @classmethod
    def respond_to_ticket(cls, ticket_number, response):
        for ticket in cls.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.response = response
                if "Password Change" in ticket.description:
                    ticket.response += f"\nNew password generated: {ticket.generate_password()}"
                    cls.close_ticket(ticket)
                else:
                    cls.resolve_ticket(ticket)

    @classmethod
    def close_ticket(cls, ticket):
        cls.resolved_tickets.append(ticket)
        cls.open_tickets.remove(ticket)

    @classmethod
    def resolve_ticket(cls, ticket):
        cls.resolved_tickets.append(ticket)
        cls.open_tickets.remove(ticket)

    @classmethod
    def reopen_ticket(cls, ticket):
        cls.resolved_tickets.remove(ticket)
        cls.open_tickets.append(ticket)

    @classmethod
    def display_ticket(cls, ticket_number):
        for ticket in cls.tickets:
            if ticket.ticket_number == ticket_number:
                print(
                    f"Ticket Number: {ticket.ticket_number}\nTicket Creator: {ticket.creator_name}\nStaff ID: {ticket.staff_id}\nEmail Address: {ticket.contact_email}\nDescription: {ticket.description}\nResponse: {ticket.response}\nTicket Status: {'Open' if ticket in cls.open_tickets else 'Closed' if ticket in cls.resolved_tickets else 'Reopened'}")
                break


if __name__ == "__main__":
    # Create tickets
    t1 = Ticket("1234", "John Doe", "johndoe@example.com", "Password Change")
    t2 = Ticket("5678", "Jane Doe", "janedoe@example.com", "My monitor stopped working")
    t3 = Ticket("9012", "Bob Smith", "bobsmith@example.com", "Request for a videocamera to conduct webinars")

    # Submit tickets and display statistics
    HelpDesk.submit_ticket(t1)
    HelpDesk.submit_ticket(t2)
    HelpDesk.submit_ticket(t3)
    print(
        f"Tickets Created: {len(HelpDesk.tickets)}\nTickets Resolved: {len(HelpDesk.resolved_tickets)}\nTickets To Solve: {len(HelpDesk.open_tickets)}")

    # Respond to tickets and display statistics and tickets
    HelpDesk.respond_to_ticket(t1.ticket_number, "Not Yet Provided")
    HelpDesk.respond_to_ticket(t2.ticket_number, "The monitor has been replaced.")
    HelpDesk.respond_to_ticket(t3.ticket_number, "Not Yet Provided")
    print(
        f"Tickets Created: {len(HelpDesk.tickets)}\nTickets Resolved: {len(HelpDesk.resolved_tickets)}\nTickets To Solve: {len(HelpDesk.open_tickets)}")

    HelpDesk.reopen_ticket(t2)

    HelpDesk.display_ticket(t1.ticket_number)

class Ticket:
    def __init__(self, ticket_number, ticket_creator_name, staff_id, email_address, description_of_issue,
                 response_from_it_department, ticket_status):
        self.ticket_number = ticket_number
        self.ticket_creator_name = ticket_creator_name
        self.staff_id = staff_id
        self.email_address = email_address
        self.description_of_issue = description_of_issue
        self.response_from_it_department = response_from_it_department
        self.ticket_status = ticket_status

    def display_ticket_information(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Name of the ticket’s creator: {self.ticket_creator_name}")
        print(f"StaffID: {self.staff_id}")
        print(f"Email address: {self.email_address}")
        print(f"Description of the issue: {self.description_of_issue}")
        print(f"Response from the IT department: {self.response_from_it_department}")
        print(f"Ticket status (open, closed or reopened): {self.ticket_status}")


ticket1 = Ticket(2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working", "Not Yet Provided",
                 "Open")
ticket2 = Ticket(2002, "Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars",
                 "Not Yet Provided", "Open")
ticket3 = Ticket(2003, "John", "JOHNS", "john@whitecliffe.co.nz", "Password change", "New password generated: JOJoh",
                 "Closed")

print("Displaying Ticket Information")
print()
ticket1.display_ticket_information()
print()
ticket2.display_ticket_information()
print()
ticket3.display_ticket_information()


class Ticket:
    def __init__(self, staff_id, creator_name, contact_email, description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = None

    def submit_ticket(self):
        # Assign ticket number automatically using the counter static field plus 2000.
        self.ticket_number = Ticket.counter + 2000
        Ticket.counter += 1

    def __str__(self):
        return f"Ticket Number: {self.ticket_number}\nName of the ticket’s creator: {self.creator_name}\nStaffID: {self.staff_id}\nEmail address: {self.contact_email}\nDescription of the issue: {self.description}"


class HelpDeskTicketingSystem:
    def __init__(self):
        self.tickets = []
        self.closed_tickets = []
        self.open_tickets = []

    def submit_ticket(self, ticket):
        ticket.submit_ticket()
        self.tickets.append(ticket)
        self.open_tickets.append(ticket)

    def respond_to_ticket(self, ticket, response):
        if "Password Change" in ticket.description:
            new_password = ticket.staff_id[:2] + ticket.creator_name[:3]
            response += f"\nNew password generated: {new_password}"
            ticket.description += response
            ticket.status = "Closed"
            self.closed_tickets.append(ticket)
            self.open_tickets.remove(ticket)
            return

        ticket.description += response
        if "Not Yet Provided" not in response:
            ticket.status = "Closed"
            self.closed_tickets.append(ticket)
            self.open_tickets.remove(ticket)

    def reopen_ticket(self, ticket):
        if ticket.status == "Closed":
            ticket.status = "Reopened"
            self.closed_tickets.remove(ticket)
            self.open_tickets.append(ticket)

    def display_ticket(self, ticket):
        print(ticket)


if __name__ == "__main__":
    system = HelpDeskTicketingSystem()
    t1 = Ticket("1234", "John Doe", "johndoe@example.com", "Password Change")
    t2 = Ticket("5678", "Jane Doe", "janedoe@example.com", "My monitor stopped working")
    t3 = Ticket("9012", "Bob Smith", "bobsmith@example.com", "Request for a videocamera to conduct webinars")

    print("Displaying Ticket Statistics")
    print(f"Tickets Created: {len(system.tickets)}")
    print(f"Tickets Resolved: {len(system.closed_tickets)}")
    print(f"Tickets To Solve: {len(system.open_tickets)}")

    print("\nPrinting Tickets:")
    for t in system.tickets:
        system.display_ticket(t)

    system.respond_to_ticket(t1, "\nNew password generated.")
    system.respond_to_ticket(t2, "\nThe monitor has been replaced.")
    system.respond_to_ticket(t3, "\nNot Yet Provided.")

    print("\nDisplaying Ticket Statistics")
    print(f"Tickets Created: {len(system.tickets)}")
    print(f"Tickets Resolved: {len(system.closed_tickets)}")
    print(f"Tickets To Solve: {len(system.open_tickets)}")

    print("\nPrinting Tickets:")
    for t in system.tickets:
        system.display_ticket(t)

