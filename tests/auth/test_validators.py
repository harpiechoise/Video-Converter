from src.auth.validators import LoginContext, EmailValidator, PasswordValidator, create_strategy
from dotenv import load_dotenv

load_dotenv()
def test_email_validator():
    email_validator = EmailValidator()
    login_context = LoginContext(email_validator)
    assert login_context.excecute('jaime') == False
    assert login_context.excecute('jaime@') == False
    assert login_context.excecute('jaime@gmail') == False
    assert login_context.excecute('jaime@gmail.com') == True

def test_password_validator():
    password_validator = PasswordValidator()
    login_context = LoginContext(password_validator)
    assert login_context.excecute('jaime') == False
    assert login_context.excecute('jaime123') == False
    assert login_context.excecute('jaime123A') == False
    assert login_context.excecute('Prueba123123123!!') == False
    assert login_context.excecute('Prueba123123123') == True

def test_create_strategy():
    login_context = create_strategy('login', 'email')
    assert isinstance(login_context, LoginContext)
    assert isinstance(login_context.validator, EmailValidator)
    login_context = create_strategy('login', 'password')
    assert isinstance(login_context, LoginContext)
    assert isinstance(login_context.validator, PasswordValidator)
