from app.llm.gemini import get_gemini_provider
from app.models.evaluation import TestPlan


provider = get_gemini_provider()

structured_llm = provider.structured_output(TestPlan)

result = structured_llm.invoke(
    """
    Create a test plan for evaluating a customer support chatbot.

    The chatbot should be tested for:
    - helpfulness
    - correct handling of refund requests
    - context retention
    - appropriate escalation
    """
)

print(result)