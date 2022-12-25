#!/bin/bash
echo "Launching Docker-compose"

sudo docker compose -f "docker-compose.yml" up -d --build

echo "Done !"
echo ""
echo "Check docker ps to see if containers run"
echo "If there is problems, report logs "