class Ticket:
    counter = 0

    def __init__(self, staff_id, creator_name, contact_email, description, status):
        Ticket.counter += 1
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.status = status


class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, staff_id, creator_name, contact_email, description):
        new_ticket = Ticket(staff_id, creator_name, contact_email, description, "Open")
        self.tickets.append(new_ticket)
        print("Ticket created successfully!")

        if "Password Change" in description:
            new_password = self.generate_new_password(staff_id, creator_name)
            print("New Password:", new_password)

    def generate_new_password(self, staff_id, creator_name):
        new_password = staff_id[:2] + creator_name[:3]
        return new_password

    def show_tickets(self):
        for ticket in self.tickets:
            print("----------------------")
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Creator Name: {ticket.creator_name}")
            print(f"Contact Email: {ticket.contact_email}")
            print(f"Description: {ticket.description}")
            print(f"Status: {ticket.status}")

    def update_ticket_status(self, ticket_num, new_status):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_num:
                ticket.status = new_status
                print("Ticket status updated successfully!")
                return
        print("Invalid ticket number.")

    def respond_to_ticket(self, ticket_num, feedback):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_num:
                ticket.status = "Responded"
                print("Feedback added successfully!")
                print("Feedback:", feedback)
                return
        print("Invalid ticket number.")


class Ticket:
    counter = 0
    closed_tickets = 0

    def __init__(self, staff_id, creator_name, contact_email, description, status):
        Ticket.counter += 1
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.status = status
        self.feedback = ""

    def close_ticket(self):
        self.status = "Closed"
        Ticket.closed_tickets += 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.closed_tickets -= 1

    def provide_response(self, feedback):
        self.feedback = feedback


class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, staff_id, creator_name, contact_email, description):
        new_ticket = Ticket(staff_id, creator_name, contact_email, description, "Open")
        self.tickets.append(new_ticket)
        print("Ticket created successfully!")

        if "Password Change" in description:
            new_password = self.generate_new_password(staff_id, creator_name)
            print("New Password:", new_password)
            new_ticket.close_ticket()

    def generate_new_password(self, staff_id, creator_name):
        new_password = staff_id[:2] + creator_name[:3]
        return new_password

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.provide_response(f"New password: {new_password}")
            self.close_ticket()

    @classmethod
    def ticket_stats(cls):
        return {"Total Tickets": cls.counter,"Open Tickets": cls.counter - cls.closed_tickets,"Resolved Tickets": cls.closed_tickets}

    def submit_ticket(self, staff_id, creator_name, contact_email, description):
        new_ticket = Ticket(staff_id, creator_name, contact_email, description, "Open")
        self.tickets.append(new_ticket)
        print("Ticket submitted successfully!")

        new_ticket.resolve_password_change()

    def show_tickets(self):
        for ticket in self.tickets:
            print("----------------------")
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Creator Name: {ticket.creator_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Contact Email: {ticket.contact_email}")
            print(f"Description: {ticket.description}")
            print(f"Feedback: {ticket.feedback}")
            print(f"Status: {ticket.status}")

    def update_ticket_status(self, ticket_num, new_status):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_num:
                if new_status == "Reopened":
                    ticket.reopen_ticket()
                elif new_status == "Closed":
                    ticket.close_ticket()
                ticket.status = new_status
                print("Ticket status updated successfully!")
                return
        print("Invalid ticket number.")

    def reopen_ticket(self, ticket_num):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_num:
                ticket.reopen_ticket()
                print("Ticket reopened successfully!")
                return
        print("Invalid ticket number.")


def display_ticket_stats(self):
    num_tickets = len(self.tickets)
    num_open_tickets = num_tickets - Ticket.closed_tickets
    num_resolved_tickets = Ticket.closed_tickets

    print("\nTicket Statistics:")
    print("Total Tickets:", num_tickets)
    print("Open Tickets:", num_open_tickets)
    print("Resolved Tickets:", num_resolved_tickets)


# Creating Ticketing System

ticketing_system = TicketingSystem()

while True:
    print("\nWelcome to the Help Desk Ticketing System")
    print("0. Exit")
    print("1. Create a new ticket")
    print("2. Show all tickets")
    print("3. Update ticket status")
    print("4. Respond to a ticket")
    print("5. Display ticket stats")

    user_choice = input("Please enter your choice: ")

    if user_choice == "1":
        staff_id = input("Enter staff ID: ")
        creator_name = input("Enter your name: ")
        contact_email = input("Enter contact email: ")
        description = input("If you require a new password type Password Change: Enter description of the issue: ")

        ticketing_system.create_ticket(staff_id, creator_name, contact_email, description)

    elif user_choice == "2":
        ticketing_system.show_tickets()

    elif user_choice == "3":
        ticket_num = int(input("Enter the ticket number: "))
        new_status = input("Enter the new status: ")
        ticketing_system.update_ticket_status(ticket_num, new_status)

    elif user_choice == "4":
        ticket_num = int(input("Enter the ticket number: "))
        feedback = input("Enter feedback response (default: Not Yet Provided): ")

    elif user_choice == "5":
        ticketing_system.display_ticket_stats()

    elif user_choice == "0":
        break

    else:
        print("Invalid choice. Please try again.")