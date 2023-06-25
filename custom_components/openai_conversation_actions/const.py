"""Constants for the OpenAI Conversation integration."""

DOMAIN = "openai_conversation_actions"

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
DEFAULT_PROMPT = """This smart home is controlled by Home Assistant.

An overview of the areas and the devices in this smart home:
{%- for area in areas() %}
  {%- set area_info = namespace(printed=false) %}
  {%- for device in area_devices(area) -%}
    {%- if not device_attr(device, "disabled_by") and not device_attr(device, "entry_type") and device_attr(device, "name") %}
      {%- if not area_info.printed %}

{{ area_name(area) }}:
        {%- set area_info.printed = true %}
      {%- endif %}
- {{ device_attr(device, "name") }}{% if device_attr(device, "model") and (device_attr(device, "model") | string) not in (device_attr(device, "name") | string) %} ({{ device_attr(device, "model") }}){% endif %}
    {%- endif %}
  {%- endfor %}
{%- endfor %}

Answer the user's questions about the world truthfully.

If the user wants to control a device, reject the request and suggest using the Home Assistant app.
"""

CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo"

CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 150

CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1

CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
