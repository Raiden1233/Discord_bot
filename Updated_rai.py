
import discord
from discord import app_commands
from discord.ext import commands
import random
import logging
import time
import requests
import generator as g
import os






intents = discord.Intents.default()
intents.message_content = True
intents.members = True



Raiden = commands.Bot(command_prefix=">", intents=discord.Intents.all())

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

Raiden.remove_command("help")

# discord.Intents.all()






#_____________________________________________________________________________________________________
# An event for showing that the raiden is ready to go 
@Raiden.event
async def on_ready():
    print(f"{Raiden.user} Has succussfully logged in.")
    await Raiden.change_presence(status= discord.Status.idle, activity= discord.Game('With Peoples'), )
    
    
    print("--------------------------------------------------------------------------------")
    s = await Raiden.tree.sync()
    Raiden.add_view(Roles())
    print(s)

class Roles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label = "📢", custom_id = "Announcement", style = discord.ButtonStyle.secondary)
  async def button1(self, interaction, button):
    role = 1129944467349184523 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)

  
  @discord.ui.button(label = "♂️", custom_id = "Male", style = discord.ButtonStyle.secondary)
  async def button2(self, interaction, button):
    role = 1130613893463543809  #put your role id here
    user = interaction.user 
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)
  
  
  @discord.ui.button(label = "♀️", custom_id = "Female", style = discord.ButtonStyle.secondary)
  async def button3(self, interaction, button):
    role = 1130613987134939136 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "⚧️", custom_id = "Others", style = discord.ButtonStyle.secondary)
  async def button4(self, interaction, button):
    role = 1130614079426416773 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🧠", custom_id = "brainstormers~", style = discord.ButtonStyle.secondary)
  async def button5(self, interaction, button):
    role = 1130614206408962058 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🎵", custom_id = "Music~", style = discord.ButtonStyle.secondary)
  async def button6(self, interaction, button):
    role = 1130749504245747774 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)    
  


  @discord.ui.button(label = "❌", custom_id = "14-18", style = discord.ButtonStyle.secondary)
  async def button7(self, interaction, button):
    role = 1130746241198850131 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True) 


  @discord.ui.button(label = "✅", custom_id = "18+", style = discord.ButtonStyle.secondary)
  async def button8(self, interaction, button):
    role = 1130746378692341792 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "💀", custom_id = "25-30", style = discord.ButtonStyle.secondary)
  async def button9(self, interaction, button):
    role = 1130746480660062309 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)



  @discord.ui.button(label = "👀", custom_id = "30+", style = discord.ButtonStyle.secondary)
  async def button10(self, interaction, button):
    role = 1130749389497970800 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "😘", custom_id = "Bump", style = discord.ButtonStyle.secondary)
  async def button11(self, interaction, button):
    role = 1131362847625056256 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🫠", custom_id = "Weird_Talkers", style = discord.ButtonStyle.secondary)
  async def button12(self, interaction, button):
    role = 1131363802684866650 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)         


  @discord.ui.button(label = "🎉", custom_id = "Welcomers", style = discord.ButtonStyle.secondary)
  async def button13(self, interaction, button):
    role = 1131948684230283406 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🙈", custom_id = "Selfie", style = discord.ButtonStyle.secondary)
  async def button14(self, interaction, button):
    role = 1131955006673780808 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "😎", custom_id = "Movie/Anime", style = discord.ButtonStyle.secondary)
  async def button15(self, interaction, button):
    role = 1132007404817633281 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)    


@Raiden.command()
async def roles(ctx):
  embed = discord.Embed(title = to_upper("Role Selection Form"), description = "1: 𝙋𝙧𝙚𝙨𝙨 📢 𝙩𝙤 𝙖𝙙𝙙 𝙖𝙣𝙣𝙤𝙪𝙣𝙘𝙚𝙢𝙚𝙣𝙩 𝙧𝙤𝙡𝙚.\n\n2: 𝙋𝙧𝙚𝙨𝙨 ♂️ 𝙞𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙢𝙖𝙡𝙚 ( ͠❛ ͜ʖ ͠❛ ) \n\n3: 𝙋𝙧𝙚𝙨𝙨 ♀️ 𝙞𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙛𝙚𝙢𝙖𝙡𝙚 ( ͠❛ ͜ʖ ͠❛ )\n\n4: 𝙋𝙧𝙚𝙨𝙨 ⚧️ 𝙁𝙤𝙧 𝙤𝙩𝙝𝙚𝙧𝙨.\n\n5: 𝙋𝙧𝙚𝙨𝙨🧠 𝙄𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙞𝙣𝙩𝙚𝙡𝙡𝙞𝙜𝙚𝙣𝙩.\n\n6:𝙋𝙧𝙚𝙨𝙨 🎵 𝙏𝙤 𝙨𝙝𝙖𝙧𝙚 𝙮𝙤𝙪𝙧 𝙢𝙪𝙨𝙞𝙘.\n\n7:𝙋𝙧𝙚𝙨𝙨 ❌ 𝙞𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙪𝙣𝙙𝙚𝙧 14-18\n\n8:𝙋𝙧𝙚𝙨𝙨 ✅ 𝙞𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 18+\n\n9:𝙋𝙧𝙚𝙨𝙨 💀 𝙞𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙪𝙣𝙙𝙚𝙧 25-30\n\n10:𝙋𝙧𝙚𝙨𝙨 👀 𝙞𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 30+\n\n11:𝙋𝙧𝙚𝙨𝙨 😘 𝙩𝙤 𝙜𝙚𝙩 𝙗𝙪𝙢𝙥 𝙨𝙚𝙧𝙫𝙚𝙧.\n\n12:𝙋𝙧𝙚𝙨𝙨🫠𝙩𝙤 𝙜𝙚𝙩 𝙒𝙚𝙞𝙧𝙙 𝙩𝙖𝙡𝙠𝙚𝙧𝙨 𝙧𝙤𝙡𝙚 𝙛𝙤𝙧 𝙩𝙝𝙚 𝙬𝙚𝙞𝙧𝙙 𝙘𝙝𝙖𝙩.\n\n13:𝙋𝙧𝙚𝙨𝙨 ≧◠‿◠≦🎉 𝙛𝙤𝙧 𝙬𝙚𝙡𝙘𝙤𝙢𝙚𝙧𝙨 𝙧𝙤𝙡𝙚\n\n14:𝙋𝙧𝙚𝙨𝙨 🙈 𝙞𝙛 𝙮𝙤𝙪 𝙬𝙖𝙣𝙣𝙖 𝙨𝙝𝙖𝙧𝙚 𝙨𝙚𝙡𝙛𝙞𝙚𝙨.\n\n15:𝙋𝙧𝙚𝙨𝙨 😎 𝙩𝙤 𝙜𝙚𝙩 𝙚𝙣𝙩𝙚𝙧𝙩𝙖𝙞𝙣𝙢𝙚𝙣𝙩 𝙧𝙤𝙡𝙚")
  await ctx.send(embed = embed, view = Roles())


def to_upper(argument):
    return argument.upper()



#_____________________________________________________________________________________________________
def questions():
    with open('question.txt', 'r', encoding='utf8') as f:
        question = f.readlines()

    return random.choice(question)


#_____________________________________________________________________________________________________

#_____________________________________________________________________________________________________
# Event to mention the user who joining the server
@Raiden.event
async def on_member_join(member: discord.Member):
    welcome_channel_id = Raiden.get_channel(1126089252409720972) #put the channel id where u want the to show the welcome Embed
    general_chat_id = Raiden.get_channel(1121115370854547459) #put the channel id of genral chat
    rules_id = Raiden.get_channel(1127493094149996594) #put the channel id of rules
    avatar = member.avatar
    # rules = Raiden.get_channel(1127493094149996594)
  
    
    em = discord.Embed(title=to_upper("> Welcome"), description=f"𝙃𝙚𝙮! {member.mention}, 𝙬𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝙨𝙚𝙧𝙫𝙚𝙧.\n𝙏𝙝𝙖𝙣𝙠𝙨 𝙛𝙤𝙧 𝙟𝙤𝙞𝙣𝙞𝙣𝙜 𝙩𝙝𝙚 𝙨𝙚𝙧𝙫𝙚𝙧 :3\n𝙃𝙤𝙥𝙚 𝙮𝙤𝙪'𝙡𝙡 𝙚𝙣𝙟𝙤𝙮 𝙮𝙤𝙪𝙧 𝙩𝙞𝙢𝙚 𝙝𝙚𝙧𝙚 <3\n𝙈𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙤 𝙧𝙚𝙖𝙙 𝙖𝙡𝙡 𝙩𝙝𝙚 {rules_id.mention} 𝙖𝙣𝙙 𝙛𝙤𝙡𝙡𝙤𝙬 𝙩𝙝𝙚𝙢<3")
    em.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2021/12/24/138342831/91f844f579855247b96030dfc3386213_895886571671433499.gif")
    em.set_thumbnail(url= avatar)
    
    server = Raiden.get_guild(1121115369646608434)
    role = discord.utils.get(server.roles, name="Friends")
    # member.leave(member=member)
    welcome_role = discord.utils.get(server.roles, name="Welcomers")
    

    

    await member.add_roles(role)
    await welcome_channel_id.send(embed= em)
    print("Person has joined the guild")
    await general_chat_id.send(f"{role} role has assigned to {member.mention}!",)
    await general_chat_id.send("Welcome don't forget to get roles or I'll tickle your toes")
    await general_chat_id.send(f"{welcome_role.mention} new person had joined the guild")
#_____________________________________________________________________________________________________

#_____________________________________________________________________________________________________
# An even to play 8balls game
def eight_ballss(argument):
    ls = [
        "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", 
        "You may rely on it", "As I see it yes", "Most likely", "Outlook good", "Yes", 
        "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", 
        "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", 
        "My sources say no", "Outlook not so good", "Very doubtful"
        ]

    if argument.startswith("8balls"):
        
        return random.choice(ls)
#_____________________________________________________________________________________________________

#an event to deal with normal messages for raiden


@Raiden.event
async def on_message(message):
    if message.author == Raiden.user:
        return


    if message.content.startswith("$"):
        if message.content == "$hello":
            
            await message.channel.send(to_upper("hello there"))


    if message.content.startswith("8"):
        v = eight_ballss("8balls")

        em = discord.Embed(title=to_upper("8balls"), description=v)
        em.set_thumbnail(url= "https://media.giphy.com/avatars/P8ball/BKVY30EuiZPu.gif")
        await message.channel.send(embed= em)
    await Raiden.process_commands(message)
#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________



@Raiden.tree.command(name='anonymous', description='Send message anonymously')
async def anonymous(interaction: discord.Interaction, message: str):  
   em = discord.Embed(title = f'⌦ 𓊈𒆜 ANONYMOUS MESSAGE 𒆜𓊉࿐☠️ \n',description = f'** ♡˗ˏ✎ ➔**  {message} \n\n ╰┈➤Volume: ■■■■■□□□' )
   em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
   await interaction.channel.send(embed= em)
   await interaction.response.send_message(f'✅ **Your message has been sent anonymously :>**', ephemeral=True)

#_____________________________________________________________________________________________________
# a command to sum to numbers
@Raiden.tree.command()
async def add(ctx: discord.Interaction, num1: str, num2: str):
    answer = int(num1) + int(num2)
    em = discord.Embed(title = 'SOMEONE CANNOT SUM HERE LMAOO!!!!',description = f"> **Here, The sum of {num1} and {num2} is: **``{answer}``  ***Lmaoo!!***" )
    if type(answer) is int:

      await ctx.response.send_message(embed= em)
    else:
      await ctx.response.send_message('> please provide integers only!')
       
#_____________________________________________________________________________________________________
# Importing my rules file 
import song

#_____________________________________________________________________________________________________
@Raiden.command()
async def rules(ctx):
  r = song.rules_() # storing all strings from my rules file to r variable
  i = 1
  rules_channel = Raiden.get_channel(1127493094149996594) # here you need to put the id of rules channel 
  if ctx.channel.id == 1127493094149996594: # put the id of your rules channel here
    em = discord.Embed(colour= ctx.author.color)
    em.set_image(url='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanhnc3Q3OTI0bWRpMDJnc2thbDhnbzV4djFyZTRqbXA1Z2pwOHY1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/yugxK5nU8pWBmrcK1Z/giphy.gif')
    await ctx.send(embed = em)
    for rules in r:
      
      em = discord.Embed(title= to_upper(f"Rule {i}"), description=f"***{rules}***", colour= ctx.author.color)
      em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
      em.set_thumbnail(url='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanhnc3Q3OTI0bWRpMDJnc2thbDhnbzV4djFyZTRqbXA1Z2pwOHY1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/yugxK5nU8pWBmrcK1Z/giphy.gif')
      i = i + 1
      await ctx.send(embed = em)
      time.sleep(0.4)
  else:
     em = discord.Embed(title= to_upper("error"), description=f"***You are not in rules channel (go there stupid) *** {rules_channel.mention}", colour= ctx.author.color)
     em.set_image(url= " https://tenor.com/view/no-head-shaking-anime-nope-gif-14958903")
     await ctx.send(embed = em)

#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________
@Raiden.tree.command(name='addrole', description='To add role to anyone\nType specific role you want to add to a member as well as mention the member')
async def addrole(ctx: discord.Interaction,  role: str, member: discord.Member):
   
   if ctx.user.id == 874561925856505857: # here u need to put onwers id cause i made this command only for owner
    roles = discord.utils.get(ctx.guild.roles , name= role)

    
    await member.add_roles(roles)
    await ctx.response.send_message(f'> {roles} role is ***assigned*** to: {member}')
   else:
      await ctx.response.send_message('> You are not allowed to use this command. Contact owner for more information.\n***Thank You!***')


#_____________________________________________________________________________________________________
import asyncio
#_____________________________________________________________________________________________________
@Raiden.command()
async def say(ctx, *, args):
  print(len(args))
  authorname = ctx.author
  authorid = ctx.author.id
  authoraccess = f'https://discord.com/users/{authorid}'
  authoravatar = ctx.author.avatar
  

  async with ctx.typing():
    await asyncio.sleep(2)
    em = discord.Embed(title= f'> Imitating->{authorname}', description= f'> `` {args} ``', colour= ctx.author.color)
    em.set_author(name= authorname, icon_url= authoravatar , url=authoraccess)
    em.set_image(url="https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10")
    await ctx.reply(embed = em)
    await ctx.message.delete()
  await asyncio.sleep(0.5)
  await ctx.send("***Done! Senpai!!!!***")


#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________


# A command for ping pong 
@Raiden.command()
async def ping(ctx):
    before = time.monotonic()
    await ctx.send("Here")
    ping = (time.monotonic() - before) * 1000
    em = discord.Embed(description= f"**Ponggggggggggg~~~~~!**    `{int(ping)}ms`" , colour= ctx.author.color)
    em.set_image(url="https://thumbs.gfycat.com/GoldenScaryBlowfish-size_restricted.gif")
    await ctx.channel.send(embed = em)

#_____________________________________________________________________________________________________

@Raiden.command(name="password")
async def password(context):
    password = g.random_()

    print(f"Someone generated Password : {password}")
    os.remove("password.txt") 

    em = discord.Embed(title= '> RANDOM PASSWORD', description=f"> **ʜᴇʀᴇ ɪs ʏᴏᴜʀ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴘᴀssᴡᴏʀᴅ: ** `` {password} ``", colour= context.author.color)
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')

    await context.channel.send(embed = em)


#_____________________________________________________________________________________________________
# question game

@Raiden.command()
async def question(ctx):
  q = questions()

  print(f'someone asked\n{q}')

  em = discord.Embed(title= to_upper("> question!"), description=f"> {q}", colour= ctx.author.color)
  em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')

  await ctx.channel.send(embed = em)
#_____________________________________________________________________________________________________
# A command to kick or ban members

@Raiden.command()
@commands.has_permissions(kick_members = True)
async def remove(context, member: discord.Member, reason = 'not specified'):
    
    role = discord.utils.get(context.guild.roles , name = "Owner") # put the roles names of your choice i used owner and admin roles cause i don't want other people to use this command.
    role2 = discord.utils.get(context.guild.roles , name = "admin")

    if context.author == member:
       em = discord.Embed(title=to_upper("what a stupid person"), description=f"{member.mention} you can't remove yourself STUPID!")
       em.set_image(url= "https://gifdb.com/images/high/mukai-naoya-angry-anime-slap-kn9tjua2wimu0rn9.gif")   
       await context.channel.send(embed = em)
    elif role in context.author.roles or role2 in context.author.roles:
       
        em = discord.Embed(title=to_upper("removed"), description=f"{member.mention} is removed from the server\nReason: {reason}")
        em.set_image(url= " https://gifdb.com/images/high/anime-fight-flying-kick-o4ddmhew9wwdpp5w.gif")   
        await context.channel.send(embed = em)
        await context.guild.kick(discord.Object(id= member.id))
    else:
        await context.reply("you are not allowed to remove members from the server")
        
        
        


@Raiden.command()
@commands.has_permissions(kick_members = True)
async def ban(context, member: discord.Member):
    
    role = discord.utils.get(context.guild.roles , name = "Owner") # put the roles names of your choice i used owner and admin roles cause i don't want other people to use this command.
    role2 = discord.utils.get(context.guild.roles , name = "admin")

    if context.author == member:
       em = discord.Embed(title=to_upper("what a stupid person"), description=f"{member.mention} you can't ban yourself STUPID!")
       em.set_image(url= "https://gifdb.com/images/high/mukai-naoya-angry-anime-slap-kn9tjua2wimu0rn9.gif")   
       await context.channel.send(embed = em)

    elif role in context.author.roles or role2 in context.author.roles:
        em = discord.Embed(title=to_upper("kicked"), description=f"{member.mention} is banned from the server\nReason: not specified.")
        em.set_image(url="https://media.tenor.com/HLx4m-urlBEAAAAC/kick-anime.gif")   
        await context.channel.send(embed = em)
        await context.guild.ban(discord.Object(id= member.id))
    else:
        await context.channel.send("Sorry you dont have permission to ban anyone.")
#_____________________________________________________________________________________________________________________________
# an event to hug , kiss, pet, slap discord users in server

gifs_url = ["https://usagif.com/wp-content/uploads/gif/anime-hug-59.gif","https://usagif.com/wp-content/uploads/gif/anime-hug-79.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-63.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-73.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-1.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-3.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-6.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-65.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-13.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-20.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-81.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-21.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-23.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-26.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-33.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-36.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-37.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-41.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-42.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-53.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-57.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-66.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-67.gif","https://usagif.com/wp-content/uploads/gif/anime-hug-69.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-74.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-76.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-80.gif", "https://usagif.com/wp-content/uploads/gif/anime-hug-14.gif",
            "https://usagif.com/wp-content/uploads/gif/anime-hug-52.gif", "https://media.giphy.com/media/IRUb7GTCaPU8E/giphy.gif",
            "https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif", "https://media.giphy.com/media/LIqFOpO9Qh0uA/giphy.gif",
            "https://media.giphy.com/media/49mdjsMrH7oze/giphy.gif","https://media.giphy.com/media/49mdjsMrH7oze/giphy.gif",
            "https://media.giphy.com/media/Ph8gm8bhJCEgmO4n7z/giphy.gif", "https://media.giphy.com/media/f6y4qvdxwEDx6/giphy.gif",
            "https://media.giphy.com/media/aD1fI3UUWC4/giphy.gif", "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-58.gif",
            "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-57.gif", "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-52.gif",
            "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-52.gif", "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-41.gif",
            "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-25.gif"
            ]

gifs_pet_url = ["https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif", "https://media.giphy.com/media/ye7OTQgwmVuVy/giphy.gif",
                "https://media.giphy.com/media/109ltuoSQT212w/giphy.gif", "https://media.giphy.com/media/xVgGouGtc21H2/giphy.gif",
                "https://media.giphy.com/media/osYdfUptPqV0s/giphy.gif", "https://media.giphy.com/media/Z7x24IHBcmV7W/giphy.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-2.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-1.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-13.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-11.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-12.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-10.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-9.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-8.gif",
                " https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-6.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-19.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-17.gif", " https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-14.gif",
                " https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-24.gif" , "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-24.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-26.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-26.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-40.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-37.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-36.gif", "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-33.gif",
                "https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-head-pat-gifs-32.gif"
                    ]
anime_kick_urls = [" https://media.tenor.com/icV2ba3gU7MAAAAM/kick-anime.gif", " https://i.pinimg.com/originals/91/0b/6b/910b6b5cd2cfa1c98be615b53897e62b.gif",
                   " https://i.pinimg.com/originals/3f/21/2a/3f212a46e353c61c839a107d755048cd.gif", " https://media.tenor.com/IlaJyD0XEMwAAAAC/index-anime.gif",
                   " https://i.makeagif.com/media/2-24-2016/XzDZ9h.gif", " https://64.media.tumblr.com/a20e21f75393bcc7709e16cb6d07429f/tumblr_psab4sgpiC1sk6fb9_1280.gif",
                   "https://i.pinimg.com/originals/44/6f/49/446f49e675e38e1bb10d226f12519092.gif", " https://64.media.tumblr.com/1ae35cc7d78b5e579d5baabe3f0c03db/93cab037caf29e98-82/s540x810/00a2d481867ccd79d1302aced86271584594dae9.gif",
                   " https://giffiles.alphacoders.com/921/92147.gif", "https://i.kym-cdn.com/photos/images/newsfeed/001/053/707/042.gif",
                   " https://i.pinimg.com/originals/e2/85/3a/e2853aff4a34f7487edce8f69cfb2d01.gif", " https://i.kym-cdn.com/photos/images/original/002/401/225/c0c.gif",
                   " https://i.kym-cdn.com/photos/images/original/001/901/624/515.gif", " https://media.tenor.com/BtwpZlg90ZkAAAAC/kick-anime.gif",
                   " https://i.gifer.com/OHNW.gif", "https://media.tenor.com/_R4OnJYIeYcAAAAd/anime-kick.gif",
                   " https://2.bp.blogspot.com/-58a9DDQ9bfc/WIZzChNFw0I/AAAAAAAAt5s/yIHCOiaFWngmaV7Uw27XeHdApdxVaz4jwCPcB/s1600/Omake%2BGif%2BAnime%2B-%2BGabriel%2BDropOut%2B-%2BEpisode%2B3%2B-%2BGab%2BKicks%2BSatania.gif",
                   
                ]
anime_kissing_urls = ["https://usagif.com/wp-content/uploads/anime-kissin-2.gif", "https://usagif.com/wp-content/uploads/anime-kissin-1.gif", "https://usagif.com/wp-content/uploads/anime-kissin-16.gif",
                      "https://usagif.com/wp-content/uploads/anime-kissin-17.gif", " https://usagif.com/wp-content/uploads/anime-kissin-19.gif", " https://usagif.com/wp-content/uploads/anime-kissin-5.gif",
                      "https://usagif.com/wp-content/uploads/anime-kissin-6.gif", " https://usagif.com/wp-content/uploads/anime-kissin-7.gif", " https://usagif.com/wp-content/uploads/anime-kissin-8.gif",
                      " https://usagif.com/wp-content/uploads/anime-kissin-9.gif", " https://usagif.com/wp-content/uploads/anime-kissin-10.gif", " https://usagif.com/wp-content/uploads/anime-kissin-12.gif",
                      " https://usagif.com/wp-content/uploads/anime-kissin-13.gif", "https://usagif.com/wp-content/uploads/anime-kissin-15.gif", " https://usagif.com/wp-content/uploads/anime-kiss-35.gif",
                      " https://usagif.com/wp-content/uploads/anime-kiss-33.gif", " https://usagif.com/wp-content/uploads/anime-kiss-32.gif", " https://usagif.com/wp-content/uploads/anime-kiss-31.gif",
                      "https://usagif.com/wp-content/uploads/anime-kiss-30.gif", "https://usagif.com/wp-content/uploads/anime-kiss-28.gif", "https://usagif.com/wp-content/uploads/anime-kiss-26.gif",
                      "https://usagif.com/wp-content/uploads/anime-kiss-23.gif", "https://usagif.com/wp-content/uploads/anime-kiss-22.gif", "https://usagif.com/wp-content/uploads/anime-kiss-20.gif",
                      "https://usagif.com/wp-content/uploads/anime-kiss-19.gif", " https://usagif.com/wp-content/uploads/anime-kiss-17.gif", "https://usagif.com/wp-content/uploads/anime-kiss-15.gif",
                      "https://usagif.com/wp-content/uploads/anime-kiss-13.gif", "https://usagif.com/wp-content/uploads/anime-kiss-10.gif", "https://usagif.com/wp-content/uploads/anime-kiss-6.gif"
                    ]

slap_anime_url = ["https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif", "https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
                  "https://gifdb.com/images/high/mukai-naoya-angry-anime-slap-kn9tjua2wimu0rn9.gif", "https://gifdb.com/images/high/mad-anime-female-character-slap-0zljynqqf0gopfhg.gif",
                  "https://gifdb.com/images/high/revenge-anime-slap-over-bread-4zr2a8mslm7ov2sm.gif", "https://gifdb.com/images/high/girl-s-last-tour-anime-slap-51dqai0u072jrc21.gif",
                  "https://gifdb.com/images/high/strong-throw-up-anime-slap-ffszl7lbg930n4gt.gif", "https://gifdb.com/images/high/kokoro-wake-up-anime-slap-lpcv2c43am2bfsl8.gif",
                  "https://gifdb.com/images/high/zombie-land-saga-anime-slap-8w2vx6zxpbijxq85.gif", "https://gifdb.com/images/high/yuruyuri-akari-kyoko-anime-slap-fcacgc0edqhci6eh.gif",
                  "https://gifdb.com/images/high/up-close-angry-anime-slap-lf84tjs2sgx8obdr.gif", "https://gifdb.com/images/high/angry-girl-student-anime-slap-srn4m1rzgboj6gts.gif",
                  "https://gifdb.com/images/high/blushing-female-anime-slap-m5wqeyulkwcnqae7.gif", "https://gifdb.com/images/high/funny-horse-head-anime-slap-mhazsm4ruyxnsr5j.gif",
                  "https://gifdb.com/images/high/mad-gangster-anime-slap-nnulodryf9gpmj9n.gif", "https://gifdb.com/images/high/sweet-anime-slap-sara-no-method-cdlnjmondb9vbf27.gif",
                  "https://gifdb.com/images/high/anime-slap-angry-sakura-haruno-coubcjfgw0yx9z17.gif", "https://gifdb.com/images/high/tsukimichi-mio-fast-anime-slap-2lyodw81eyovnfjq.gif"

                ]

kick_names = ["Kicking", "kicked", "kicking hard ", "just kicked", "kicked cutely"]
hug_names = ["Hugs","Hugging","Cuddling","Doing something to~"]
pet_names  = ["Petting", "Headpets to ", " Petting head of", " Giving head pet"]
kissing_names = ["Kissing", "kissed", "Justt kissed~", "Giving Kiss to~"]
slapping_names = ["Slaps", "slapped", "slapping", "Just slapped"]


@Raiden.command()
async def hug(ctx, *, member : discord.Member):
        embed = discord.Embed(
            title= to_upper("hug!"),
            colour=ctx.author.color,
            description=f"{ctx.author.mention} {random.choice(hug_names)} {member.mention}"
        )
        embed.set_image(url=(random.choice(gifs_url)))

        await ctx.send(embed=embed)


@Raiden.command()
async def pet(ctx, *, member : discord.Member):
        embed = discord.Embed(
            title=to_upper("head_pet!"),
            colour=ctx.author.color,
            description=f"{ctx.author.mention} {random.choice(pet_names)} {member.mention}"
        )
        embed.set_image(url=(random.choice(gifs_pet_url)))

        await ctx.send(embed=embed)


@Raiden.command()
async def kick(ctx, *, member : discord.Member):
        embed = discord.Embed(
            title=to_upper("kicking!"),
            color= ctx.author.color,
            description=f"{ctx.author.mention} {random.choice(kick_names)} {member.mention}"
        )
        embed.set_image(url= random.choice(anime_kick_urls))

        await ctx.channel.send(embed = embed)


@Raiden.command()
async def kiss(context, *, member : discord.Member):
        embed = discord.Embed(
            title= to_upper("kissue!"),
            color= context.author.color,
            description= f"{context.author.mention} {random.choice(kissing_names)} {member.mention}"
            
        )
        embed.set_image(url= random.choice(anime_kissing_urls))

        await context.channel.send(embed = embed)


@Raiden.command()
async def slap(context, *, member : discord.Member):
        embed = discord.Embed(
            title= to_upper("slapping!"),
            color= context.author.color,
            description= f"{context.author.mention} {random.choice(slapping_names)} {member.mention}"
            
        )
        embed.set_image(url= random.choice(slap_anime_url))

        await context.channel.send(embed = embed)
#___________________________________________________________________________________________________________________________

#___________________________________________________________________________________________________________________________
# an event to show user avatars

@Raiden.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar

    em = discord.Embed(title=f"{to_upper('avatar')} of {avamember._user}")
    em.set_image(url= userAvatarUrl)
    await ctx.send(embed= em)
    print(userAvatarUrl)

    url = userAvatarUrl
    
    response = requests.get(url)

    with open("Avatar.jpg", 'wb') as o:
         o.write(response.content)


#_______________________________________________________________________________________________________________________________
# Avatars command to see multiple avatars at once
@Raiden.command()
async def avatars(ctx, members: commands.Greedy[discord.Member]):
  ls = []
  for urls in members:
      ls.append(urls.avatar)
      

  if len(ls) > 1:
    for avatarr in members:  
      em = discord.Embed(title=f"{to_upper('avatar')} of {avatarr._user}")
      em.set_image(url= avatarr.avatar)
      
      await ctx.send(embed= em)

  elif len(ls) < 2:
    em = discord.Embed(
                title= 'Error!',
                description= 'Sorry ***This function*** is only to check multiple users avatar at sametime\n use ***>avatar*** to check only **1 person avatar** at a time. <3 Thank you!',
                color= ctx.author.color                      
                        )
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.send(embed = em)

#_______________________________________________________________________________________________________________________________        
  

#_______________________________________________________________________________________________________________________________
# A command to check all  commands
@Raiden.group(invoke_without_command= True)
async def help(ctx):
    em = discord.Embed(title="Help", description="Use >help <command_name> for extend information related to that command")

    em.add_field(name= to_upper("moderation !"), value="> remove\n> ban\n> autorole")
    em.add_field(name= to_upper("fun !"), value="> 8balls\n> hug\n> say \n> avatar\n> avatars \n> add [ slash command ] \n> kick\n> kiss\n> pet \n> slap \n> password\n> question\n> addrole\n> anonymous [ slash command ]")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)

@help.command()
async def remove(ctx):
    em = discord.Embed(title="remove", description="> To remove a member from the server", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">remove (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def pet(ctx):
    em = discord.Embed(title="Headpet", description="> To pet someone in your server", color=ctx.author.color)
    em.add_field(name="**Pet**", value=">pet (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def slap(ctx):
    em = discord.Embed(title="Slap", description="> To slap a member from the server", color=ctx.author.color)
    em.add_field(name="**Slap**", value=">slap (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def avatars(ctx):
    em = discord.Embed(title="Avatars", description="> To check many avatars at same time", color=ctx.author.color)
    em.add_field(name="**Avatars**", value=">avatars (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)



@help.command()
async def say(ctx):
    em = discord.Embed(title="say", description="> To let your bot imitate what you type ", color=ctx.author.color)
    em.add_field(name="**say**", value=">say (Your message) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)



@help.command()
async def anonymous(ctx):
    em = discord.Embed(title="anonymous", description="> To send message anonymously", color=ctx.author.color)
    em.add_field(name="**/anonymous**", value="Just enter your message ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def addrole(ctx):
    em = discord.Embed(title="addrole", description="> To add any role to server memeber", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">addrole  (role_name)  (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def question(ctx):
    em = discord.Embed(title="question", description="> Korone will ask you questions.", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">question")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)



@help.command()
async def kiss(ctx):
    em = discord.Embed(title="remove", description="> To kiss a member from the server", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">kiss (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def password(ctx):
    em = discord.Embed(title="password", description="> To to get random generated password", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">password  ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def kick(ctx):
    em = discord.Embed(title="remove", description="> To kick someone from the server", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">kick (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def ban(ctx):
    em = discord.Embed(title="ban", description="> To ban any member in the server", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">ban (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em) 


@help.command()
async def hug(ctx):
    em = discord.Embed(title="Hug", description="> To Hug any member in the server", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">hug (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command()
async def add(ctx):
    em = discord.Embed(title="Add", description="> To check the sum of two numbers", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">add (1st Number) (2nd Number) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em) 


@help.command()
async def avatar(ctx):
    em = discord.Embed(title="Avatar", description="> To check avatar of any person in the server", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=">avatar (Mention_member) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)


@help.command("8balls")
async def eight_balls(ctx):
    em = discord.Embed(title="8balls", description="> To ask random questions to bot", color=ctx.author.color)
    em.add_field(name="**Syntax**", value="8balls (Ask Questions) ")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)  


@help.command()
async def autorole(ctx):
    em = discord.Embed(title="autorole", description="> It is to assign friends role automatically to new person", color=ctx.author.color)
    em.add_field(name="**Syntax**", value="Works automatically")
    em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
    await ctx.channel.send(embed = em)
#___________________________________________________________________________________________________________________________ 


#_______________________________________________________________________________________________________________________________
                 
TOKEN = "MTExMjA2NDE3NjE3MzYxMzIyNg.GJ6FPK.xachqjwBpbEs35l7NjQZkJRwBVz78AmhEGI_Z0"

Raiden.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
    