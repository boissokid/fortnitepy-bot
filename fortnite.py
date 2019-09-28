import fortnitepy
import json
import aiohttp
import time

with open('config.json', 'r') as f:
    data = json.load(f)
    emailjson = data[0]['email']
    passwordjson = data[0]['password']
    netcljson = data[0]['netcl']
    cid = data[0]['cid']
    bid = data[0]['bid']
    eid = data[0]['eid']
    banner = data[0]['banner']
    banner_colour = data[0]['banner_colour']
    level = data[0]['level']
    friendaccept = data[0]['friendaccept']

client = fortnitepy.Client(
    email=emailjson,
    password=passwordjson,
    net_cl=netcljson,
)

BEN_BOT_BASE = 'http://benbotfn.tk:8080/api/cosmetics/search/multiple'

print('fortnitepy-bot made by xMistt. credit to Terbau for creating the library.'.format(client))

@client.event
async def event_ready():
    print('Client ready as {0.user.display_name}'.format(client))

@client.event
async def event_party_invite(invitation):
    await invitation.accept()
    # if you want the bot to join with stuff on, put in here.
    # await invite(user_id) (Invite other bots/people to your lobby when the main bot joins.)

@client.event
async def event_friend_request(request):
    if friendaccept == "true":
        await request.accept()
    else:
        await request.decline()

@client.event
async def event_party_member_join(member):
    await client.user.party.me.set_outfit(asset=cid)
    await client.user.party.me.set_backpack(asset=bid)
    await client.user.party.me.set_banner(icon=banner, color=banner_colour, season_level=level)
    time.sleep(2)
    await client.user.party.me.set_emote(asset=eid)
    #await client.user.party.me.set_battlepass_info(self_boost_xp=999999, friend_boost_xp=999999):

async def fetch_cosmetic_id(display_name):
    idint = 0
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(BEN_BOT_BASE, params={'displayName': display_name}) as r:
                data = await r.json()
                type = data[idint]["type"]
                if type == "Outfit":
                            id = data[idint]["id"]
                            return id
                else:
                    idint += 1

@client.event
async def event_friend_message(message):
    args = message.content.split()
    split = args[1:]
    joinedArguments = " ".join(split)
    print('Received message from {0.author.display_name} | Content: "{0.content}"'.format(message))

    if "!skin" in args[0]:
        id = await fetch_cosmetic_id(' '.join(split))
        await client.user.party.me.set_outfit(
            asset=id
        )

    if "!purpleskull" in args[0]:
        variants = client.user.party.me.create_variants(
           clothing_color=1
        )

        await client.user.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=variants
        )

        await message.reply('Skin set to Purple Skull Trooper!')

    if "!banner" in args[0]:
        await client.user.party.me.set_banner(icon=args[1], color=args[2], season_level=args[3])

    if "CID_" in args[0]:
        await client.user.party.me.set_outfit(
            asset=args[0]
        )

        await message.reply('Skin set to ' + args[0])

    if "!variants" in args[0]:
        args3 = int(args[3])
        variants = client.user.party.me.create_variants(**{args[2]: args3})

        await client.user.party.me.set_outfit(
            asset=args[1],
            variants=variants
        )

        await message.reply('Skin set to checkered Renegade Raider!')

    if "!checkeredrenegade" in args[0]:

        variants = client.user.party.me.create_variants(
           material=2
        )

        await client.user.party.me.set_outfit(
            asset='CID_028_Athena_Commando_F',
            variants=variants
        )

        await message.reply('Skin set to ' + args[0] + '!')

    if "EID_" in args[0]:
        await client.user.party.me.set_emote(
            asset=args[0]
        )
        await message.reply('Emote set to ' + args[0] + '!')
        
    if "!stop" in args[0]:
        await client.user.party.me.set_emote(
            asset="StopEmote"
        )
        await message.reply('Stopped emoting.')

    if "BID_" in args[0]:
        await client.user.party.me.set_backpack(
            asset=args[0]
        )

        await message.reply('Backbling set to ' + message.content + '!')

    if "!help" in args[0]:
        await message.reply('My commands are; !purpleskull, !renegaderaider, !variants, CID_, EID_, BID_, PICKAXE_ID_ !banner, !stop & !help')

    if "PICKAXE_ID_" in args[0]:
        await client.user.party.me.set_pickaxe(
                asset=args[0]
        )

        await message.reply('Pickaxe set to ' + args[0] + '!')

    if "!legacypickaxe" in args[0]:
        await client.user.party.me.set_pickaxe(
                asset=args[1]
        )

        await message.reply('Pickaxe set to ' + args[1] + '!')

@client.event
async def event_party_message(message):
    # only type these if you're alone in your lobby + you're on console.
    args = message.content.split()
    split = args[1:]
    print('Received message from {0.author.display_name} | Content: "{0.content}"'.format(message))

    if "!skin" in args[0]:
        id = await fetch_cosmetic_id(' '.join(split))
        await client.user.party.me.set_outfit(
            asset=id
        )

    if "!purpleskull" in args[0]:
        variants = client.user.party.me.create_variants(
           clothing_color=1
        )

        await client.user.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=variants
        )

        await message.reply('Skin set to Purple Skull Trooper!')

    if "!banner" in args[0]:
        await client.user.party.me.set_banner(icon=args[1], color=args[2], season_level=None)

    if "CID_" in args[0]:
        await client.user.party.me.set_outfit(
            asset=args[0]
        )

    if "!variants" in args[0]:
        args3 = int(args[3])
        variants = client.user.party.me.create_variants(**{args[2]: args3})

        await client.user.party.me.set_outfit(
            asset=args[1],
            variants=variants
        )

        await message.reply('Skin set to' + args[1])

    if "!renegaderaider" in args[0]:

        variants = client.user.party.me.create_variants(
           material=2
        )

        await client.user.party.me.set_outfit(
            asset='CID_028_Athena_Commando_F',
            variants=variants
        )

        await message.reply('Skin set to' + args[0] + '!')

    if "EID_" in args[0]:
        await client.user.party.me.set_emote(
            asset=args[0]
        )
        await message.reply('Emote set to' + args[0] + '!')
        
    if "!stop" in args[0]:
        await client.user.party.me.set_emote(
            asset="StopEmote"
        )
        await message.reply('Stopped emoting.')

    if "BID_" in args[0]:
        await client.user.party.me.set_backpack(
            asset=args[0]
        )

        await message.reply('Backbling set to' + message.content + '!')

    if "!help" in args[0]:
        await message.reply('My commands are; !purpleskull, !renegaderaider, !variants, CID_, EID_, BID_, PICKAXE_ID_ !banner, !stop & !help')

    if "PICKAXE_ID_" in args[0]:
        await client.user.party.me.set_pickaxe(
                asset=args[0]
        )

        await message.reply('Pickaxe set to' + args[0] + '!')

    if "!legacypickaxe" in args[0]:
        await client.user.party.me.set_pickaxe(
                asset=args[1]
        )

        await message.reply('Pickaxe set to' + args[1] + '!')

client.run()