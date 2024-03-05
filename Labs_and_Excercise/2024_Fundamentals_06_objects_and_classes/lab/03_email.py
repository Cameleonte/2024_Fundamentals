class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    command = input().split()
    if command[0] == "Stop":
        break
    sender, receiver, content = command
    email = Email(sender, receiver, content)
    emails.append(email)

sent_mails = [int(x) for x in input().split(', ')]

for index in sent_mails:
    if 0 <= index <= len(sent_mails):
        emails[index].send()

for email in emails:
    print(email.get_info())
