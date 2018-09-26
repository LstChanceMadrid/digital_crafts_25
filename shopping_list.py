store_name = []




class ListManager:
    def __init__(self):
        self.grocery_lists = {}
        self.grocery_items = []
        

        print("hi")
    

    #USER INPUT OPTIONS
    def user_options(self):

        # Gives a set of options for the user to choose from
        selection = input(" Press 1. to create a new list, Press 2. to add a new item to the current list, Press 3. to view your current lists: ")


        # 1 creates a new list
        if (selection == '1'):
            self.create_new_list()

        # 2 adds items to the newly created list
        if (selection == '2'):
            self.add_items_to_list(self.new_list_name)

        # 3 prints the lists out in {key: [value]} format
        if (selection == '3'):
            self.view_list()

        # q exits the program
        if (selection == 'q'):
            print("Take Care!")
            exit()
        # prints out an error and prompts user options again
        else:
            print("That is an invalid option.")
            self.user_options()

    # TAKES USER INPUT AND CREATES A NEW LIST
    def create_new_list(self):

        new_list_name = input("Enter the name of your new list: ")

        self.grocery_lists[new_list_name] = []
        self.add_items_to_list(new_list_name)
    
    
    # ADDS ITEMS TO THE LIST
    def add_items_to_list(self, new_list_name):
        self.new_list_name = new_list_name
        item = input("Enter item name: ")
        self.grocery_lists[self.new_list_name].append(item)
        if (item == "q"):
            self.grocery_lists[self.new_list_name].remove(item)
            dictionary_list = self.grocery_items
            self.user_options()

        self.add_items_to_list(self.new_list_name)

    # PRINTS THE LISTS AND ITEMS
    def view_list(self):
        print(self.grocery_lists)

        self.user_options()




list_manager = ListManager()
list_manager.user_options()
