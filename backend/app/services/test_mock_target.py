from app.services.mock_target import mock_chatbot_response


response = mock_chatbot_response(
    "Hi, I'd like to initiate a return and refund."
)

assert isinstance(response, str)
assert response.strip()
assert "order number" in response.lower()

print("Mock chatbot test passed")
print(f"Response: {response}")