
def mock_chatbot_response(user_message: str) -> str:
    """Return a deterministic response from the mock chatbot."""

    message = user_message.lower()

    if "refund" in message or "return" in message:
        return (
            "I'd be happy to help with your return. "
            "Please provide your order number so I can check "
            "the refund eligibility and explain the next steps."
        )

    if "order" in message:
        return (
            "I can help you with your order. "
            "Please let me know what you'd like to resolve."
        )

    return (
        "Thank you for contacting customer support. "
        "Could you provide a few more details so I can assist you?"
    )