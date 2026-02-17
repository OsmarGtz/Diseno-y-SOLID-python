from .service import PaymentService
from .processors import StripePaymentProcessor
from .notifiers import EmailNotifier, SMSNotifier
from .validators import CustomerValidator, PaymentDataValidator
from .loggers import TransactionLogger
from payment_service import service
from payment_service.commons import CustomerData
from payment_service.notifiers import NotifierProtocol

def get_email_notifier() -> NotifierProtocol:
    return EmailNotifier()

def get_sms_notifier() -> NotifierProtocol:
    return SMSNotifier(gateway="SMSGatewayExample")

def get_notifier_implementation(custumer_data: CustomerData) -> NotifierProtocol:
    if custumer_data.email:
        return get_email_notifier()
    elif custumer_data.phone:
        return get_sms_notifier()
    else:
        raise Exception("no notifier implementation found")

if __name__ == "__main__":
    stripe_processor = StripePaymentProcessor()
    service = PaymentService(
        payment_processor=StripePaymentProcessor(),
        notifier=get_notifier_implementation(CustomerData()),
        customer_validator=CustomerValidator(),
        payment_validator=PaymentDataValidator(),
        logger=TransactionLogger(),
        recurring_processor=StripePaymentProcessor(),
        refund_processor=StripePaymentProcessor(),
    )