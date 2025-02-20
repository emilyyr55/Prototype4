class UMLField:
    # UML class attribute constructor
    # Create an attribute to add to the UML Class
    def __init__(self,type: str = "", field_name: str = ""):
        self.__type = type
        self.__field_name = field_name

    def __str__(self):
            return f"{self.__type} {self.__field_name}"
        
    #################################################################
    # Method to get attribute's data members #
    def _get_name(self) -> str:
        return self.__field_name
    
    def _get_type(self) -> str:
        return self.__type

    #################################################################
    # Method to modify attribute's data members #
    def _set_name(self, new_name: str):
        self.__field_name = new_name
        
    def _set_type(self, new_name: str):
        self.__type = new_name

    #################################################################
    # Method to convert attribute to json format
    def _convert_to_json_field(self) -> dict[str, str]:
        return {"name": self.__field_name,
                "type": self.__type}