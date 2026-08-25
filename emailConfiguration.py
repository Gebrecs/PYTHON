import datetime


# Represents a single email
class Email:

    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

        # Save the current date and time when the email is created
        self.timestamp = datetime.datetime.now()

        # New emails start as unread
        self.read = False

    # Mark this email as read
    def mark_as_read(self):
        self.read = True

    # Display the complete contents of the email
    def display_full_email(self):
        # Reading an email automatically marks it as read
        self.mark_as_read()

        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # Controls how an email looks when we print it
    def __str__(self):
        # Show Read or Unread depending on the current status
        status = 'Read' if self.read else 'Unread'

        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# Represents a person who can send and receive emails
class User:

    def __init__(self, name):
        self.name = name

        # Every user gets their own inbox
        self.inbox = Inbox()

    # Create and send an email to another user
    def send_email(self, receiver, subject, body):

        # Create an Email object
        email = Email(
            sender=self,
            receiver=receiver,
            subject=subject,
            body=body
        )

        # Put the email into the receiver's inbox
        receiver.inbox.receive_email(email)

        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Display all emails in the user's inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # Read a specific email
    def read_email(self, index):
        self.inbox.read_email(index)

    # Delete a specific email
    def delete_email(self, index):
        self.inbox.delete_email(index)


# Represents a user's inbox
class Inbox:

    def __init__(self):
        # Store all received emails in a list
        self.emails = []

    # Add a received email to the inbox
    def receive_email(self, email):
        self.emails.append(email)

    # Display a list of emails in the inbox
    def list_emails(self):

        # Check whether the inbox is empty
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')

        # enumerate gives us both the email number and the email itself
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # Read an email using its number
    def read_email(self, index):

        # Check whether the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Users count emails starting from 1,
        # but Python list indexes start from 0
        actual_index = index - 1

        # Make sure the selected number is valid
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Display the selected email
        self.emails[actual_index].display_full_email()

    # Delete an email using its number
    def delete_email(self, index):

        # Check whether the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Convert the user's number to a Python list index
        actual_index = index - 1

        # Make sure the selected number is valid
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Remove the selected email from the list
        del self.emails[actual_index]

        print('Email deleted.\n')


# Main function where we test the email system
def main():

    # Create two users an example
    gebremariam = User('Gebremariam Godad')
    ezra = User('Ezra Destaw')

    # ለ እዝራ እየላኩለት ነው አሁን
    gebremariam.send_email(
        ezra,
        'Hello',
        'Hi Ezra Destaw, just saying hello!'
    )

    # እዝራ ለገብረማሪያም ሲመልስ
    ezra.send_email(
        gebremariam,
        'Re: Hello',
        'Hi ገብረማሪያም, hope you are fine.'
    )

    # email  መግባቱን እያረጋገተ ነው
    ezra.check_inbox()

    # እዝራ የመጀመሪያውን email ሲያነብ ()
    ezra.read_email(1)

    # ካነበበው በኋላ አጠፋው(🤣🤣🤣)
    ezra.delete_email(1)

    # እዝራ አዲስ email ገብቶ እንደሆነ ብሎ ..(image.png)
    ezra.check_inbox()


# Run main() only when this file is executed directly
if __name__ == '__main__':
    main()