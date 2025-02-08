# Bot Commands and Usage

This document outlines the commands available in the bot, their purposes, and how to use them.

---

## Study Commands

### `!study` or `!start`
- **Purpose**: Starts a study session for the user.
- **Usage**: 
  - Type `!study` or `!start` in the `denshi-bot` channel.
  - The bot will log the start time and notify the channel that you have started studying.
  - Example: `!study`

### `!stop` or `!end`
- **Purpose**: Ends the current study session for the user.
- **Usage**: 
  - Type `!stop` or `!end` in the `denshi-bot` channel.
  - The bot will calculate the time spent studying, log the end time, and send a summary of the study session.
  - Example: `!stop`

---

## Logs Commands

### `!study_logs`
- **Purpose**: Sends the study logs CSV file to the channel.
- **Usage**: 
  - Type `!study_logs` in the `denshi-bot` channel.
  - The bot will send the `study_logs.csv` file, which contains records of all study sessions.
  - Example: `!study_logs`

### `!channel_logs`
- **Purpose**: Sends the voice channel logs CSV file to the channel.
- **Usage**: 
  - Type `!channel_logs` in the `denshi-bot` channel.
  - The bot will send the `channel_logs.csv` file, which contains records of users joining and leaving voice channels.
  - Example: `!channel_logs`

---

## Greeting Commands

### General Greetings
- **Purpose**: Responds to user greetings with a friendly message.
- **Usage**: 
  - Type any common greeting (e.g., `hello`, `hi`, `hey`, `good morning`, etc.) in the `denshi-bot` channel.
  - The bot will respond with a random friendly greeting.
  - Example: `hello`

---

## Terminal Input Mode

### Entering Terminal Input Mode
- **Purpose**: Allows the bot to send messages from the terminal to the Discord channel.
- **Usage**: 
  - Press `Enter` in the terminal where the bot is running to enter terminal input mode.
  - Type the message you want to send to the `denshi-bot` channel.
  - The bot will send the message to the channel.
  - Example: 
    ```
    Press 'Enter' to start or re-enter terminal input mode.
    Enter message to send: Hello from terminal!
    ```

---

## Notes
- All commands must be sent in the assigned channel in the `main.py` file, for example `denshi-bot` channel.
- The bot will ignore messages sent in other channels or empty messages.
- The bot logs study sessions and voice channel activity in CSV files (`study_logs.csv` and `channel_logs.csv`), which can be retrieved using the respective log commands.