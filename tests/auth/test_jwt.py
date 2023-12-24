from src.auth.login import JWT
from dotenv import load_dotenv

load_dotenv()
def test_jwt():
    jwt = JWT('HS256')
    token = jwt.jwt_operation('create', username='jaime', authz=True)
    assert token is not None
    decoded = jwt.jwt_operation('decode', token=f"Bearer: {token}")
    assert decoded is not None
    assert decoded['user'] == 'jaime'
    assert decoded['admin'] == True
    assert 'exp' in decoded
    assert 'iat' in decoded
