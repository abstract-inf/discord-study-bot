# discord-study-bot

## **Description**
to be written in the future

## **Bot Commands**
Below is a list of commands that the bot supports:

### Study Commands
- **`!study` or `!start`**  
  Start a study session. The bot will log the time you started studying and send a confirmation message.

- **`!stop` or `!end`**  
  End your current study session. The bot will calculate the total time you spent studying and send a summary, including a fun GIF based on the duration.
  

### General Commands
- **Greetings**  
  The bot responds to various greetings such as:
  - `hello`, `hi`, `hey`, `greetings`, `good morning`, `good afternoon`, `good evening`, `good night`, `howdy`, `sup`, `what's up`, `yo`, etc.

### Bad Words Handling
The bot detects and responds to inappropriate language with a sarcastic or disapproving message.


## **Installation**

### Prerequisites
Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

*Python 3.10 is prefered, but any 3.x version should work.*

### Clone the Repository
```bash
git clone https://github.com/abstract-inf/discord-study-bot.git
cd discord-study-bot-main  # could be different for you 
```

### Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file and add the required keys:
```env
TOKEN=your-bot-token
```
you can get your keys from the Discord API by creating an application and following the steps https://discord.com/developers/applications 

## **Usage**
you can change the bot texting channel by going to the `main.py` file and changing `channel_logs_name = 'bot channel name'`

To run the bot run the following command:
```bash
python main.py
```

## **Contributing**
This project is still in it's early stages and more features are expected to be added such as:
1. saving logs into `csv` files.
2. being able to call a command `!top` to make a visualization of the members' that studied the most during the week (e.g., using Matplotlib).
3. integratting Large Language Models into this bot (e.g., ChatGPT or DeepSeek).
4. being able to set study hours goals to hit during the day.
5. the ability to check if the user is still studying and has not left his PC while studying hours are still counting.
6. the ability to pause the timer and resume it later during the same day.

Feel free to fork this project and submit pull requests!
