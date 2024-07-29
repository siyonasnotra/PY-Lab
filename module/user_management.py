class User:
    def __init__(self, user_id, name, email, user_type='member'):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.user_type = user_type

class Member(User):
    def __init__(self, user_id, name, email, membership_type):
        super().__init__(user_id, name, email, user_type='member')
        self.membership_type = membership_type

class Staff(User):
    def __init__(self, user_id, name, email, position):
        super().__init__(user_id, name, email, user_type='staff')
        self.position = position

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]

# Example usage
if __name__ == "__main__":
    user_manager = UserManager()
    
    member = Member(1, "John Doe", "john@example.com", "gold")
    staff = Staff(2, "Jane Smith", "jane@example.com", "trainer")
    
    user_manager.add_user(member)
    user_manager.add_user(staff)
    
    print("All Users:", [user.name for user in user_manager.users])
    
    user = user_manager.get_user(1)
    print(f"Retrieved User: {user.name}, Type: {user.user_type}")
    
    user_manager.remove_user(1)
    print("All Users after removal:", [user.name for user in user_manager.users])
