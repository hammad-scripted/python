from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Class
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "Kick-starting the bike!"

# my_vehicle = Vehicle() # ❌ Error: Cannot instantiate abstract class directly
my_bike = Bike()
print(my_bike.start_engine()) #  Output: Kick-starting the bike!
from abc import ABC, abstractmethod

# 1. Define the Abstract Base Class (The Blueprint)
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount: float):
        """Abstract method; subclasses must implement this."""
        pass

    def generate_receipt(self, amount: float):
        """Concrete method; shared logic across all subclasses."""
        print(f"Receipt generated for ${amount}")


# 2. Implement Concrete Subclasses
class StripePayment(PaymentProcessor):
    def process_payment(self, amount: float):
        # Hidden complex API logic for Stripe goes here
        print(f"Processing ${amount} securely through Stripe API.")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        # Hidden complex API logic for PayPal goes here
        print(f"Processing ${amount} securely through PayPal API.")


# 3. Execution
if __name__ == "__main__":
    # Attempting to instantiate the abstract class directly will raise a TypeError:
    # client = PaymentProcessor() 
    
    # Using the concrete implementations instead:
    payment_1 = StripePayment()
    payment_1.process_payment(49.99)
    payment_1.generate_receipt(49.99)
    
    print("-" * 30)
    
    payment_2 = PayPalPayment()
    payment_2.process_payment(120.00)
    payment_2.generate_receipt(120.00)
