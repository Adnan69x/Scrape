from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am a member scraper bot. Send me /scrape to start scraping members from a group or channel.')

@client.on(events.NewMessage(pattern='/scrape'))
async def scrape(event):
    group_entity = await client.get_entity('YOUR_GROUP_OR_CHANNEL_LINK')
    offset = 0
    limit = 1000  # adjust the limit according to your needs
    all_participants = []
    while True:
        participants = await client(GetParticipantsRequest(
            group_entity,
            ChannelParticipantsSearch(''),
            offset,
            limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)
    members_info = '\n'.join([f"{member.id}, {member.username}, {member.first_name}, {member.last_name}" for member in all_participants])
    await event.respond(f"Scraped members:\n{members_info}")

client.run_until_disconnected()
