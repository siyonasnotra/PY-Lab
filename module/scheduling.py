from datetime import datetime

from user_management import Member

class ClassSchedule:
    def __init__(self, class_id, name, start_time, end_time, instructor):
        self.class_id = class_id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.instructor = instructor
        self.booked_members = []

    def book_member(self, member):
        self.booked_members.append(member)

class ScheduleManager:
    def __init__(self):
        self.schedules = []

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def get_schedule(self, class_id):
        for schedule in self.schedules:
            if schedule.class_id == class_id:
                return schedule
        return None

    def remove_schedule(self, class_id):
        self.schedules = [schedule for schedule in self.schedules if schedule.class_id != class_id]


if __name__ == "__main__":
    schedule_manager = ScheduleManager()
    
    class_schedule = ClassSchedule(1, "Yoga Class", datetime(2024, 7, 20, 8, 0), datetime(2024, 7, 20, 9, 0), "Jane Smith")
    schedule_manager.add_schedule(class_schedule)
    
    print("All Schedules:", [schedule.name for schedule in schedule_manager.schedules])
    
    schedule = schedule_manager.get_schedule(1)
    print(f"Retrieved Schedule: {schedule.name}, Instructor: {schedule.instructor}")
    
    member = Member (1, "John Doe", "john@example.com", "gold")
    schedule.book_member(member)
    print(f"Booked Members for {schedule.name}:", [member.name for member in schedule.booked_members])
    
    schedule_manager.remove_schedule(1)
    print("All Schedules after removal:", [schedule.name for schedule in schedule_manager.schedules])
