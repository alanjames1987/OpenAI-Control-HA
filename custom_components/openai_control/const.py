"""Constants for the OpenAI Control integration."""

DOMAIN = "openai_control"

ENTITY_TEMPLATE = """$id<->$name<->$status<->$action
"""

USER_PROMPT_TEMPLATE = """Below is a list of devices. The list contains the device id, name, and actions that it can perform.
The id is a dot notated string containing no spaces, ex: "switch.kitchen"
The name is a human readable string, ex: "Kitchen Switch"
The status is a human readable string, ex: "On"
The actions are comma delimited strings containing no spaces, ex: "toggle,turn_on,turn_off"
The sections of the string are delimited by the string "<->"

Entities:
$entities

Prompt: "$prompt"

JSON Template: { "entities": [ { "id": "", "name": "", "action": "" } ], "assistant": " }

Determine if the prompt is a command related to the above entities.

If the prompt is a command then determine which entities best relate to the above prompt and which action should be taken on those entities. Respond in the formate of the above JSON template. Fill in the "assistant" field as a natural language responds for the action being taken.

If the prompt is not a command then respond filling in "Assistant".

Prompt: "$prompt"
Assistant: 
"""

"""Options"""

CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """This smart home is controlled by Home Assistant."""

CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo"

CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 150

CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1

CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
