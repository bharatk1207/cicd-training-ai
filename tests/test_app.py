import pytest
from app import app
import socket

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world_route(client):
    """Test the / route"""
    response = client.get('/')
    assert response.status_code == 200
    
    # Get the expected hostname and IP
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    expected_response = f"Hello World from {hostname} (IP: {ip_address})"
    
    # Convert bytes to string and compare
    assert response.data.decode('utf-8') == expected_response

def test_hello_mark_route(client):
    """Test the /hello route"""
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello Mark!"

def test_goodbye_route(client):
    """Test the /goodbye route"""
    response = client.get('/goodbye')
    assert response.status_code == 200
    
    # Get the expected hostname and IP
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    expected_response = f"Goodbye (IP: {ip_address})"
    
    # Convert bytes to string and compare
    assert response.data.decode('utf-8') == expected_response

def test_greet_route(client):
    """Test the /greet/<name> route"""
    test_name = "Larry"
    response = client.get(f'/greet/{test_name}')
    assert response.status_code == 200
    
    # Get the expected hostname and IP
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    expected_response = f"Hello, {test_name} (IP: {ip_address})"
    
    # Convert bytes to string and compare
    assert response.data.decode('utf-8') == expected_response

def test_non_existing_route(client):
    """Test a non-existing route returns 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
