#!/usr/bin/env bash

httpd=$(ps aux | grep -c httpd)
initd=$(ps aux | grep -c initd)
ssh_agent=$(ps aux | grep -c 'ssh-agent')

if (( httpd )); then
	echo "The Apache web server is running."
fi

if (( initd )); then
	echo "The init daemon is running."
fi

if (( ssh_agent )); then 
	echo "The ssh-agent is running."
fi



