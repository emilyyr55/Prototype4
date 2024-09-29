###################################################################################################

from typing import List, Dict
from UML_MANAGER.uml_core_manager import UMLCoreManager as Manager, InterfaceOptions

###################################################################################################

class UMLCommandLineInterface:
    
    # Constructor for interface #
    def __init__(self):
        # Each interface instance has its own program manager, easier for testing
        self.ProgramManager = Manager()
        
    #################################################################
    ### INTERFACE FUNCTIONS THAT CONNECT WITH THE MANAGER ###
    
    ## OBJECT CREATION ##
    
    # Class creation method interface #
    def create_class(self, class_name: str):
        return self.ProgramManager.create_class(class_name)
    
    # Field creation method interface #
    def create_field(self, field_name: str):
        return self.ProgramManager.create_field(field_name)
    
    # Method creation method interface #
    def create_method(self, method_name: str):
        return self.ProgramManager.create_method(method_name)
    
    # Parameter creation method interface #
    def create_parameter(self, parameter_name: str):
        return self.ProgramManager.create_parameter(parameter_name)
    
    # Relationship creation method interface #
    def create_relationship(self, source_class: str, destination_class: str, rel_type: str):
        return self.ProgramManager.create_relationship(source_class, destination_class, rel_type)
    
    ## DATA RELATED FOR GUI AND TESTING ##

    # Get main data interface #
    def get_main_data(self) -> Dict:
        return self.ProgramManager._get_main_data()
    
    # Get relationship list interface #
    def get_relationship_list(self) -> List:
        return self.ProgramManager._get_relationship_list()
    
    # Get storage manager interface #
    def get_storage_manager(self):
        return self.ProgramManager._get_storage_manager()
    
    # Extract and and a list of UML class data interface #
    """class_data can be retrieved using get_main_data()
       main_data =  get_main_data()
       class_data = main_data["classes"]
    """
    def extract_class_data(self, class_data: List[Dict]) -> List: 
        return self.ProgramManager._extract_class_data(class_data)
    
    # This one is for Testing, you can check whether 
    # Class, Field, Method, or Parameter exist or not
    # Check uml_core_manager.py to see how to use this function
    # You can find it in _add_class, _add_method, _add_parameters, etc.
    def validate_entities(
        self,
        class_name: str = None, 
        field_name: str = None, 
        method_name: str = None, 
        parameter_name: str = None, 
        class_should_exist: bool = None, 
        field_should_exist: bool = None,
        method_should_exist: bool = None, 
        parameter_should_exist: bool = None
    ) -> bool:
        return self.ProgramManager._validate_entities(
            class_name, field_name, method_name, parameter_name, 
            class_should_exist, field_should_exist, 
            method_should_exist, parameter_should_exist)
    
    ## CLASS RELATED ##
    
    # Add class interface #
    def add_class(self, class_name: str):
        self.ProgramManager._add_class(class_name, is_loading=False)
        
    # Delete class interface #
    def delete_class(self, class_name: str):
        self.ProgramManager._delete_class(class_name)
        
    # Rename class interface #
    def rename_class(self, current_name: str, new_name: str):
        self.ProgramManager._rename_class(current_name, new_name)
        
    ## FIELD RELATED ##
    
    # Add field interface #
    def add_field(self, class_name: str, field_name: str):
        self.ProgramManager._add_field(class_name, field_name, is_loading=False)
        
    # Delete field interface #
    def delete_field(self, class_name: str, field_name: str):
        self.ProgramManager._delete_field(class_name, field_name)
    
    # Rename field interface #
    def rename_field(self, class_name: str, current_field_name: str, new_field_name: str):
        self.ProgramManager._rename_field(class_name, current_field_name, new_field_name)
        
    ## METHOD RELATED ##
    
    # Add method interface #
    def add_method(self, class_name: str, method_name: str):
        self.ProgramManager._add_method(class_name, method_name, is_loading=False)
    
    # Delete method interface #
    def delete_method(self, class_name: str, method_name: str):
        self.ProgramManager._delete_method(class_name, method_name)
        
    # Rename method interface #
    def rename_method(self, class_name: str, current_method_name: str, new_method_name: str):
        self.ProgramManager._rename_method(class_name, current_method_name, new_method_name)
        
    ## PARAMETER RELATED ##
    
    # Add parameter interface #
    def add_parameter(self, class_name: str, method_name: str, parameter_name: str):
        self.ProgramManager._add_parameter(class_name, method_name, parameter_name, is_loading=False)
        
    # Delete parameter interface #
    def delete_parameter(self, class_name: str, method_name: str, parameter_name: str):
        self.ProgramManager._delete_parameter(class_name, method_name, parameter_name)
        
    # Rename parameter interface #
    def rename_parameter(self, class_name: str, method_name: str, current_parameter_name: str, new_parameter_name: str):
        self.ProgramManager._rename_parameter(class_name, method_name, current_parameter_name, new_parameter_name)
        
    # Replace parameter list interface #
    def replace_param_list(self, class_name: str, method_name: str):
        self.ProgramManager._replace_param_list(class_name, method_name)
        
    ## RELATIONSHIP RELATED ##
    
    # Add relationship interface #
    def add_relationship(self, source_class_name: str, destination_class_name: str, type: str):
        self.ProgramManager._add_relationship(source_class_name, destination_class_name, type, is_loading=False)
    
    # Delete relationship interface #
    def delete_relationship(self, source_class_name: str, destination_class_name: str):
        self.ProgramManager._delete_relationship(source_class_name, destination_class_name)
        
    # Change relationship type interface #
    def change_type(self, source_class_name: str, destination_class_name: str, new_type: str):
        self.ProgramManager._change_type(source_class_name, destination_class_name, new_type)
    
    ## DISPLAY RELATED ##
    
    # Display saved file list #
    def display_saved_list(self):
        self.ProgramManager._display_saved_list()
        
    # Display classes #
    def display_classes(self):
        self.ProgramManager._display_wrapper()
        
    # Display single class #
    def display_single_class(self, class_name: str):
        self.ProgramManager._display_single_class_detail(class_name)
        
    # Display relationship #
    def display_relationship(self):
        self.ProgramManager._display_relationship_list()
    
    ## SAVE/LOAD RELATED ##
    
    # Save data #
    def save(self):
        self.ProgramManager._save()
        
    # Load data #
    def load(self):
        self.ProgramManager._load()
    
    # Delete saved file #
    def delete_saved_file(self):
        self.ProgramManager._delete_saved_file()
        
    # Get active file #
    def get_active_file(self) -> str:
        return self.ProgramManager._get_active_file()
    
    # Saved file name check #
    def saved_file_name_check(self, file_name: str) -> bool:
        return self.ProgramManager._saved_file_name_check(file_name)
    
    # Clear current active data #
    def clear_current_active_data(self):
        self.ProgramManager._clear_current_active_data()
    
    # Go back to blank program #
    def end_session(self):
        self.ProgramManager._end_session()
        
    # Sort class list #
    def sort_class_list(self):
        self.ProgramManager._sort_class_list()
        
    # Exit program #
    def exit(self):
        self.ProgramManager._exit()

    #################################################################   
    
    ## USER INTERFACE ##
    
    # Display banner #
    def __display_banner(self):
        banner = r"""
        ▗▖ ▗▖▗▖  ▗▖▗▖       ▗▄▄▄▖▗▄▄▄ ▗▄▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
        ▐▌ ▐▌▐▛▚▞▜▌▐▌       ▐▌   ▐▌  █  █    █ ▐▌ ▐▌▐▌ ▐▌
        ▐▌ ▐▌▐▌  ▐▌▐▌       ▐▛▀▀▘▐▌  █  █    █ ▐▌ ▐▌▐▛▀▚▖
        ▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖    ▐▙▄▄▖▐▙▄▄▀▗▄█▄▖  █ ▝▚▄▞▘▐▌ ▐▌
                                             
        
            Welcome to the UML Management Interface!
    For more information on commands, type "help" for the manual.
        """
        print(banner)
    
    # Promp menu #
    def __prompt_menu(self):
        print("Welcome To Our UML Program!\n")
        # Class
        print("Type 'add_class <class_name>' to add a class")
        print("Type 'delete_class <class_name>' to delete a class")
        print("Type 'rename_class <class_name> <new_name>' to rename a class\n")
        # Field
        print("Type 'add_field <class_name> <attr_name>' to add a field")
        print("Type 'delete_field <class_name> <field_name>' to delete a field from the chosen class")
        print("Type 'rename_field <class_name> <current_field_name> <new_name>' to rename a field\n")
        # Method
        print("Type 'add_method <class_name> <method_name>' to add a method")
        print("Type 'delete_method <class_name> <method_name>' to delete a method from the chosen class")
        print("Type 'rename_method <class_name> <current_method_name> <new_name>' to rename a method\n")
        # Parameter
        print("Type 'add_param <class_name> <method_name> <param_name>' to add a parameter")
        print("Type 'delete_param <class_name> <method_name> <param_name>' to delete a parameter from the chosen class")
        print("Type 'rename_param <class_name> <method_name> <current_param_name> <new_name>' to rename a parameter")
        print("Type 'replace_param <class_name> <method_name>' to replace a method's parameter list\n")
        # Relationship
        print("Type 'add_rel <source_class> <destination_class_name> <relationship_level>' to add relationship and relationship level")
        print("Type 'delete_rel <chosen_class_name> <destination_class_name>' to delete a relationship\n")
        print("Type 'type_mod <source_class_name> <destination_class_name> <type>' to change the type of a relationship\n")
        # Class related commands
        print("Type 'list_class' to see the list of all created class(es)")
        print("Type 'class_detail <class_name>' to see the detail of the chosen class")
        print("Type 'class_rel' to see the relationships between class(es)\n")
        # Save/Load related commands
        print("Type 'saved_list' to see the list of saved files")
        print("Type 'save' to save data")
        print("Type 'load' to load data from saved files")
        print("Type 'delete_saved' to delete saved file")
        print("Type 'clear_data' to delete all the data in the current storage")
        print("Type 'default' to go back to blank program\n")
        # Other tasks
        print("Type 'sort' to sort the class list in alphabetical order")
        print("Type 'help' to see the instructions")
        print("Type 'exit' to quit program")
    
    # Main program #
    def main_program_loop(self):
       # Display a welcome message and help menu
        self.__display_banner()  # Display the banner once
        self.__prompt_menu()  # Show initial instructions
        while True:
            # Collect input from the user
            current_active_file: str = self.get_active_file()
            if current_active_file != "No active file!":
                current_active_file = current_active_file + ".json"
            print(f"\n(Current active file: {current_active_file})")
            print("\n==> ", end="")
            user_input: str = input()  # User provides the input
            user_input_component = user_input.split()  # Split the input by space
            # Parse command and parameters
            if len(user_input_component) == 0:
                continue
            command = user_input_component[0]
            parameters = user_input_component[1:]
            # Pass command and parameters to ProgramManager for processing
            self.ProgramManager._process_command(command, parameters)
            # Show the main menu again #
            if command == InterfaceOptions.HELP.value:
                self.__prompt_menu()
            # Exit command handling in the interface
            elif command == InterfaceOptions.EXIT.value:
                break
        self.exit()
