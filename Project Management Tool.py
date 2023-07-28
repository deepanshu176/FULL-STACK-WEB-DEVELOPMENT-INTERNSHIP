class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def assign_task(self, task, assignee):
        assignee.tasks.append(task)
        print(f"{self.name} has assigned task '{task}' to {assignee.name}.")
    
    def display_tasks(self):
        if self.tasks:
            print(f"{self.name}'s tasks:")
            for task in self.tasks:
                print(task)
        else:
            print(f"{self.name} doesn't have any tasks.")
    
class ProjectManagementTool:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user):
        self.users[user.name] = user
    
    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            print(f"User '{name}' not found.")
    
    def display_users(self):
        print("Users:")
        for user_name in self.users:
            print(user_name)
    
    def run(self):
        while True:
            print("\n***** Project Management Tool *****")
            print("1. Add User")
            print("2. Assign Task")
            print("3. Display User's Tasks")
            print("4. Display Users")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                name = input("Enter user's name: ")
                user = User(name)
                self.add_user(user)
                print(f"User '{name}' added successfully!")
            
            elif choice == "2":
                assigner_name = input("Enter assigner's name: ")
                assigner = self.get_user(assigner_name)
                if assigner:
                    assignee_name = input("Enter assignee's name: ")
                    assignee = self.get_user(assignee_name)
                    if assignee:
                        task = input("Enter task description: ")
                        assigner.assign_task(task, assignee)
            
            elif choice == "3":
                user_name = input("Enter user's name: ")
                user = self.get_user(user_name)
                if user:
                    user.display_tasks()
            
            elif choice == "4":
                self.display_users()
            
            elif choice == "5":
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")
            

# Example usage
if __name__ == "__main__":
    tool = ProjectManagementTool()
    tool.run()
