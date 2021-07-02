import discord
import random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
client = commands.Bot(command_prefix = '.')
bot = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

#commands
@client.command(aliases=["8ball"], name = "8 ball", description = "You ask it a question, and it responds like a magic 8 ball.")
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
"Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
"Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
"Yes.", "Yes – definitely.", "You may rely on it."]
    await ctx.send (f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(name = "give me mod", description = "haha meme funny")
async def givememod(ctx):
    await ctx.send('''You: give me mod, give me mod, give me mod, give me mod, give me mod, give me mod, give me mod, give me mod, give me mod, give me mod, give me mod
Me: no u.''')

@client.command(name = "getrole", description = "adds a role (by god please DO NOT GIVE YOURSELF MOD OR ADMIN!!!! YOU WILL BE KICKED!!!!!)")
async def getrole(ctx, member : discord.Member, *, role : discord.Role):
    await member.add_roles(role)
    await member.send(f"You have been given the role '{role}'")

@client.command(name = "clear", description = "Clears a specified amount of messages. The default value is 10 messages.")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=all):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['ping'], name = "pings", description = "pings @everyone")
async def ping_everyone(ctx):
    await ctx.send("@everyone")

@client.command(name = "ping_here", description = "pings @here")
async def ping_here(ctx):
    await ctx.send("@here")

@client.command(name = "ban", description = "bans someone from the guild")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, *, reason="being a jerk and breaking the rules"):
    await user.ban(reason=reason)
    await ctx.send(f'Banned {user.mention} for {reason}')
    await user.send(f"You have been banned from the server for {reason}")

@client.command(name = "kick", description = "kicks someone from the guild")
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User, *, reason="being a jerk and breaking the rules"):
    await user.kick(reason=reason)
    await ctx.send (f'Kicked {user.mention}')
    await user.send(f"You have been kicked from the server for {reason}")

@client.command(name = "mute", description = "mutes someone from text (NOT VOICE) and prevents them from talking in the guild that they were muted in.")
async def mute(ctx, user:discord.User, *, reason="For breaking the rules."):
    await user.mute()
    await user.send(f"You have been muted from a server for {reason}")

@client.command(name = "unmute", description = "unmutes someone from talking in text")
async def unmute(ctx, user:discord.User):
    await user.unmute()
    await user.send("You have been unmuted from a server. Be careful, though, as if you break the rules again you may be muted again.")

@client.command(name = "dm", description = "dms a member of choice, sending whatever message you want and displays the author")
async def dm(ctx, author:discord.User, user:discord.User, *, message):
    await user.send(f"From {ctx.author}, {message}")
    await ctx.send("Message sucessfully delivered!")

@client.command(name = "unban", description = "unbans someone")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command(name = "rickroll", description = "sends a dm to anyone in the guild, with the lyrics of never gonna give you up by Rick Astley")
async def rickroll(ctx, user:discord.User):
    await user.send("We're no strangers to love. You know the rules, and so do I. A full commitment's what I'm thinking of. You wouldn't get this from any other guy. I just wanna tell you how I'm feeling, gotta make you understand. Never gonna give you up, never gonna let you down. Never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye, never gonna tell a lie, and hurt you. We've know each other for so long. Your heart's been aching but you're too shy to say it. Inside we both know what's been goin' on, you know the game and we're gonna play it, and if you ask me how I'm feeling, don't tell me you're too blind to see. Never gonna give you up, never gonna let you down never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you. Never gonna give you up, never gonna let you down. Never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you.")
    await user.send("Never gonna give, never gonna give. (Give you up) We've known each other for so long, your heart's been aching but you're too shy to say it. Inside we both know what's been goin' on, you know the game and we're gonna play it. I just wanna tell you how I'm feeling, gotta make you understand. Never gonna give you up, never gonna let you down. Never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you. Never gonna give you up, never gonna let you down never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you. Never gonna give you up, never gonna let you down. Never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you. Never gonna give you up, never gonna let you down never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you. Never gonna give you up, never gonna let you down. Never gonna run around and desert you. Never gonna make you cry, never gonna say goodbye. Never gonna tell a lie, and hurt you.")

@client.command(aliases=["mass ping"], name = "massping", description = "Pings everyone exactly 261 times (yes I counted)")
@commands.has_permissions(administrator=True)
async def massping(ctx):
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")

@client.command(name = "rps", description = "Fun little rock paper scissors game! nothing much else.")
async def rps(ctx):
    await ctx.send("Make your move in the chat.")
    move = random.randint(1, 3)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["rock", "paper", "scissors"]

    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "rock":
        if move == 1:
            await ctx.send("My move was rock, so it is a draw. Type '!rps' to play again.")
        elif move == 2:
            await ctx.send("My move was paper, so I win. Ha! You lose! Type '!rps' to play again.")
        else:
            await ctx.send("My move was scissors, so I lose. Awww... Type '!rps' to play again.")
    elif msg.content.lower() == "paper":
        if move == 1:
            await ctx.send("My move was rock, so I lose. Awww... Type '!rps' to play again.")
        elif move == 2:
            await ctx.send("My move was paper, so it is a draw. Type '!rps' to play again.")
        else:
            await ctx.send("My move was scissors, so I win. Ha! You lose! Type '!rps' to play again.")
    elif msg.content.lower() == "scissors":
        if move == 1:
            await ctx.send("My move was rock, so I win. Ha! You lose! Type '!rps' to play again.")
        elif move == 2:
            await ctx.send("My move was paper, so I lose. Awww... Type '!rps' to play again.")
        else:
            await ctx.send("My move was scissors, so it is a draw. Type '!rps' to play again.")
    else:
        await ctx.send("What are you THINKING? That's not even rock paper or scissors!")


#slash commands

@slash.slash(name = "ping", description="sends the ping, or latency")
async def ping(ctx : SlashContext):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@slash.slash(name = "beg", description="begging is bad, but don't disrespect beggars (like I did).")
async def beg(ctx : SlashContext):
    await ctx.send("""ey you little beggar, I can't have you begging for anything! GO AWAY!!!!!
*slowly walking away*""")

@slash.slash(name = "pingall", description="pings everyone")
async def pingall(ctx : SlashContext):
    await ctx.send("@everyone")

#events

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Ya idiot, you didn't even include a question, dummy!")

@kick.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lol you dummy, you didn't put a member to kick")

@ban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lol you dummy, you didn't put a member to ban")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't even exist what are you doing tbh")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('managing the server'))
    print("Bot is ready")

@client.event
async def on_member_join(member):
    await member.send(f"{member} has come with our pizza.")

@client.event
async def on_member_remove(member):
    await member.send(f"{member} was the imposter")

client.run("ODQ5ODAzODMxMzM1NzE0ODI3.YLgffQ.Baz4ZUICZ1OIWSpm9XG7oNyZ_rs")