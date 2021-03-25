# CNA335_Final_Project
## Set Up Telegram Bot on Raspberry Pi

![image](https://user-images.githubusercontent.com/63702251/112428862-0f843500-8cf9-11eb-8966-c730fc7e5e5e.png)

...
On 24 June, 2015, Telegram published the Bot API, enabling machines to talk Telegram. From that day on, not only can human use Telegram, so can machines.

For those who don't know what Telegram is, it is a messaging app, very much like WhatsApp. This tutorial is going to teach how to send a Telegram message to your Raspberry Pi, and how to make your Pi telegram back.

Make sure the Pi has internet access, and I assume you know how to enter the Pifrom a PC, either via SSH or a USB-TTL serial cable.

### Step 1: Install Telegram on Your Phone, Obviously
...
Go to App Store (iPhone) or Play Store (Android), download and install Telegram on your phone.

Now, you can use Telegram. Not yet for the Raspberry Pi. Telegram reserves a special kind of accounts for machines, called bot accounts. As the owner of your own Pi, you have to obtain a bot account for it.

### Step 2: Text /newbot to BotFather
...
Open Telegram on your phone, search for a user called BotFather. As the name implies, he is the Father of All Bots.

As you may have guessed, he is not of our own species, but is actually a machine. He accepts special commands, because he does not understand plain English very well.

To obtain a bot account, text him /newbot. (you need the slash '/' in front) He will then ask a couple of questions. In the screenshot above, I call my bot "Dicey Clock". You will see why in a few moments. But you can give it any name you want.

At the end of process, you will be given a token, something like 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ. This token represents the bot account. You are going to put this token on the Pi.

Here, we have a problem. How are you going to copy this lonnnnnnng token from the phone to the Pi? By hand?

### Step 3: Use Telegram's Web Version
...
Aside from being a smartphone app, Telegram may also be used on a web browser.

On your PC, open a browser, go to Telegram's Web Version. It will ask for your phone number, then send you an SMS message containing a code. Enter the code, and you will be led to an interface very similar to your Telegram app.

Find the conversations with BotFather. You should see the token right there. Now, you can easily copy-&-paste the token from the browser window to the Pi, whenever you want, as often as you want.

### Step 4: Install Telepot on Raspberry Pi
...
Enter the Pi, via SSH or a USB-TTL serial cable. Install telepot, a Python package that enables the Pi to speak Telegram Bot API.

On the command line, run these two commands:

sudo apt-get install python-pip
sudo pip3 install telepot

### Step 5: Test Token
...
On the command line, type python to enter the Python interpreter.

In the Python interpreter, enter these three lines, as in the screenshot above:

import telepot
bot = telepot.Bot('copy bot token from browser ')
bot.getMe()

I have blurred out my bot's token and id. You should keep yours secret too. Having the token means having access to the bot account.

If the last command, getMe(), returns a dictionary describing the bot account (as in the screenshot), all is good. Type exit() to leave the Python interpreter.

If not, you have copied the wrong token. Type exit() to leave the Python interpreter. Then type python to come in again, and repeat those three lines of code.

### Step 6: Create Python script
...
Download from this repository
Are you still wondering why I call my bot Dicey Clock? It is because I want it to behave like this:

when you text it /roll, it will reply with a random integer between 1 and 6, like rolling a dice.
when you text it /time, it will reply with the current time, like a clock.
Such a bot is not very useful, but it serves as a first example of what a bot can do. Once you gain more Python experience, possibilities are limitless.

Save the code in the above screenshot into a file on the Raspberry Pi. If you don't want to write it by hand, you may copy it from here. Remember to insert your bot's token into the code.

Preceding a command with a '/' is Telegram's convention. You don't have to follow it, but following it has benefits, as we will soon see.

### Step 7: Run It and Text It
...
Assuming you have named the file you have just saved "Saeid Nahali.py", type python Saeid Nahali.py to run the bot.

Open Telegram on your phone, search for your bot using its name or username. Text it /roll or /time or /logo, and see how it responds. It is quite fun to have a Raspberry Pi answering your text, isn't it?

This is only a beginning. You can basically use Telegram to tell the Pi to do whatever you want. This is, by far, the easiest way for you to keep in touch with your Pi, from anywhere in the world.

I could have stopped here, but I want to tell you one more thing, that Telegram has a way to save typing. You don't have to actually type the commands every time.

### Step 8: BotFather Can Save You Typing
...
Text BotFather /setcommands. He will ask you to provide a command list for one of your bots. Look at the left screenshot above to see how I did it. Pay attention that the first letter of each line of the command list has to be lowercase.

After that, exit Telegram. Force-stop it if you want. Open it again, and go to your bot's page (not BotFather's, but your own bot's). Type a slash (/), and you should see something like the right screenshot above - Telegram will list out the commands for you. You only have to tap on it.

I hope this tutorial helps you set up a Telegram Bot on Raspberry Pi for the first time. As I said, this is only a beginning. For as long as you can communicate with your Pi, you can tell it to do whatever you want, or you can tell it to tell you whatever it wants.
