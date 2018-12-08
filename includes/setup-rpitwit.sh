#!/bin/bash

echo "Setup rpitwit..."
cd rpitwit
./rpitwit --setup -d ../rpitwit_commands/ -f /usr/share/BlackBulb/conf/rpitwit_config

echo ""
echo "Setup twittert..."
twitter --oauth /usr/share/BlackBulb/conf/rpitwit_twitter_oauth

