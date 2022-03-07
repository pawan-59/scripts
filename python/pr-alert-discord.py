import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import re

webhook = DiscordWebhook(url="url", username="Devtron")
r = requests.get('https://api.github.com/repos/devtron-labs/devtron/releases/latest')
embed = DiscordEmbed(
    title="New Release",description=r.json()['tag_name'], color='03b2f8'
)
embed.set_author(
    name="Devtron",
    url="https://devtron.ai/",
    icon_url="https://avatars.githubusercontent.com/u/60952665?s=200&v=4",
)
notes=r.json()['body'].splitlines()
for note in notes:
    regex = re.compile(".*?\((.*?)\)")
    url = re.findall(regex, note)
    regex = re.compile(".*?\](.*?)\[")
    title = re.findall(regex, note)
    regex = re.compile(".*?\[(.*?)\]")
    result = re.findall(regex, note)
    feat=""
    for i in range(len(result)-1):
        feat+="[%s] "%result[i]
    embed.add_embed_field(name=feat+"\n"+title[-1], value=url[-1], inline=False)
webhook.add_embed(embed)
response = webhook.execute()
