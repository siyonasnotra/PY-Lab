class MembershipPlan:
    def __init__(self, plan_id, name, price):
        self.plan_id = plan_id
        self.name = name
        self.price = price

class Payment:
    def __init__(self, payment_id, member_id, amount, date):
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.date = date

class BillingManager:
    def __init__(self):
        self.membership_plans = []
        self.payments = []

    def add_membership_plan(self, plan):
        self.membership_plans.append(plan)

    def get_membership_plan(self, plan_id):
        for plan in self.membership_plans:
            if plan.plan_id == plan_id:
                return plan
        return None

    def add_payment(self, payment):
        self.payments.append(payment)

    def get_payments_for_member(self, member_id):
        return [payment for payment in self.payments if payment.member_id == member_id]

# Example usage
if __name__ == "__main__":
    billing_manager = BillingManager()
    
    plan = MembershipPlan(1, "Gold Plan", 50)
    billing_manager.add_membership_plan(plan)
    
    print("All Membership Plans:", [plan.name for plan in billing_manager.membership_plans])
    
    payment = Payment(1, 1, 50, "2024-07-15")
    billing_manager.add_payment(payment)
    
    print(f"Payments for Member 1:", [payment.amount for payment in billing_manager.get_payments_for_member(1)])
