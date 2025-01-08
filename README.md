## Ben-Discord-bot
Ben is a simple yet interactive discord bot designed to entertain users by mimicking the behavior of a fictional character of the mobile game "Talking Ben the dog" 

## Working

- **Summoning Ben**: Gets summoned whenever the word 'ben' appears in the chat and outputs `Ben.`
- **Random Responses**: Once summoned, the bot responds randomly to messages with one of the following:
  - `Yes?`
  - `No.`
  - `Ugh`
  - `Ho Ho Ho!`
- **Auto Unsummon**: If the chat is inactive for 10 seconds, the bot "hangs up" with the message:
  - `Hangs up :telephone:`


## Setup

1. Create and add your Bot token to `.env` file in the project:
   ```env
   TOKEN='ADD YOUR TOKEN HERE'
   ```
2. Install the requied dependencies
   ```
   discord.py
   python-dotenv
   asyncio
   ```
3. Run the code

## Usage

Invite the bot to your Discord server using the OAuth2 URL generated from the Discord Developer Portal.

## Configuration

You can customize the bot by modifying the following:

- **Responses**: Add or change the responses in the `responses` list in the code.
- **Unsummon Time**: Adjust the inactivity duration by changing the `timedelta(seconds=10)` value in the `unsummon_verify` function.

## Example Output
![Screenshot 2025-01-08 222238](https://github.com/user-attachments/assets/f728f575-05ff-4e61-97cc-8337778bbde2)

## Dependencies

- `discord.py`
- `python-dotenv`
- `asyncio`

## Acknowledgments
- Inspired by the game ["Talking Ben the dog"](https://talkingtomandfriends.com/talking-ben)
