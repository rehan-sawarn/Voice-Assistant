# Voice Assistant

## Overview

The Voice Assistant is a multifunctional tool that responds to voice commands to perform various tasks. It can:

- **Search Wikipedia** for specific topics.
- **Tell Jokes and Random Facts** for entertainment.
- **Play Videos and Songs** on YouTube.
- **Provide News Updates** with the latest headlines.

## Features

- **Wikipedia Search:** Opens Wikipedia and retrieves information about a specified topic.
- **Joke Telling:** Delivers jokes to entertain and lighten the mood.
- **YouTube Playback:** Plays videos and songs on YouTube based on voice commands.
- **News Updates:** Provides current news headlines.
- **Random Facts:** Tells Random facts using the randfact library.

## Prerequisites

Before using the Voice Assistant, ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries 

## Installation

1. **Clone the Repository**
    ```bash
   git clone https://github.com/rehan-sawarn/Voice-Assistant
   cd voice-assistant
    ```
2. **Install Dependencies**

   Make sure you have `pip` installed. Run the following command to install the required Python libraries:

   ```python
    pip install selenium
    pip install requests
    pip install pyttsx3
    pip install SpeechRecognition
    pip install randfacts
    ```

## Configuration

### News API

To use the news functionality, you'll need an API key from [NewsAPI](https://newsapi.org/). Follow these steps:

1. **Obtain Your API Key**

   - Go to [NewsAPI](https://newsapi.org/) and sign up for an account.
   - After signing up, navigate to your dashboard to get your API key.

2. **Update Configuration**

   - Locate the `news.py` file in the project directory.
   - Find the line where `key` is defined and update it with your API key:

     ```bash
     key = "YOUR_API_KEY"
     ```

### Other Configurations

- Review `config.example.json` for other configuration settings.
- Rename `config.example.json` to `config.json` and update any necessary values specific to your setup.

## Usage

1. **Start the Voice Assistant**

   Run the script using Python:

   ```bash
   python voice_assistant.py
   ```

2. **Voice Commands**

   The Voice Assistant responds to the following commands:

   - **Search Wikipedia:** "Search for [topic] on Wikipedia"
   - **Tell a Joke:** "Tell me a joke"
   - **Play YouTube Video/Song:** "Play [title] on YouTube"
   - **News Updates:** "What’s the news today?"
   - **Tell a Random Fact:** "Tell me a random fact"


## Contact

For any questions or support, please contact rehansawarn@gmail.com.
