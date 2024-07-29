from user_management import UserManager, Member, Staff
from scheduling import ScheduleManager, ClassSchedule
from billing import BillingManager, MembershipPlan, Payment

def main():
    
    user_manager = UserManager()
    member = Member(1, "John Doe", "john@example.com", "gold")
    staff = Staff(2, "Jane Smith", "jane@example.com", "trainer")
    user_manager.add_user(member)
    user_manager.add_user(staff)
    print("All Users:", [user.name for user in user_manager.users])
    
  
    schedule_manager = ScheduleManager()
    class_schedule = ClassSchedule(1, "Yoga Class", "2024-07-20 08:00", "2024-07-20 09:00", "Jane Smith")
    schedule_manager.add_schedule(class_schedule)
    print("All Schedules:", [schedule.name for schedule in schedule_manager.schedules])
    
   
    billing_manager = BillingManager()
    plan = MembershipPlan(1, "Gold Plan", 50)
    billing_manager.add_membership_plan(plan)
    payment = Payment(1, 1, 50, "2024-07-15")
    billing_manager.add_payment(payment)
    print(f"Payments for Member 1:", [payment.amount for payment in billing_manager.get_payments_for_member(1)])

if __name__ == "__main__":
    main()
