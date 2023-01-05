#!/bin/bash
docker run -p 32168:32168 --name CodeProject.AI-Server -d -v /usr/share/CodeProject/AI:/usr/share/CodeProject/AI codeproject/ai-server

