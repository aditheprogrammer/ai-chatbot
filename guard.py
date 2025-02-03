import litellm
from guardrails import Guard
from guardrails.hub import ProfanityFree

# Create a Guard class
guard = Guard().use(ProfanityFree())

# Call the Guard to wrap the LLM API call
validated_response = guard(
    litellm.completion,
    model="ollama/mango",
    max_tokens=500,
    api_base="http://localhost:11434",
    messages=[{"role": "user", "content": "stupid"}]
)

print(validated_response.validated_output)