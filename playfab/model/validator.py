# build-in modules
import re


class Validator:
    
    RULE_REQUIRED   = "required"
    RULE_MIN_LENGTH = "minlength"
    RULE_MAX_LENGTH = "maxlength"
    RULE_EQUAL      = "equal"
    RULE_UNIQUE     = "unique"
    RULE_PASSWORD   = "password"
    RULE_EMAIL      = "email"

    _input = None


    @classmethod
    def input(cls, input):
        cls._input = str(input).strip()
        return cls
    
    @classmethod
    def rules(cls, *rules):
        try:
            for rule in rules:
                if type(rule) is str:
                    eval("cls." + rule + "()")
                elif type(rule) is list:
                    eval("cls." + rule[0] + "('" + str(rule[1]) + "')")
        except Exception as error:
            raise error

    """ RULES CONSTANTS GETTERS (works only with objects)"""

    @property
    def rulerequired(self):
        return self.RULE_REQUIRED
    
    @rulerequired.getter
    def rulerequired(self):
        return self.RULE_REQUIRED

    """ RULES METHODS """
    
    @classmethod
    def required(cls):
        if len(cls._input) == 0:
            raise Exception("Field required.")
        
    @classmethod
    def minlength(cls, argument):
        if len(cls._input) < int(argument):
            raise Exception("Minimum number of characters " + argument + ".")
        
    @classmethod
    def maxlength(cls, argument):
        if len(cls._input) > int(argument):
            raise Exception(argument + " characters exceeded.")
        
    @classmethod
    def equal(cls, argument):
        if argument and not cls._input == argument:
            raise Exception("Inputs are not the same.")

    @classmethod
    def password(cls):
        # /(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9_])/
        if not re.search("(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9_])", cls._input):
            raise Exception("Password does not met requirements.")    
    @classmethod
    def email(cls):
        if not re.search("^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", cls._input):
            raise Exception("Incorrect email address.")