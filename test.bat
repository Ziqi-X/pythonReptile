@echo off
echo prefab img_data.json prefab | python PathJson.py
move img_data.json ./prefab/img_data.json
pause