from .automatic_payments import make_automatic_payment_for_customer
from .customer_pipeline_pushes import (
    contact_the_customer_after_adding_address,
    contact_the_customer_after_adding_members,
    contact_the_customer_after_adding_schedule,
    contact_the_customer_after_registration,
)
from .customer_tasks import contact_the_customer
from .ondemand_tasks import (
    cancelled_on_demand_trip_task,
    check_bank_card_is_linked,
    new_on_demand_trip_task,
)
from .schedule_tasks import update_dynamic_prices
from .traccar import (
    connect_driver_to_traccar,
    deactivate_traccar_session_cookie,
    link_drivers_to_city_traccar_admin,
)
