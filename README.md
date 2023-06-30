<p align="center">
    <img src="https://raw.githubusercontent.com/alanjames1987/OpenAI-Control-HA/master/.attachments/icon-light-mode.png#gh-light-mode-only">
    <img src="https://raw.githubusercontent.com/alanjames1987/OpenAI-Control-HA/master/.attachments/icon-dark-mode.png#gh-dark-mode-only">
</p>

<h1 align="center">

[OpenAI Control Custom Integration](https://github.com/alanjames1987/OpenAI-Control-HA) for Home Assistant

</h1>

| :warning: This integration is a work in progress and only controls lights. |
| --- |

# About

This custom integratration uses OpenAI to parse intents from Home Assistant Conversation Assist and call Home Assistant services.

In short, HA Assist can now control your house with natual language and more complex commmands.

This integration, along with the [appropriate hardware](https://shop.m5stack.com/products/atom-echo-smart-speaker-dev-kit) can replace Alexa, Google Assisant, Siri, and other digital assistants.

Currently, this integration only supports OpenAI but can be used as a base to integrate with other LLMs, like a locally deployed instance of [Open Assistant](https://open-assistant.io/).

# Installation

## HACS

1. It's recommended to install this custom component using [HACS](https://hacs.xyz/).

1. To install HACS please see their installation instructions.

**The following information may change in future versions of HACS so it's always best to refer to the official HACS documentation [here](https://hacs.xyz/docs/faq/custom_repositories/).**

1. Once HACS is installed navigate to the HACS interface and click on "Integrations".

1. From "Integrations" click on the three dots in the top right corner and click "Custom reponsitories".

1. Paste in the GitHub link to this repository, [https://github.com/alanjames1987/OpenAI-Control-HA](https://github.com/alanjames1987/OpenAI-Control-HA) and select "Integration" as the category.

1. Click add and the integration will be added to HACS.

1. You should now see the integration in your HACS integations list. Click on it and click "Download" in the bottom corner. Select a version and click "Download".

1. This may take some time but once it's complete restart Home Assistant.

## Configure

1. Once Home Assistant restarts navigate to the Home Assistant Devices & Services page by clicking the gear icon in the bottom left of your Home Assistant interface and then clicking "Devices & Services".

<div align="center">

![](https://raw.githubusercontent.com/alanjames1987/OpenAI-Control-HA/master/.attachments/install_key.png "API Key")

</div>

1. Once there click the "Add Integration" button in the bottom right corner and search for "OpenAI Control".

<div align="center">

![](https://raw.githubusercontent.com/alanjames1987/OpenAI-Control-HA/master/.attachments/install_select.png "Integraions")

</div>

1. Click it and the integration will install and start the configuration process.

1. Once installed click on a modal will ask you for your OpenAI API key. To get one visit the [OpenAI API Key portal](https://platform.openai.com/account/api-keys) and create a new one. Note, you will need billing configured on your account to create a key.

1. Once you enter the OpenAI API key the integration is installed and can be used.

## How it Works

OpenAI-Control-HA behaves as a standard [Conversation Agent](https://developers.home-assistant.io/docs/core/conversation/custom_agent/) within the Home Assistant [https://www.home-assistant.io/voice_control/voice_remote_local_assistant/]("Assist Pipeline"). It behaves as a intent parser, which is part of the pipeline that takes in a sentence and performs various actions to generate various responses. OpenAI-Control-HA performs the following actions during its intent parsing process.

1. Receives in the sentence sent by the Assist Pipeline.

1. Retrieves the id, name, state, and services of all entities that are exposed to the Conversation pipeline.

1. Adds the entities and sentence to a logic prompt to be sent to OpenAI models (GPT-3.5-Turbo by default).
    1. The logic prompt asks the OpenAI model to determine if the user's sentence is a command requesting a state change to an entity.
    1. If the sentence is a command then OpenAI is asked to return a JSON of all entities relating to the command and a service to call on those entities.
    1. If the sentence is not a command then OpenAI is asked to ignore anything relating to the smart home and reply normally.
    1. OpenAI is asked to return a conversational response, which will be returned to the user.

1. Once OpenAI returns a JSON response OpenAI-Control-HA parses the returned JSON JSON and calls the service listed for each entitiy OpenAI has identifed relates to the sentence.

1. Finally the conversational response is passed through to the next step of the Assist Pipeline, to be displayed to the user.

## Examples

OpenAI-Control-HA can perform simple tasks but can also understand more obsure requests.

The phrase "Turn on the office switch" did as expected and turned on the office switch.

<div align="center">

![](https://raw.githubusercontent.com/alanjames1987/OpenAI-Control-HA/master/.attachments/example_office.png "Turn on the office switch")

</div>

The phrase "Can you get ready for a guest to arrive?" turned on the driveway light, the front door light, the guest room light, and set a special mode in my house called "Guest Mode" to on. This mode disables some automations that some guests might find confusing, like bathroom lights automatically turning off or lights dimming for bedtime.

<div align="center">

![](https://raw.githubusercontent.com/alanjames1987/OpenAI-Control-HA/master/.attachments/example_guest.png "Can you get ready for a guest to arrive?")

</div>

Based only on their name OpenAI reasoned that these switches related to a guest arriving and turned on the switches.

This type of natual language fuzzy intent parsing can currently only be achived using LLMs.