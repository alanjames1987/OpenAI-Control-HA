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

## Configur

1. Once Home Assistant restarts navigate to the Home Assistant Devices & Services page by clicking the gear icon in the bottom left of your Home Assistant interface and then clicking "Devices & Services".

1. Once there click the "Add Integration" button in the bottom right corner and search for "OpenAI Control".

1. Click it and the integration will install and start the configuration process.

1. TDB
