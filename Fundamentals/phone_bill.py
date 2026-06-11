MONTHLY_FREE_MINUTES = 60
MONTLY_FREE_MESSAGES = 20
ADDITIONAL_PRICE_PER_MINUTE = 0.10
ADDITIONAL_PRICE_PER_MESSAGE = 0.06
MONTHLY_PLAN_PRICE = 12
SALES_TAX_PERCENT = 0.2

total_messages = int(input())
total_minutes = int(input())

additional_messages = 0
additional_messages_cost = 0
additional_minutes = 0
additional_minutes_cost = 0

if total_messages - MONTLY_FREE_MESSAGES > 0:
    additional_messages = total_messages - MONTLY_FREE_MESSAGES
    
    additional_messages_cost = additional_messages * ADDITIONAL_PRICE_PER_MESSAGE

if total_minutes - MONTHLY_FREE_MINUTES > 0:
    additional_minutes = total_minutes - MONTHLY_FREE_MINUTES
    additional_minutes_cost = additional_minutes * ADDITIONAL_PRICE_PER_MINUTE

total_additional_cost = additional_messages_cost + additional_minutes_cost
sales_tax = total_additional_cost * SALES_TAX_PERCENT
total_bill = MONTHLY_PLAN_PRICE + sales_tax + total_additional_cost

print(f"{additional_messages} additional messages for {additional_messages_cost:.2f} levas")
print(f"{additional_minutes} additional minutes for {additional_minutes_cost:.2f} levas")
print(f"{sales_tax:.2f} additional taxes")
print(f"{total_bill:.2f} total bill")

