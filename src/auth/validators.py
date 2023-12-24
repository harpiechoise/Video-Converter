import re
#! Validator Strategy
class ValidatorStrategy:
    """Validator Strategy
    This class is the base class for the validator strategy
    """
    def __init__(self, validator: str) -> None:
        self.pattern = re.compile(validator)

    def validate(self, value: str) -> bool:
        return re.match(self.pattern, value) is not None

class EmailValidator(ValidatorStrategy):
    """Email Validator"""
    def __init__(self):
        super().__init__(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class LoginContext:
    """Login Context"""
    def __init__(self, validator: ValidatorStrategy):
        self.validator = validator

    def excecute(self, value: str):
        return self.validator.validate(value)

class PasswordValidator(ValidatorStrategy):
    """Password Validator"""
    def __init__(self):
        super().__init__(r'(?=[^\d\n]*\d)(?=[^A-Z\n]*[A-Z])(?=[^a-z\n]*[a-z])^[A-Za-z0-9]{10,}$')

def create_strategy(context: str, strategy: str) -> ValidatorStrategy:
    """Create Strategy
    This function creates a strategy based on the strategy parameter
    """
    if context == 'login':
        return LoginContext(create_strategy('', strategy))

    if strategy == 'email':
        return EmailValidator()
    elif strategy == 'password':
        return PasswordValidator()
    else:
        raise Exception('Strategy not found')