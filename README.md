# AI Chatbot Tutorial for Beginners

Welcome to the AI Chatbot Tutorial repository! This project is designed to teach complete beginners how to code with Python by building increasingly complex chatbots. Through this tutorial, you'll learn fundamental Python concepts and how to integrate with OpenAI's GPT models.

## Project Structure

This repository contains four Python scripts, each representing a different stage in building an AI chatbot:

1. `echo_bot.py`: A simple bot that repeats what you say
2. `pretty_echo.py`: An echo bot with improved formatting using the Rich library
3. `chatbot.py`: A basic AI chatbot using OpenAI's GPT-3.5-turbo model
4. `stream_bot.py`: An advanced AI chatbot with streaming responses

## Prerequisites

Before you begin, ensure you have the following:

1. Python installed on your system.

2. Install the required libraries by running:
   ```
   pip install -r requirements.txt
   ```

3. For the AI-powered chatbots (`chatbot.py` and `stream_bot.py`), you'll need an OpenAI API key. Follow these steps to set it up:

   a. Sign up for an OpenAI account and obtain an API key from the OpenAI dashboard.
   
   b. In the root directory of this project, create a file named `.env`.
   
   c. Open the `.env` file and add your OpenAI API key like this:
      ```
      OPENAI_API_KEY=your_api_key_here
      ```
      Replace `your_api_key_here` with your actual OpenAI API key.

   d. Save and close the `.env` file.

Note: The OpenAI library used in this project automatically loads the `OPENAI_API_KEY` from the `.env` file, so you don't need to use any additional library like python-dotenv to manage environment variables.

4. Ensure that `.env` is added to your `.gitignore` file to prevent accidentally sharing your API key on GitHub.

With these prerequisites in place, you're ready to start working with the chatbots in this tutorial.

## Bot Descriptions

### 1. Echo Bot (echo_bot.py)

This is the simplest bot in the tutorial. It repeats whatever the user inputs.

To run:
```
python echo_bot.py
```

### 2. Pretty Echo Bot (pretty_echo.py)

This bot enhances the echo functionality with colored output using the Rich library.

To run:
```
python pretty_echo.py
```

### 3. Basic AI Chatbot (chatbot.py)

This script introduces AI capabilities using OpenAI's GPT-3.5-turbo model. The bot takes on the persona of an ancient golem.

To run:
```
python chatbot.py
```

### 4. Streaming AI Chatbot (stream_bot.py)

This is the most advanced bot in the tutorial. It uses the streaming capability of the OpenAI API to provide a more interactive experience.

To run:
```
python stream_bot.py
```

## Usage

For all bots:
1. Run the script using the commands provided above.
2. Type your message and press Enter.
3. To exit any bot, type `/exit` and press Enter.

## Learning Objectives

Through this tutorial, you'll learn:

- Basic Python syntax and control structures
- Working with external libraries (Rich, OpenAI)
- Handling user input and program output
- Making API calls to AI services
- Implementing streaming responses

## Contributing

This project is part of a tutorial series. If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo model
- The Rich library for beautiful terminal formatting

Happy coding!