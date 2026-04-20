# Connect to an LLM
# - Needs to be a module

# Inject the prompt
#
# Extract the vector embeddings
# We need an object whose interface is a model, data for connecting to the model, prompts, and outputs embeddings


# Object
# Object interface: model, model data, outputs,
class Agent:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


test_agent = Agent("test_agent")

print(test_agent.name)
