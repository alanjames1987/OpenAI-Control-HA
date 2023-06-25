<p align="center">
    <img src="https://raw.githubusercontent.com/alanjames1987/OpenAI-Conversation-Actions-HA/main/.attachments/light_icon.png#gh-light-mode-only">
    <img src="https://raw.githubusercontent.com/alanjames1987/OpenAI-Conversation-Actions-HA/main/.attachments/dark_icon.png#gh-dark-mode-only">
</p>

<h1 align="center">

[OpenAI Conversation Actions Custom Integration](https://github.com/alanjames1987/OpenAI-Conversation-Actions-HA) for Home Assistant

</h1>

# About

This is a custom integration to use OpenAI to parse Home Assistant conversations and execute Home Assistant actions.

This integration along with the appropriate hardware can replace Alexa, Google Assisant, Siri, and other digital assistants.

This integration only supports OpenAI but can be forked and altered to integrat with other LLMs, like a locally deployed instance of Open Assistant.

# Installation

## HACS

1. It's recommended to install this custom component using [HACS](https://hacs.xyz/).

1. To install HACS please see their installation instructions.

**The following information may change in future versions of HACS so it's always best to refer to the official HACS documentation [here](https://hacs.xyz/docs/faq/custom_repositories/).**

1. Once HACS is installed navigate to the HACS interface and click on "Integrations".

1. From "Integrations" click on the three dots in the top right corner and click "Custom reponsitories".

1. Paste in the GitHub link to this repository, [https://github.com/alanjames1987/https://github.com/alanjames1987/OpenAI-Conversation-Actions-HA](https://github.com/alanjames1987/https://github.com/alanjames1987/OpenAI-Conversation-Actions-HA) and select "Integration" as the category.

1. Click add and the integration will be added to HACS.

1. You should now see the integration in your HACS integations list. Click on it and click "Download" in the bottom corner. Select a version and click "Download".

1. This may take some time but once it's complete restart Home Assistant.

## Home Assistant Devices & Services

1. Once Home Assistant restarts navigate to the Home Assistant Devices & Services page by clicking the gear icon in the bottom left of your Home Assistant interface and then clicking "Devices & Services".

1. Once there click the "Add Integration" button in the bottom right corner and search for "OpenAI Conversation Actions".

1. Click it and the integration will install and start the configuration process.

1. TDB
