from .service import PaymentService
from .processors import StripePaymentProcessor
from .notifiers import EmailNotifier, SMSNotifier  # noqa: F401
from .validators import CustomerValidator, PaymentDataValidator
from .loggers import TransactionLogger
from payment_service import service

if __name__ == "__main__":
    stripe_processor = StripePaymentProcessor()
    service = PaymentService(
        payment_processor=StripePaymentProcessor(),
        notifier=EmailNotifier(),
        customer_validator=CustomerValidator(),
        payment_validator=PaymentDataValidator(),
        logger=TransactionLogger(),
        recurring_processor=StripePaymentProcessor(),
        refund_processor=StripePaymentProcessor(),
    )