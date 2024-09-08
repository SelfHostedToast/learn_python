class Privileges():

    def __init__(self, privileges=['can add posts', 'can delete own posts']):
        self.privileges = privileges

    def show_privileges(self):

        
        for privilege in self.privileges:
                print(f"\t-{privilege}")