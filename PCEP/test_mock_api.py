import requests
import responses

# Base URL for the mock API
BASE_URL = "https://api.example.com"

# Function to fetch user data
def fetch_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return response.json(), response.status_code

# Function to create a new user
def create_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    return response.json(), response.status_code

@responses.activate
def test_fetch_user_success():
    # Mock the GET /users/{user_id} endpoint
    responses.add(
        responses.GET,
        f"{BASE_URL}/users/1",
        json={"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
        status=200
    )

    # Call the function and assert the result
    user, status_code = fetch_user(1)
    assert status_code == 200
    assert user == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

@responses.activate
def test_create_user_success():
    # Mock the POST /users endpoint
    responses.add(
        responses.POST,
        f"{BASE_URL}/users",
        json={"id": 2, "message": "User created successfully"},
        status=201
    )

    # Call the function and assert the result
    user_data = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    response, status_code = create_user(user_data)
    assert status_code == 201
    assert response == {"id": 2, "message": "User created successfully"}

@responses.activate
def test_fetch_user_not_found():
    # Mock a 404 error for GET /users/{user_id}
    responses.add(
        responses.GET,
        f"{BASE_URL}/users/99",
        json={"error": "User not found"},
        status=404
    )

    # Call the function and assert the result
    user, status_code = fetch_user(99)
    assert status_code == 404
    assert user == {"error": "User not found"}

if __name__ == "__main__":
    # Run the tests manually (useful for educational purposes)
    test_fetch_user_success()
    print("Fetch user success test passed.")

    test_create_user_success()
    print("Create user success test passed.")

    test_fetch_user_not_found()
    print("Fetch user not found test passed.")
