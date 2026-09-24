class Delivery:
    def __init__(self,order_id, destination):
        self.order_id = order_id
        self.destination = destination
    def deliver(self):
        print(f"Delivering {self.order_id} to {self.destination}")
class Trackable:
    def track(self):
        print(f"Tracking order {self.order_id}")
class StandardDelivery(Delivery):
    def deliver(self):
        print(f"Order {self.order_id} will arrive in {self.destination}")
class ExpressDelivery(Delivery,Trackable):
    def deliver(self):
        print(f"Order {self.order_id} will arrive within {self.destination}")
standard = StandardDelivery("D234","3-5 days")
express = ExpressDelivery("D122","24 hours")
deliveries = [standard,express]
for delivery in deliveries:
    delivery.deliver()
express.track()