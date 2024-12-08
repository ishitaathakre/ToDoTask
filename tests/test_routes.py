import pytest
from app import create_app, db
from app.models import ToDoTable
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        db.session.remove()
        db.drop_all()

def test_add_task(test_client):
    print("Running test_add_task...")
    response = test_client.post('/', json={'task': 'Test Task'})
    print(f"Response: {response}")
    assert response.status_code == 201
    # print(11111111)
    data = response.get_json()
    # print(data)
    assert data['task'] == 'Test Task'

def test_get_tasks(test_client):
    print("Running test_get_tasks...")
    test_client.post('/', json={'task': 'Test Task'})
    response = test_client.get('/')
    print(f"Response: {response}")
    assert response.status_code == 200
    data = response.get_json()
    print(data)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['task'] == 'Test Task'

def test_update_task(test_client):
    print("Running test_update_task...")
    test_client.post('/', json={'task': 'Old Task'})
    response = test_client.put('/1', json={'task': 'Updated Task', 'status': 'Completed'})
    print(f"Response: {response}")
    assert response.status_code == 200
    data = response.get_json()
    assert data['task'] == 'Updated Task'
    assert data['status'] == 'Completed'

def test_delete_task(test_client):
    print("Running test_delete_task...")
    test_client.post('/', json={'task': 'Task to Delete'})
    response = test_client.delete('/1')
    print(f"Response: {response}")
    assert response.status_code == 200
    response = test_client.get('/')
    data = response.get_json()
    assert data == []

def test_delete_all_tasks(test_client):
    print("Running test_delete_all_tasks...")
    test_client.post('/', json={'task': 'Task 1'})
    test_client.post('/', json={'task': 'Task 2'})
    response = test_client.delete('/delete_all')
    print(f"Response: {response}")
    assert response.status_code == 200
    response = test_client.get('/')
    data = response.get_json()
    assert data == []
