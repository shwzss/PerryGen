import discord
from discord.ext import commands
import random
import string
import asyncio
import re

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Add this line to include message content intent

bot = commands.Bot(command_prefix='!', intents=intents)

dns_servers = ['8.8.8.8', '1.1.1.1']

domain_mapping = {
    'steam': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'netflix': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'crunchyroll': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'psn': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'xbox': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'roblox': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'epic_games': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'amazon': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'ebay': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'telegram': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'tiktok': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'battle_net': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'google': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'spotify': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'twitch': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'kick': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'reddit': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'soundcloud': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'facebook': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'twitter': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'linkedin': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'pinterest': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'snapchat': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'whatsapp': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'vimeo': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'tumblr': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'flickr': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'dribbble': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'behance': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'medium': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'quora': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'yelp': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'bitcoin': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'gmail': 'gmail.com',
    'rottentomatoes': 'gmail.com, yahoo.com, hotmail.com, aol.com',
    'paypal': 'gmail.com, yahoo.com, hotmail.com, aol.com'
}

def generate_random_email(service=None, domain=None):
    if domain:
        if service in domain_mapping:
            domain = random.choice(domain_mapping[service].split(', '))
        else:
            domain = domain
    else:
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com'])
    
    return f"{random.choice(string.ascii_lowercase)}{random.randint(1, 999)}@{domain}"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def generate_random_phone_number():
    return f"+1{random.randint(1000000000, 9999999999)}"

def is_valid_email(email):
    # Simple regex for validating an email
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

async def create_account_task(service=None, domain=None):
    email = generate_random_email(service, domain)
    password = generate_random_password()
    phone_number = generate_random_phone_number()

    if not is_valid_email(email):
        email = None

    print(f"Creating account with email: {email}")
    print(f"Password: {password}")
    print(f"Phone number: {phone_number}")

    await bot.wait_until_ready()
    return email, password, phone_number

async def create_channel_task(guild, name, category):
    channel = await guild.create_text_channel(name, category=category)
    print(f"Channel created: {channel.mention}")
    return channel

def generate_credit_card():
    number = []
    for _ in range(15):
        number.append(random.randint(0, 9))
    return ''.join(str(x) for x in number)

def generate_expiration_date():
    month = random.randint(1, 12)
    year = random.randint(2023, 2030)
    return f"{month}/{year}"

def generate_cvv():
    return str(random.randint(100, 999))

def validate_credit_card(number):
    sum = 0
    reverse_digits = number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        sum += n
    return sum % 10 == 0

def validate_expiration_date(date):
    try:
        month, year = map(int, date.split('/'))
        if month < 1 or month > 12:
            return False
        if year < 2023 or year > 2030:
            return False
        return True
    except ValueError:
        return False

def generate_service_code(service, length=None):
    if service == 'psn':
        return ''.join(random.choices(string.digits, k=12))
    elif service == 'xbox':
        return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5))
    elif service == 'fortnite':
        if length == 12:
            return ''.join(random.choices(string.digits, k=12))
        elif length == 16:
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        elif length == 25:
            return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5))
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

def check_service_code(service, code):
    # Simulated code checking logic
    valid_codes = {
        'psn': 'PSN1234567890ABCD',
        'xbox': 'XBOX1234567890ABCD',
        'fortnite': 'FORTNITE123456AB'
    }
    return code == valid_codes.get(service.lower(), '')

def estimate_balance(card_number):
    # Simulated balance estimation based on the first digit of the card number (MII)
    mii = card_number[0]
    balance_mapping = {
        '1': random.uniform(1, 5000),
        '2': random.uniform(1, 5000),
        '3': random.uniform(1, 5000),
        '4': random.uniform(1, 5000),
        '5': random.uniform(1, 5000),
        '6': random.uniform(1, 5000),
        '7': random.uniform(1, 5000),
        '8': random.uniform(1, 5000),
        '9': random.uniform(1, 5000),
        '0': random.uniform(1, 5000)
    }
    return round(balance_mapping.get(mii, 0.00), 2)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name='setup_server')
@commands.is_owner()
async def setup_server(ctx):
    print("setup_server command called")
    guild = ctx.guild

    # Create roles
    roles = ['Free', 'Basic', 'Super', 'Owner', 'Extended Stock', 'Mod', 'Admin', 'Support', 'Ticket Support', 'Head Support', 'Head Mod', 'Head Admin']
    for role in roles:
        print(f"Creating role: {role}")
        await guild.create_role(name=role)
    
    # Create categories and channels
    categories = {
        'Welcome': ['welcome'],
        'Tickets': ['tickets'],
        'Main': ['rules', 'announcements', 'general-chat', 'mod-chat'],
        'Legit': ['vouches', 'legit'],
        'Generator': ['free', 'basic', 'super'],
        'Free': ['giveaways', 'drops']
    }

    for category_name, channels in categories.items():
        category = await guild.create_category(category_name)
        for channel in channels:
            await create_channel_task(guild, channel, category)
    
    await ctx.send("Server setup complete with roles and channels!")

@bot.command(name='create_channel')
async def create_channel_command(ctx, *, name):
    try:
        channel = await create_channel_task(ctx.guild, name, None)
        await ctx.send(f"Channel created: {channel.mention}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(name='generate_account')
async def generate_account_command(ctx, service: str, domain: str, count: int = 1):
    role_limits = {
        'Free': 10,
        'Basic': 50,
        'Super': 100,
        'Extended Stock': 500,
        'Owner': 10000
    }

    user_roles = [role.name for role in ctx.author.roles]
    max_count = 0

    for role, limit in role_limits.items():
        if role in user_roles:
            max_count = limit
            break

    if max_count == 0:
        await ctx.send("You do not have permission to use this command.")
        return

    if count > max_count:
        await ctx.send(f"You can only generate up to {max_count} accounts.")
        return

    if domain not in ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com']:
        await ctx.send("Invalid domain. Please choose from: gmail.com, yahoo.com, hotmail.com, aol.com.")
        return

    try:
        accounts = []
        for _ in range(count):
            email, password, phone_number = await create_account_task(service, domain)
            if email:
                accounts.append(f"Email: {email}, Password: {password}")
            else:
                accounts.append(f"Phone number: {phone_number}, Password: {password}")
        
        tier = 'Super' if 'Super' in user_roles else 'Basic'
        channel_name = ctx.channel.name
        await ctx.send(f"Generated {tier} account(s) for {service} in the {channel_name} channel:\n" + "\n".join(accounts))
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(name='generate_credit_card')
async def generate_credit_card_command(ctx):
    try:
        number = generate_credit_card()
        expiration_date = generate_expiration_date()
        cvv = generate_cvv()
        balance = estimate_balance(number)
        await ctx.send(f"**Credit Card Number:** `{number}`\n**Expiration Date:** `{expiration_date}`\n**CVV:** `{cvv}`\n**Estimated Balance:** `${balance}`")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(name='validate_credit_card')
async def validate_credit_card_command(ctx, number: str, expiration_date: str, cvv: str):
    """Validates a credit card."""
    try:
        if validate_credit_card(number) and validate_expiration_date(expiration_date):
            await ctx.send("Credit card is valid!")
        else:
            await ctx.send("Credit card is not valid.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(name='generate_service_code')
async def generate_service_code_command(ctx, service: str, length: int = None):
    """Generates a service code (Super role required)."""
    if 'Super' in [role.name for role in ctx.author.roles]:
        try:
            code = generate_service_code(service, length)
            await ctx.send(f"**Generated code for {service}:** `{code}`")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command(name='check_service_code')
async def check_service_code_command(ctx, service: str, code: str):
    """Checks if a service code is valid (Super role required)."""
    if 'Super' in [role.name for role in ctx.author.roles]:
        try:
            if check_service_code(service, code):
                await ctx.send(f"The code for {service} is valid!")
            else:
                await ctx.send(f"The code for {service} is not valid.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command(name='cmds')
async def cmds_command(ctx):
    commands_list = """
    **Commands:**
    ```
    !setup_server - Sets up the server with roles and channels.
    !create_channel <name> - Creates a new text channel.
    !generate_account <service> <domain> [count] - Generates account(s) for the specified service and domain (Free: 10, Basic: 50, Super: 100, Extended Stock: 500, Owner: 10000).
    !generate_credit_card - Generates a random credit card.
    !validate_credit_card <number> <expiration_date> <cvv> - Validates a credit card.
    !generate_service_code <service> [length] - Generates a service code (Super role required).
    !check_service_code <service> <code> - Checks if a service code is valid (Super role required).
    !cmds - Shows this help message.
    !stock - Shows the stock.
    ```
    """
    await ctx.send(commands_list)

@bot.command(name='stock')
async def stock_command(ctx):
    stock_list = """
    **Available services:**
    ```
    - steam
    - discord
    - netflix
    - crunchyroll
    - psn
    - xbox
    - roblox
    - epic_games
    - amazon
    - ebay
    - telegram
    - tiktok
    - battle_net
    - google
    - spotify
    - twitch
    - kick
    - reddit
    - soundcloud
    - facebook
    - twitter
    - linkedin
    - pinterest
    - snapchat
    - whatsapp
    - vimeo
    - tumblr
    - flickr
    - dribbble
    - behance
    - medium
    - quora
    - yelp
    - tripadvisor
    - imdb
    - rottentomatoes
    - paypal
    ```
    """
    await ctx.send(stock_list)

bot.run('YOUR_BOT_TOKEN')

# Replace 'YOUR_BOT_TOKEN' with your bot token.