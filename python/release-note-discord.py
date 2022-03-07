import json
import os
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

hyperlink_format = '<a href="{link}">{text}</a>'
webhook = DiscordWebhook(url=os.environ["webhook_url"], username="Devtron")
r = requests.get('https://api.github.com/repos/%s/releases/latest'%os.environ["repo"])

output=json.loads(r.text)
release_name= output["name"]
tag_name= output["tag_name"]
tag_url= output["html_url"]
body=output["body"]

embed = DiscordEmbed(
    title="New Release",description="**"+"[%s](%s)"%(tag_name,tag_url)+"**\n\n"+body, color='03b2f8'
)

embed.set_author(
    name="Devtron",
    url="https://devtron.ai/",
    icon_url="https://avatars.githubusercontent.com/u/60952665?s=200&v=4",
)

webhook.add_embed(embed)
response = webhook.execute()
