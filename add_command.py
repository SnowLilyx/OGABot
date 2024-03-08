import requests
url = "https://discord.com/api/v10/applications/1215275797775122513/guilds/747563555884367902/commands"
headers = {
    "Authorization": "Bot MTIxNTI3NTc5Nzc3NTEyMjUxMw.GoXsr5.khPlGWUNg_QserCh6bX--xpHoHzmN7mSn_puqU"
}

json = {
    "name": "reportkill",
    "type": 1,
    "description": "Report a kill",
    "options": [
        {
            "name": "killer",
            "description": "Who was the killer?",
            "type": 3,
            "required": True
        },
        {
            "name": "killee",
            "description": "Who was killed?",
            "type": 3,
            "required": True
        },
        {
            "name": "weapon",
            "description": "Which weapon type was used?",
            "type": 3,
            "required": True,
            "choices": [
                {"name": "Melee", "value": "melee"},
                {"name": "Ranged", "value": "ranged"},
                {"name": "Indirect", "value": "indirect"},
                {"name": "Squishimajig", "value": "squishimajig"}
            ]
        },
        {
            "name": "location",
            "description": "Where did the kill happen?",
            "type": 3,
            "required": True
        },
        {
            "name": "time",
            "description": "When did the kill happen?",
            "type": 3,
            "required": True
        }
    ]
}

r = requests.post(url, headers=headers, json=json)
