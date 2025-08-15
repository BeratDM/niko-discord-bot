#!/bin/bash

cd ~/bxProjects/niko-discord-bot || exit

# Pull latest changes
git pull origin main

# Activate venv and install dependencies
source .venv/bin/activate
pip install -r requirements.txt

# Restart the bot
sudo systemctl restart niko-bot
