class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email to user@example.com")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS to 0812345678")


notifications = [
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send()