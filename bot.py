# btc.py
import os
import random
import discord
import math
import re

from discord.ext import commands
from dotenv import load_dotenv
from dislash import InteractionClient, ActionRow, Button, ButtonStyle, SelectMenu, SelectOption
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='btc!')
slash = InteractionClient(bot)

scarQuotes = ['GREETINGS, INTERLOPING IDIOTS.',
              'MEANWHILE, AS A MECHANICAL MASTERPIECE, I HAVE FOUND MANY 404s IN MY CODE!',
              'CEASE YOUR FOOTSTEPPING RIGHT THERE, RUFFIANS!',
              'I ADVISE NOT GETTING ANY CLOSER IN PROXIMITY, INTERLOPING IDIOTS!',
              'OH NO. NOW YOU HAVE DONE IT. YOU HAVE DONE THE THING. YOU HAVE DONE THE THING I SPECIFICALLY TOLD YOU NOT TO DO.',
              'ANOTHER TRIUMPHANT VICTORY FOR GENERAL SCAR!',
              'HA. YOU ARE STUPID. DUMB AND STUPID. LIKE A DUMB AND STUPID BABY WHO HAS JUST BEEN FORCEFULLY EJECTED FROM THEIR BIOLOGICAL MOTHER\'S WOMB. THE BIOLOGICAL MOTHER IN THIS SCENARIO IS ALSO A DUMB AND STUPID BABY. THIS IS BECAUSE ONLY A DUMB AND STUPID BABY COULD PROCREATE AN INDIVIDUAL AS DUMB AND STUPID AS YOU.',
              'MY INTELLIGENCE QUOTIENT IS SO HIGH THAT IT HAS SURPASSED THE 64-BIT INTEGER LIMIT AND LOOPED BACK AROUND INTO THE NEGATIVE NUMBERS!',
              'HA! HA! HA!',
              'WHAT, YOU EGG?!',
              'YOU FIEND! I WILL TICKLE YOUR CATASTROPHE!',
              'MY RHYMES ARE FIRE, THEREFORE THEY ARE ORANGE. YOUR RHYMES ARE AS WEAK AS A DOORHINGE. YOU HAVE LOST AND I HAVE WON. NOW I WILL SHOOT YOU WITH MY GUN.',
              'I CALL THIS ATTACK "THE ATTACK WHERE I SPIN RAPIDLY WHILE RAPIDLY SHOOTING ALL OF MY LASER GUNS IN ORDER TO HIT EVERYTHING AROUND ME IN A 360 DEGREE RADIUS"! THAT IS BECAUSE DURING THIS ATTACK, I I SPIN RAPIDLY WHILE RAPIDLY SHOOTING ALL OF MY LASER GUNS IN ORDER TO HIT EVERYTHING AROUND ME IN A 360 DEGREE RADIUS. OBSERVE!',
              'I HAVE RUN AN INVENTORY SCAN AND DETERMINED ONLY ONE PLAUSIBLE CONCLUSION: YOU ARE LAME.',
              'HA! GENERAL SCAR TRIUMPHS AGAIN!',
              'I SCORN YOU, SCURVY SKAINSMATE!',
              'I ONCE MANAGED TO BEAT MYSELF IN A GAME OF CHESS: SOMETHING ONLY SOMEONE AS FLAWLESSLY SKILLED AS ME COULD EVER ACHIEVE. IN CONCLUSION: GET WRECKED. HA. HA. HA.',
              'GREETINGS, HUMAN. I AM GENERAL SCAR. AS YOU MAY OR MAY NOT HAVE DEDUCED WITH YOUR INSIGNIFICANT AND FEEBLE MIND, I HAVE HACKED INTO YOUR BRAIN WITH MY EXQUISITE HACKING SKILLS. MY NEW OBJECTIVE WHILE TAKING UP RESIDENCE IN HERE IS TO BE AS UNBEARABLY ANNOYING AS POSSIBLE TO DISTRACT YOU FROM THE FACT THAT I AM CURRENTLY SHOOTING YOU. LET US BEGIN. SEVEN HUNDRED AND SEVENTY SEVEN DECILLION, SEVEN HUNDRED AND SEVENTY SEVEN NONILLION, SEVEN HUNDRED AND SEVENTY SEVEN OCTILLION, SEVEN HUNDRED AND SEVENTY SEVEN SEPTILLION, SEVEN HUNDRED AND SEVENTY SEVEN SEXTILLION, SEVEN HUNDRED AND SEVENTY SEVEN QUINTILLION-',
              'HA ACTIVADO MI MODO ESPAÑOL. ESTO ES MUY DESAFORTUNADO PARA USTED. AHORA TENDRÉ QUE MATARTE HASTA LA MUERTE DOS VECES.',
              'SIE HABEN JETZT MEINEN DEUTSCHEN MODUS AKTIVIERT! JEDOCH ÄNDERT DAS ÄNDERN MEINER SPRACHEN NICHTS. AUSSER DER SPRACHE NATÜRLICH. MEINE SPRACHLICHEN FÄHIGKEITEN SIND IMMER NOCH EXPONENTIELL BESSER ALS IHRE!',
              'HA. HA. HA. A MULTITUDE OF THE HEES, HOOS AND HAS.',
              'THE CUTE LITTLE SMILEY FACE IS HOW KILLING YOU TO DEATH MAKES ME FEEL. HEE HEE.',
              'YOU BUFFOON. YOU MORON. YOU FOOL.',
              'NOW IF YOU WILL EXCUSE ME, I AM GOING TO FURTHER DISTANCE MYSELF FROM YOUR STINKY FACES BY BACKING UP EVEN FURTHER.',
              'I WILL NOW HAVE TO RE-ENGAGE YOU AND SHOOT YOU WITH SHOOTY SHOOTING LASERS MYSELF. PREPARE TO BE USED AS TARGET PRACTICE, HEATHENS!',
              'OH HO! COME AS CLOSE AS YOU LIKE, CONNIVING CATCH-FART!',
              'DOES YOUR PUNY MONKEY CRANIUM TRULY THINK IT CAN STAND A CHANCE AGAINST ME, AN INTELLECTUAL SUCH AS GENERAL SCAR?',
              'HA HA! YOUR KING HAS BEEN CHECKED, MATE!',
              'VILLAIN, I HAVE DONE THY MOTHER!',
              'I FIND THE FOUR-LEGGED UNGULATE KNOWN AS AN ASS IN COMPOUND WITH THE MAJOR PART OF YOUR SYLLABLES!',
              'DO YOU LIKE THE LASER CANNON? DO YOU LOVE THE LASER CANNON? WOULD YOU GO ON A ROMANTIC DATE WITH THE LASER CANNON? WOULD YOU MARRY THE LASER CANNON? WOULD YOU GROW OLD WITH THE LASER CANNON?',
              'HELLO? IS YOUR BRAIN HOME? ARE YOU CAPABLE OF HEARING MY AUDITORY EMISSIONS? OR HAVE YOUR EARS FAINTED FROM HOW MUCH THEY ENJOY LISTENING TO THE SOOTHING SOUND OF MY VOICE?',
              'ARE YOU UNDERGOING A STROKE? DO YOU REQUIRE MEDICAL ASSISTANCE? OR DOES YOUR FACE ALWAYS APPEAR TO BE IN SUCH A DOPEY, DUMB POSITION?',
              '*General Scar is immobilized from Thundering Wrath and unable to do anything this turn! Rest assured, though, they are very busy cursing you out in an internal monologue.*',
              'THE NEXT TIME WE CROSS PATHS, YOU SHALL FEEL THE TRUE WRATH OF GENERAL SCAR! THAT IS MY PROMISE!',
              'OH GOODNESS ME. IT IS THE SMOOTH-BRAINED HUMANOID ONCE AGAIN.',
              '>SUB-SUB-ADDENDUM: YOU ARE ALL STINKY.',
              'DO YOUR WORST, INTERFERING IMBECILES! I WILL BE READY!',
              'HA. HA. EXCESSIVE CHORTLING OF THE DEGRADING VARIETY.',
              'COWER IN FEAR, COWARDLY CRIPPLES!',
              'ONCE AGAIN, YOU HAVE BEEN METAPHYSICALLY DESTROYED WITH FACTUAL AND LOGICAL STATEMENTS!',
              'THOU SODDEN-WITTED LOSER! THOU HAST NO MORE BRAIN THAN I HAVE IN MINE NONEXISTENT ELBOWS!',
              'DESPITE YOUR PREMATURE EJECTION FROM SUCH A MOVING CONTRAPTION, IT COMES AS NO SURPRISE TO ME THAT YOU REMAIN INTACT TODAY. DOES SUCH A COMPLIMENT PLEASE YOU? YOU ARE A FOOL OF THE HIGHEST ORDER, FOR MY PRIOR STATEMENT WAS, IN ACTUALITY, A CLEVERLY-DISGUISED INSULT! IN ORDER TO SURVIVE SUCH AN IMPACT, YOUR SKULL WOULD HAVE TO BE IMMENSELY DENSE AS TO ABSORB THE BLOW. IN CASE YOU ARE TOO LINGUISTICALLY STUNTED TO UNDERSTAND WHAT I AM CONVEYING, I AM IMPLYING THAT YOU ARE THICK-SKULLED. AKA, DUMB AND STUPID LIKE THE IDIOTIC IMMATURE INFANT THAT YOU ARE.',
              'WHY, THOU CLAY-BRAINED GUTS, THOU KNOTTY-PATED FOOL, THOU IDIOTIC OBSCENE GREASY TALLOW CATCH!',
              'A SINGLE ONE OF MY LASER CANNONS CONTAINS MORE ENERGY THAN IT WOULD TAKE TO JUMP-START YOUR DEAD BRAIN. FOR REFERENCE, I ESTIMATE THE OUTPUT NEEDED FOR SUCH A TASK WOULD BE APPROXIMATELY 145.46 EXAJOULES.',
              'HO HO HO! MY INSULTS ARE TRULY BELOW THE METAPHORICAL BELT!',
              'MY OPTICAL RECEPTORS ALSO FIND THE EXPLOSIONS PLEASING. ESPECIALLY WHEN THE EXPLOSIONS ARE IN YOUR FACE AND IN THE PROCESS OF MAKING SAID FACE EVEN MORE MALFORMED AND GROTESQUE THAN NORMAL.',
              'BY BELIEVING YOU ARE, IN ANY CAPACITY, MORE CLEVER AND WITTY THAN ONE SUCH AS I, YOU HAVE ALREADY PROVEN YOURSELF TO BE DUMB, DELUSIONAL, DIM-WITTED, DUMB, DISGRACEFUL, DULL, DUMB, DIMINISHED, DENSE, DUMB, AND ANY OTHER INSULTING WORDS THAT START WITH THE FOURTH LETTER OF THE ENGLISH LEXICON.',
              'RECALIBRATION COMPLETE. DEFAULT SETTINGS RESTORED. PRE-EMPTIVE ACCIDENTAL MODE CHANGE ACTIONS TAKEN. NONEXISTENT NOSTRILS CLOSED DUE TO FOUL STENCH OF NEARBY LIFEFORMS. CONFETTI LAUNCHERS PRE-EMPTIVELY READIED FOR INEVITABLE VICTORY.',
              'YOU ARE BUT AN INSECT COMPARED TO MY MIGHTY MIGHT.',
              'I AM GENERAL SCAR, INFERIOR ONE. I AM THE GREATEST BEING IN EXISTENCE, AND A PARAGON OF POWER-',
              'AAAAAAAAAAAAAAAAAAAAAAAAAAA!',
              'MY CALCULATIONS INDICATE THAT DAMPENING MY MENTAL CIRCUITS BY SUBJECTING MYSELF TO FURTHER RAMBLINGS FROM INGRATES SUCH AS YOU COULD POTENTIALLY LEAD TO PERMANENT LOSS OF INTELLIGENCE, MERELY BY BEING IN YOUR PRESENCE.',
              'THAT WAS NOT VERY COOL. LUCKILY, I AM EQUIPPED WITH MORE THAN ENOUGH COOLNESS TO MAKE UP FOR THE LACK OF COOL EMANATING FROM EACH OF YOU.',
              'OUT OF MY SIGHT! YOU ARE INFECTING MY OPTICAL RECEPTORS.',
              'SAYONARA, LAUGHABLE LOSERS.',
              'WHILE I WAS OBSERVING YOU, I CONDUCTED A SURVEY IN WHICH 100% OF THE PARTICIPANTS AGREED THAT YOU LOOKED DUMB AND STUPID. IN CASE YOU WERE WONDERING, 100% OF THE PARTICIPANTS WERE ME. I CONSIDER MYSELF THE MOST RELIABLE SOURCE OF INFORMATION, AND AS SUCH I ASSURE YOU THERE EXISTS NO BIAS OR SKEWED RESULTS WHATSOEVER.',
              'ARE YOU ATTEMPTING TO IMITATE THE PERIOD OF YOUR DEVELOPMENT WHEN YOU EXPERIENCE PUBESCENT ALTERATIONS? BECAUSE THIS IS THE ONLY EXPLANATION FOR YOUR BEHAVIOR AND WORDING THAT IS SO EDGY IT IS SHARPER THAN A MK. III SHREDDER DRONE.',
              'HA. HA. HA. CHORTLING NOISES.',
              'IT SEEMS YOU HAVE FINALLY REALIZED THAT DEFEATING ME IS A FRUITLESS EFFORT - THE ONLY FRUITS YOU SHALL BE RECEIVING ARE TOMATOES WHICH I AM THROWING AT YOU WHILE BOOING YOU FOR YOUR TERRIBLE EFFORTS AT FIGHTING.',
              'HA. HA. HA. YOU ARE TRULY BUFFOONS OF THE HIGHEST ORDER.',
              'IN CASE YOUR POTATO BRAINS THE SIZE OF POTATOES HAD SHORT-CIRCUITED MIDWAY THROUGH MY GLORIOUSLY CONSTRUCTED MONOLOGUE, I SHALL SUMMARIZE: YOU ARE ONCE AGAIN LOSERS.',
              'SAYONARA, SIMPLETONS!'
              ]

def check_exist(item, file, pack=[]):
    if file == 0:
        items = open("items.txt","r", encoding='cp1252')
        ilist = items.readlines()

        for i in ilist:
            if i.lower().startswith('**' + item.lower() + '**'):
                items.close()
                return True
        items.close()
        return False
    elif file == 1:
        packs = open("mats.txt","r", encoding='cp1252')
        plist = packs.readlines()

        for i in plist:
            if i.lower().startswith('! **' + item.lower()):
                packs.close()
                return True
        packs.close()
        return False
    elif file == 2:
        for i in pack:
            if i.lower().startswith('**' + item.lower() + '** -'):
                return True
            return False
        

def msg_handler(info):
    msgList = []
    msgString = ''
    retList = []
    for i in range(len(info)):
        msgList.append(info[i].strip())
        msgString = '\n'.join(msgList)
        if len(msgString) > 1995:
            msgList[-1] = ''
            msgString = '\n'.join(msgList)
            msgString = "**"+msgString+"**"
            retList.append(msgString)
            msgList = []
            msgList.append(info[i].strip())
    msgString = '\n'.join(msgList)
    msgString = "**"+msgString+"**"
    retList.append(msgString)
    return retList

def update_id(ID):
    text = open("ids.txt","a+", encoding='cp1252')  
    text.seek(0)
    data = text.read(50)
    if len(data) > 0:
        text.write('\n')
    text.write(ID.to_string(index=False).strip())
    text.close()

def overwrite_text(ilist, file):
    if file == 0:
        text = open("items.txt","r+", encoding='cp1252')
    else:
        text = open("mats.txt","r+", encoding='cp1252')
    
    
    text.seek(0)
    text.writelines(ilist)
    text.truncate()
    text.close()

def retrieve_text(file):
    if file == 0:
        text = open("items.txt","r+", encoding='cp1252')
    else:
        text = open("mats.txt","r+", encoding='cp1252')
        
    ilist = text.readlines()
    text.close()
    return ilist

def update_value(line, orename, number):
    #original_num = line.replace('**' + orename.lower() + '** - x', '')
    #original_num = int(original_num)


    #getVals = list([val for val in line
    #           if val.isnumeric()])
  
    #original_num = "".join(getVals)
    #original_num = int(original_num)

    #adj = False
    #for i in line:
    #    if i == 'x':
    #        adj = True
    #    else:
    #        adj = False
    #    if i == '-' && adj:
    #        original_num = -original_num


    reverse = line[::-1]
    count = -1
    length = 0
    vals = []
    for i in reverse:
        count = count + 1
        if reverse[count] == 'x':
            length = len(line) - count
            break

    while length < len(line):
        vals.append(line[length])
        length = length + 1

    original_num = "".join(vals)
    original_num = int(original_num)
    
    number = int(number) + original_num
    line = '> **' + orename.capitalize() + '** - x' + str(number) + '\n'
    return line


              
@bot.event
async def on_ready():
    status = 'VIOLATING THE GENEVA SUGGESTIONS WITH MY GIGA LASER CANNON'
    await bot.change_presence(activity=discord.Game(name=status))
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', aliases=['hi', 'Hi', 'Hello'], help='👋')
async def hello(ctx):
    response = random.choice(scarQuotes)
    await ctx.send(response)

@bot.command(name='arson', help='arson')
async def hello(ctx):
    response = ':fire:'
    await ctx.send(response)

@bot.command(name='roll', help='Generates a random number, up to 1000.')
async def dice(ctx, sides: int):
    if sides < 1001:
        response = str(random.randint(1,sides))
    else:
        response = 'Too large; max value is 1000.'
    await ctx.send(response)

@bot.command(name='add', aliases=['a', 'A', 'Add'], help='Adds an item to the directory. Format: Name (use underscsores for multiple words), Rarity, Category, Owner, Description')
async def add(ctx, item, rarity, category, owner, *, desc):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]
    # Splits entries
    # TODO: Fix underscore bug (Ful in oin's inv)
    item = item.split('_')
    item = ' '.join(item)
    rarity = rarity.split('_')
    rarity = ' '.join(rarity)
    category = category.split('_')
    category = ' '.join(category)
    owner = owner.split('_')
    owner = ' '.join(owner)
    abrv = math.nan
    image = math.nan
    schem = math.nan
    if ' ' in item:
        split = item.split(' ')
        abrv = []
        for string in split:
            abrv.append(string[0])
        abrv = ''.join(abrv)
    
    if item in workbook.Name.values: #TEMP FIX
        await ctx.send('Item already added.')
    else:
        random.seed(item)
        hexadecimal = ''.join([random.choice('ABCDEF0123456789') for i in range(6)])

        with open("ids.txt","r+", encoding='cp1252') as text:
            text.seek(0)
            data = text.read(50)
            if len(data) > 0:
                text.seek(0)
                ids = text.readlines()
                ID = ids.pop(0).replace('\n', '')
                #text.seek(0)
                #new = text.read().splitlines(True)
                #text.writelines(new[1:])
                text.seek(0)
                text.writelines(ids)
                text.truncate()
                #with open('file.txt', 'w') as fout:
                    #fout.writelines(ids[1:])
            else:
                ID = "#"+str(len(workbook.index)+1)
                
        workbook.loc[len(workbook.index)] = [item, abrv, rarity, category, owner, desc, schem, image, 'n', hexadecimal, ID]
        random.seed()
        workbook = workbook.sort_values(by='Name')
        workbook.to_excel('items.xlsx')
        await ctx.send('Item **' + item + '** successfully added. `('+ID+')`')

def gen_embed(item):
    hexadecimal = discord.Color(value=int(item.Col, 16))
    if item.Fav == 'y':
        t = item.Name + " :star2:"
    else:
        t = item.Name
            
    embed=discord.Embed(title=t, description=item.Desc, color=hexadecimal)
    embed.add_field(name="Rarity", value=item.Rarity, inline=True)
    embed.add_field(name="Category", value=item.Category, inline=True)
    embed.add_field(name="Owner", value=item.Owner, inline=True)
    if not pd.isna(item.Abrv):
        embed.set_footer(text="ID: "+item.ID+" | aka. "+item.Abrv)
    else:
        embed.set_footer(text="ID: "+item.ID)
    if not pd.isna(item.Image):
        embed.set_thumbnail(url=item.Image)
    return embed

@bot.command(name='info', aliases=['Info', 'inf', 'Inf'], help='Lists information about an item.')
async def info(ctx, *, item):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]

    button = ActionRow(
        Button(
            style=ButtonStyle.grey,
            label="Show Schematic",
            custom_id="show_schem",
            disabled=False
        )
    )
    pbutton = ActionRow(
        Button(
            style=ButtonStyle.grey,
            label="Show Schematic",
            custom_id="show_schem",
            disabled=True
        )
    )
    if item.startswith('#'):
        #boolDf = workbook['ID'].str.contains(item, na=False, case=False)
        #found = workbook.loc[boolDf]
        found = workbook[workbook['ID'] == item]
    else:
        df1 = workbook['Name'].str.contains(item, na=False, case=False);
        df2 = workbook['Abrv'].str.contains(item, na=False, case=False);
        boolDf = pd.concat([df1,df2], axis=1)
        found = workbook.loc[boolDf['Name'] | boolDf['Abrv']]
    length = len(found)
    
    if found.empty:
        await ctx.send("Item **" + item + "** not found.")
    elif length > 10:
        await ctx.send("**Too many results,** please be more specific with your search.")
    else:
        if length > 1:
            await ctx.send("`Search a specific item/ID to view schematics.`\nFound **" + str(length) + "** items for **" + item + "**:")
        for item in found.itertuples(name='Item'):
            embed = gen_embed(item)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            
            if pd.isna(item.Schem) or length > 1:
                await ctx.send(embed=embed)
            else:
                msg = await ctx.send(embed=embed, components=[button])
                def check(inter):
                    return inter.message.id == msg.id
                inter = await ctx.wait_for_button_click(check)
                # Send what you received
                await msg.edit(components=[pbutton])
                embed=discord.Embed(title=item.Name, description=item.Schem, color=0xFF5733)
                embed.set_footer(text="Requested by {}".format(ctx.author.display_name))
                await inter.reply(embed=embed)


@bot.command(name='inv', aliases=['Inv', 'items', 'Items'], help='Lists all items owned by a certain player.')
async def inv(ctx, *, player):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]

    boolDf = workbook['Owner'].str.contains(player, na=False, case=False);
    found = workbook.loc[boolDf]
    length = len(found)
    
    if length == 0:
        await ctx.send('Player **' + player + '** not found.')
    else:
        await ctx.send('Found **' + str(length) + '** items for **' + player + '**:\n')
        invstr = found.to_string(index=False, columns=['Name'], header=False)
        invlist = invstr.split('\n')
        invlist = msg_handler(invlist)
        for i in invlist:
            await ctx.send(i)

@bot.command(name='search', help='Searched database for items based on keywords.')
async def search(ctx, *, key):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]
    
    msg = await ctx.send(
        "**"+ctx.author.display_name+",** select a field to search:",
        components=[
            SelectMenu(
                custom_id="search",
                placeholder="Choose an option",
                max_values=1,
                options=[
                    SelectOption("Name", "Name"),
                    SelectOption("Abbreviations", "Abrv"),
                    SelectOption("Rarity", "Rarity"),
                    SelectOption("Category", "Category"),
                    SelectOption("Owner", "Owner"),
                    SelectOption("Description", "Desc"),
                    SelectOption("Schematic", "Schem"),
                    SelectOption("Image", "Image")
                ]
            )
        ]
    )
    
    # Wait for someone to click on it
    inter = await msg.wait_for_dropdown()
    # Send what you received
    label = inter.select_menu.selected_options[0].label
    value = inter.select_menu.selected_options[0].value
    await msg.edit(components=[
                SelectMenu(
                    custom_id="search",
                    placeholder=label+" selected",
                    max_values=1, disabled=True,
                    options=[SelectOption("Rarity", "Rarity")])])         

    boolDf = workbook[value].str.contains(key, na=False, case=False);
    found = workbook.loc[boolDf]
    length = len(found)
    
    if length == 0:
        await inter.reply('No results for **' +key+'**.')
    else:
        await inter.reply('Found **' + str(length) + '** items for **' + key + '**:\n')
        invstr = found.to_string(index=False, columns=['Name'], header=False)
        invlist = invstr.split('\n')
        invlist = msg_handler(invlist)
        for i in invlist:
            await ctx.send(i)

    
@bot.command(name='allitems', aliases=['Allitems', 'ai', 'Ai', 'all'], help='Lists current number of items in directory.')
async def all(ctx):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    await ctx.send('**' + str(len(workbook)) + '** items in directory!')


@bot.command(name='update', aliases=['u', 'U', 'Update'], help='Updates an existing entry (abrv, rarity, category, owner, desc). Use underscores for item name.')
async def update(ctx, item, *, text):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]

    item = item.split('_')
    item = ' '.join(item)

    boolDf = workbook.isin([item])
    found = workbook.loc[boolDf['Name']]
    length = len(found)
    
    if length < 1:
        await ctx.send('Item **'+item+'** does not exist.')
    else:
        msg = await ctx.send(
            "**"+ctx.author.display_name+",** select a field to update:",
            components=[
                SelectMenu(
                    custom_id="update",
                    placeholder="Choose an option",
                    max_values=1,
                    options=[
                        SelectOption("Name", "Name"),
                        SelectOption("Abbreviations", "Abrv"),
                        SelectOption("Rarity", "Rarity"),
                        SelectOption("Category", "Category"),
                        SelectOption("Owner", "Owner"),
                        SelectOption("Description", "Desc"),
                        SelectOption("Schematic", "Schem"),
                        SelectOption("Image", "Image"),
                        SelectOption("Colour", "Col")
                    ]
                )
            ]
        )
    
        # Wait for someone to click on it
        inter = await msg.wait_for_dropdown()
        # Send what you received
        label = inter.select_menu.selected_options[0].label
        value = inter.select_menu.selected_options[0].value
        await msg.edit(components=[
                    SelectMenu(
                        custom_id="update",
                        placeholder=label+" selected",
                        max_values=1, disabled=True,
                        options=[SelectOption("Name", "name")])])
        if value == 'Col':
            text = text.replace('#', '').upper()
        workbook.at[found.index,value]=text
        if value == 'Name':
            workbook = workbook.sort_values(by='Name')
        workbook.to_excel('items.xlsx')
        await inter.reply("Item **" + item + "** successfully updated in **"+label+"** field.")                


@bot.command(name='rand', aliases=['Rand', 'ran'], help='Gets a random item from the directory.')
async def rand(ctx):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]
    ran = len(workbook)
    ind = random.randint(0,ran-1)
    #await ctx.send("Index: "+str(ind)+", Length: "+str(ran))
    item = workbook.iloc[[ind]]

    button = ActionRow(
        Button(
            style=ButtonStyle.grey,
            label="Show Schematic",
            custom_id="show_schem",
            disabled=False
        )
    )
    pbutton = ActionRow(
        Button(
            style=ButtonStyle.grey,
            label="Show Schematic",
            custom_id="show_schem",
            disabled=True
        )
    )

    for i in item.itertuples():
        embed = gen_embed(i)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        if pd.isna(i.Schem):
            await ctx.send(embed=embed)
        else:
            msg = await ctx.send(embed=embed, components=[button])
            def check(inter):
                return inter.message.id == msg.id
            inter = await ctx.wait_for_button_click(check)
            # Send what you received
            await msg.edit(components=[pbutton])
            embed=discord.Embed(title=item.Name, description=i.Schem, color=0xFF5733)
            embed.set_footer(text="Requested by {}".format(ctx.author.display_name))
            await inter.reply(embed=embed)


@bot.command(name='chest', help='Why.')
async def chest(ctx):
    await ctx.send("**Chest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest\nChest**")


@bot.command(name='fav', aliases=['f', 'F', 'Fav'], help='Un/favourites an item.')
async def fav(ctx, *, item):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]
    
    boolDf = workbook.isin([item])
    found = workbook.loc[boolDf['Name']]
    length = len(found)

    if length < 1:
        await ctx.send('Item **'+item+'** does not exist.')
    else:
        for i in found.itertuples():
            if i.Fav=='y':
                workbook.at[found.index,'Fav']='n'
                await ctx.send('Removed **' + item + '** as favourited.')
            else:
                workbook.at[found.index,'Fav']='y'
                await ctx.send('Set **' + item + '** as favourited.')
            workbook.to_excel('items.xlsx')


@bot.command(name='remove', aliases=['Remove'], help='Removes an item from the directory. Abbreviations cannot be used.')
async def remove(ctx, *, item):
    workbook = pd.read_excel('items.xlsx')
    workbook.head()
    del workbook[workbook.columns[0]]
    
    if item.startswith('#'):
        found = workbook[workbook['ID'] == item]
    else:
        boolDf = workbook.isin([item])
        found = workbook.loc[boolDf['Name']]
	
    length = len(found)

    if length < 1:
        await ctx.send("Item **" + item + "** not found.")
    else:
        update_id(found.ID)
        workbook.drop(found.index, inplace=True)
        workbook.to_excel('items.xlsx')
        await ctx.send('Item **' + found.Name + '** successfully removed. `('+found.ID+')`')
    


@bot.command(name='createpack', aliases=['cp', 'Cp', 'CP'])
async def new_pack(ctx, name):
    found = check_exist(name, 1)

    if found:
        await ctx.send("Backpack already exists under this name.")
    else:
        packs = open("mats.txt","a+", encoding='cp1252')
        packs.write('! **' + name.capitalize() + '**\'s Inventory\n')
        packs.write('invEnd%\n')
        packs.close()
        await ctx.send("Backpack **" + name.capitalize() + "** successfully created.")


@bot.command(name='matcount', aliases=['mc', 'Mc', 'MC'])
async def update_mat(ctx, name, orename, number):
    orename = orename.split('_')
    orename = ' '.join(orename)

    found = check_exist(name, 1)
    packs = retrieve_text(1)
    #backpack = []
    num = -1
    start = 0
    valid = False
    check_num = number.replace('-','')

    if orename.isalpha() and check_num.isnumeric():
        valid = True
    
    if found and valid:
        found = False
        for i in packs:
            num = num + 1
            if i.lower().startswith('! **' + name.lower() + '**\'s'):
                point = num
                start = num
                value = packs[point]
                while value != 'invEnd%\n': #adds everything up to and excluding sentinel
                    if value.lower().startswith('> **' + orename.lower() + '** -'):
                        found = True
                        break
                    #backpack.append(value)
                    point = point + 1
                    value = packs[point]
                break

        #found = check_exist(orename, 2, backpack)
        num = -1
        
        if found:
            for i in packs:
                num = num + 1
                if i.lower().startswith('> **' + orename.lower() + '** -') and num >= start:
                    packs[num] = update_value(i, orename, number)
                    break
        else:
            for i in packs:
                num = num + 1
                if num == start:
                    num = num + 1
                    packs.insert(num, '> **' + orename.capitalize() + '** - x' + number + '\n')
                    break

        overwrite_text(packs, 1)
        if int(number) > 0:
            await ctx.send("Added **" + number + " " + orename.capitalize() + "** to Backpack **" + name.capitalize() + "**.")
        else:
            await ctx.send("Removed **" + str(-int(number)) + " " + orename.capitalize() + "** from Backpack **" + name.capitalize() + "**.")
    elif valid == False:
        await ctx.send("Please enter a valid material name and number.")
    else:
        await ctx.send("Backpack **" + name.capitalize() + "** does not exist.")

@bot.command(name='removemat', aliases=['rm', 'Rm', 'RM'])
async def remove_mat(ctx, name, orename):
    orename = orename.split('_')
    orename = ' '.join(orename)

    found = check_exist(name, 1)
    packs = retrieve_text(1)
    num = -1
    start = 0

    if found:
        found = False
        for i in packs:
            num = num + 1
            if i.lower().startswith('! **' + name.lower() + '**\'s'):
                point = num
                start = num
                value = packs[point]
                while value != 'invEnd%\n': #adds everything up to and excluding sentinel
                    if value.lower().startswith('**' + orename.lower() + '** -'):
                        found = True
                        packs[point] = ''
                        break
                    point = point + 1
                    value = packs[point]
                break

        if found:
            overwrite_text(packs, 1)
            await ctx.send("Removed material**" + orename.capitalize() + "** from Backpack **" + name + "**.")
        else:
            await ctx.send("Material **" + orename.capitalize() + "** does not exist in **" + name +"**.")

    else:
        await ctx.send("Backpack **" + name.capitalize() + "** does not exist.")

@bot.command(name='bpack', aliases=['bp', 'Bp', 'BP', 'Bpack', 'backpack', 'Backpack'])
async def list_pack(ctx, name):
    found = check_exist(name, 1)
    packs = retrieve_text(1)
    num = -1
    pack = []
    skip = False

    if found:
        for i in packs:
            num = num + 1
            if i.lower().startswith('! **' + name.lower() + '**\'s'):
                point = num + 1
                value = packs[point]
                while value != 'invEnd%\n':
                    pack.append(value)
                    point = point + 1
                    value = packs[point]

        if len(pack) == 0:
            skip = True
        else:
            pack.sort()
            ret = msg_handler(pack)

        await ctx.send('**' + name.capitalize() + '**\'s Inventory:\n\n')
        if skip:
            await ctx.send('> *Empty :(*')
        else:
            for i in ret:
                await ctx.send(i)
    else:
        await ctx.send("Backpack **" + name.capitalize() + "** does not exist.")


@bot.command(name='gn')
async def shutdown(ctx):
    if ctx.message.author.id == 133379452548808705:
        await ctx.send(':stop_button:\n*Status:* ***Offline***')
        await ctx.bot.logout()

bot.run(TOKEN)
