
# replace the name of your of bot with raiden or simply use bot.command()
@Raiden.command()
async def rules(ctx):
  r = song.rules_() # storing all strings from my rules file to r variable
  i = 1
  rules_channel = Raiden.get_channel(1127493094149996594)
  print(ctx.channel.id)
  if ctx.channel.id == 1127493094149996594: # put the id of your rules channel here
    for rules in r:
      
      em = discord.Embed(title= to_upper(f"Rule {i}"), description=f"***{rules}***", colour= ctx.author.color)
      i = i + 1
      await ctx.send(embed = em)
      time.sleep(0.4)
  else:
     em = discord.Embed(title= to_upper("error"), description=f"***You are not in rules channel (go there stupid) *** {rules_channel.mention}", colour= ctx.author.color)
     em.set_image(url= " https://gifdb.com/images/high/mukai-naoya-angry-anime-slap-kn9tjua2wimu0rn9.gif")
     await ctx.send(embed = em)
