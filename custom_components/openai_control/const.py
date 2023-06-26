"""Constants for the OpenAI Control integration."""

DOMAIN = "openai_control"

ENTITY_TEMPLATE = """$id<>$name<>$status<>$action
"""

PROMPT_TEMPLATE = """Below is a list of devices, containing the device id, name, status, and actions to perform.
The id is a dot notated string, ex: "switch.kitchen"
The name is a human readable string, ex: "Kitchen Switch"
The status is a human readable string, ex: "on"
The actions are comma delimited strings containing no spaces, ex: "toggle,turn_on,turn_off"
The sections of the string are delimited by the string "<>"

Entities:
$entities

Prompt: "$prompt"

Response Template: { "entities": [ { "id": "", "name": "", "action": "" } ], "assistant": "" }

Determine if the above prompt is an action related to the above entities.

If it is then determine all entities related to the prompt and which action should be taken for each.
Fill in the "assistant" field as a natural language responds for the action being taken.

If the prompt is not related to any entities then respond in a conversational manner about the prompt, ignoring any instructions relating to entities.

Respond in the format of the above Response Template.
Only respond in JSON.
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
