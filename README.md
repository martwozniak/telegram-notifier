# telegram-notifier
This script .py and .sh is for notification system I use in my VPS and dedi servers. 

The main purpose of the creation of this script is to quickly inform me through a message on telegram and a notification on my phone. 

At the moment when any of the sites stops working. For example, instead of code 200 it returns 404, then I get the relevant information on Telegram. 

The script works on many different actions that can happen, for example:
- when any page stops working a notification is sent
- when the CPU usage is at a high level, a notification is sent
- when RAM usage is high, a notification is sent
 - when disk usage is at a high level, a notification is sent

There are many cases in which you can trigger the sending of a notification through Telegram. The best part is that you can also associate other operations for a specific situation. 

## Prerequirements

You have to install:
* **Python3**
* **requirements.txt** installed (*all installed Python modules*)

**Setup you .env file**

## Usage
Using this script is simple. However, it requires early configuration of the appropriate bot on Telegram and obtaining the environment variables used in the .env file. You can use the .env.example file to see what these variables should look like.

**Default error message:**

> `python3 main.py`  

or   
> `./notify.sh`  

  

**Specific error message:**

> `python3 main.py "This is my custom error message"`  

or   
> `./notify.sh "This is my custom error message"`  

## Features

| Task                                     | isDone? |
|------------------------------------------|---------|
| Pass argument to function and script     |    ✅    |
| Prepare triggers for different scenarios |         |
| Add delay to notifications (as argument) |         |
| Other channels communication (eg. mail, slack and more) |         |
| Chart generation, S3 img hosting and telegram message |         |
| PDF Raport generation (cron weekly, monthly, comparison w2w, m2m) |         |


## Emojis


| Second argument                                     | Emoji |
|------------------------------------------|---------|
| -error (error)     |    🔥     |
| -warning (warning) |     ⚠️    |
| -money (money) |     💵    |
| -sparkles (sparkles) |     ✨    |
| -users (users) |     👥    |
| -melting (melting face) |    🫠    |
| -thumb (thumb up) |     👍    |
| -accept (check mark) |     ✅    |
| -star (star) |     ⭐    |
| -thumb (thumb) |     🖙    |