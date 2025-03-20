import discord
from discord.ext import commands
from discord import app_commands
import random
import string
import asyncio
import re

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Role limits for generation commands
role_limits = {
    'Free': 10,
    'Basic': 50,
    'Super': 100,
    'Extended Stock': 500,
    'Owner': 10000
}

# Domain mapping for services
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

# Service stock
service_stock = {
    'steam': 9999999999,
    'netflix': 9999999999,
    'crunchyroll': 9999999999,
    'psn': 9999999999,
    'xbox': 9999999999,
    'roblox': 9999999999,
    'epic_games': 9999999999,
    'amazon': 9999999999,
    'ebay': 9999999999,
    'telegram': 9999999999,
    'tiktok': 9999999999,
    'battle_net': 9999999999,
    'google': 9999999999,
    'spotify': 9999999999,
    'twitch': 9999999999,
    'kick': 9999999999,
    'reddit': 9999999999,
    'soundcloud': 9999999999,
    'facebook': 9999999999,
    'twitter': 9999999999,
    'linkedin': 9999999999,
    'pinterest': 9999999999,
    'snapchat': 9999999999,
    'whatsapp': 9999999999,
    'vimeo': 9999999999,
    'tumblr': 9999999999,
    'flickr':9999999999,
    'dribbble': 9999999999,
    'behance': 9999999999,
    'medium': 9999999999,
    'quora': 9999999999,
    'yelp': 9999999999,
    'gmail': 9999999999,
    'rottentomatoes': 9999999999,
    'paypal': 9999999999
}

# Predefined valid service codes (for demonstration purposes)
valid_service_codes = {
    'psn': ['A1B2C3D4E5F6', 'G7H8I9J0K1L2'],
    'xbox': ['A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5'],
    'epic_games': ['A1B2C3D4E5F6G7H8']
}

# Predefined valid accounts (for demonstration purposes)
valid_accounts = {
    'steam': [{'email': 'test1@gmail.com', 'password': 'password123'}],
    'netflix': [{'email': 'test2@yahoo.com', 'password': 'password456'}]
}

# Helper functions
def generate_credit_card():
    """Generate a random 16-digit credit card number starting with 3, 4, 5, or 6."""
    first_digit = random.choice(['3', '4', '5', '6'])
    remaining_digits = ''.join(random.choices(string.digits, k=15))
    return first_digit + remaining_digits

def generate_cvv():
    """Generate a random 3-digit CVV."""
    return ''.join(random.choices(string.digits, k=3))

def generate_expiration_date():
    """Generate a random expiration date in the format MM/YYYY."""
    month = random.randint(1, 12)
    year = random.randint(2023, 2030)
    return f"{month:02d}/{year}"

def get_user_limit(member: discord.Member):
    for role_name, limit in role_limits.items():
        if discord.utils.get(member.roles, name=role_name):
            return limit
    return 0  # Default to 0 if no role matches

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

# Slash command to generate an account
@bot.tree.command(name="generate_account", description="Generate an account for a specific service and domain.")
@app_commands.describe(service="The service to generate an account for.", domain="The domain to use.")
async def generate_account(interaction: discord.Interaction, service: str, domain: str):
    user_limit = get_user_limit(interaction.user)
    if user_limit == 0:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        return

    if service not in domain_mapping:
        await interaction.response.send_message(f"Invalid service. Available services: {', '.join(domain_mapping.keys())}", ephemeral=True)
        return

    if domain not in domain_mapping[service].split(', '):
        await interaction.response.send_message(f"Invalid domain for {service}. Available domains: {domain_mapping[service]}", ephemeral=True)
        return

    email = generate_random_email(service, domain)
    password = generate_random_password()
    await interaction.response.send_message(f"Generated account:\nEmail: `{email}`\nPassword: `{password}`")

# Slash command to generate credit cards
@bot.tree.command(name="generate_credit_card", description="Generate random credit cards.")
@app_commands.describe(amount="The number of credit cards to generate.")
async def generate_credit_card_command(interaction: discord.Interaction, amount: int = 1):
    user_limit = get_user_limit(interaction.user)
    if user_limit == 0:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        return

    if amount > user_limit:
        await interaction.response.send_message(
            f"You can only generate up to {user_limit} credit cards based on your role.",
            ephemeral=True
        )
        return

    # Defer the response to allow more time for processing
    await interaction.response.defer()

    # Generate the requested number of credit cards
    cards = [
        {
            "number": generate_credit_card(),
            "expiration_date": generate_expiration_date(),
            "cvv": generate_cvv()
        }
        for _ in range(amount)
    ]

    # Format the response
    card_details = "\n".join(
        f"**Card {i+1}:**\n"
        f"**Number:** `{card['number']}`\n"
        f"**Expiration Date:** `{card['expiration_date']}`\n"
        f"**CVV:** `{card['cvv']}`"
        for i, card in enumerate(cards)
    )

    # Send the response
    if len(card_details) > 2000:  # Discord message limit is 2000 characters
        await interaction.followup.send("The generated credit cards are too many to display in one message. Please try generating fewer cards.")
    else:
        await interaction.followup.send(f"Generated {amount} credit card(s):\n\n{card_details}")

# Slash command to validate a credit card
@bot.tree.command(name="validate_credit_card", description="Validate a credit card.")
@app_commands.describe(number="The credit card number.", expiration_date="The expiration date (MM/YYYY).", cvv="The CVV.")
async def validate_credit_card(interaction: discord.Interaction, number: str, expiration_date: str, cvv: str):
    if not number.isdigit() or len(number) != 16:
        await interaction.response.send_message("Invalid credit card number. It must be 16 digits.")
        return

    if not re.match(r"^(0[1-9]|1[0-2])\/\d{4}$", expiration_date):
        await interaction.response.send_message("Invalid expiration date. Format must be MM/YYYY.")
        return

    if not cvv.isdigit() or len(cvv) != 3:
        await interaction.response.send_message("Invalid CVV. It must be 3 digits.")
        return

    await interaction.response.send_message("Credit card is valid!")

# Generate the requested number of service codes
    code_length = service_code_lengths[service]
    codes = [
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))
        for _ in range(amount)
    ]
    await interaction.response.send_message(
        f"Generated {amount} code(s) for **{service.capitalize()}**:\n" + "\n".join(f"`{code}`" for code in codes)
    )

# Slash command to generate service codes
@bot.tree.command(name="generate_service_code", description="Generate service codes for a specific service.")
@app_commands.describe(service="The service to generate codes for.", amount="The number of codes to generate.")
async def generate_service_code(interaction: discord.Interaction, service: str, amount: int = 1):
    user_limit = get_user_limit(interaction.user)
    if user_limit == 0:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        return

    # Define specific code lengths for services
    service_code_lengths = {
        'psn': 12,
        'xbox': 25,
        'epic_games': 16
    }

    if service not in service_code_lengths:
        await interaction.response.send_message(
            f"Invalid service. Available services: {', '.join(service_code_lengths.keys())}",
            ephemeral=True
        )
        return

    if amount > user_limit:
        await interaction.response.send_message(
            f"You can only generate up to {user_limit} codes based on your role.",
            ephemeral=True
        )
        return

    # Generate the requested number of service codes
    code_length = service_code_lengths[service]
    codes = [
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))
        for _ in range(amount)
    ]
    await interaction.response.send_message(
        f"Generated {amount} code(s) for **{service.capitalize()}**:\n" + "\n".join(f"`{code}`" for code in codes)
    )

# Slash command to check a service code
@bot.tree.command(name="check_service_code", description="Check if a service code is valid.")
@app_commands.describe(service="The service to check the code for.", code="The service code to check.")
async def check_service_code(interaction: discord.Interaction, service: str, code: str):
    if service not in valid_service_codes:
        await interaction.response.send_message(
            f"Invalid service. Available services: {', '.join(valid_service_codes.keys())}",
            ephemeral=True
        )
        return

    if code in valid_service_codes[service]:
        await interaction.response.send_message(f"The code `{code}` for **{service.capitalize()}** is valid!")
    else:
        await interaction.response.send_message(f"The code `{code}` for **{service.capitalize()}** is not valid.")

# Slash command to check an account
@bot.tree.command(name="check_account", description="Check if an account is valid.")
@app_commands.describe(service="The service to check the account for.", email="The email of the account.", password="The password of the account.")
async def check_account(interaction: discord.Interaction, service: str, email: str, password: str):
    if service not in valid_accounts:
        await interaction.response.send_message(
            f"Invalid service. Available services: {', '.join(valid_accounts.keys())}",
            ephemeral=True
        )
        return

    # Check if the account exists in the valid accounts list
    for account in valid_accounts[service]:
        if account['email'] == email and account['password'] == password:
            await interaction.response.send_message(f"The account `{email}` for **{service.capitalize()}** is valid!")
            return

    await interaction.response.send_message(f"The account `{email}` for **{service.capitalize()}** is not valid.")

# Slash command to show all commands
@bot.tree.command(name="show_commands", description="Show all available commands.")
async def show_commands(interaction: discord.Interaction):
    commands_list = [
        "/generate_account - Generate an account for a specific service and domain.",
        "/generate_credit_card - Generate a random credit card.",
        "/validate_credit_card - Validate a credit card.",
        "/generate_service_code - Generate a service code for a specific service.",
        "/check_service_code - Check if a service code is valid.",
        "/check_account - Check if an account is valid.",
        "/setup_server - Set up the server with categories and channels for the bot.",
        "/show_commands - Show all available commands.",
        "/show_stock - Show the stock for all services."
    ]
    await interaction.response.send_message("Available commands:\n" + "\n".join(commands_list))

# Slash command to show stock
@bot.tree.command(name="show_stock", description="Show the stock for all available services.")
async def show_stock(interaction: discord.Interaction):
    if not service_stock:
        await interaction.response.send_message("No services are currently available.", ephemeral=True)
        return

    stock_list = [f"**{service.capitalize()}**: {stock}" for service, stock in service_stock.items()]
    await interaction.response.send_message("**Service Stock:**\n" + "\n".join(stock_list))

# Slash command to set up the server
@bot.tree.command(name="setup_server", description="Set up the server with categories and channels for the bot.")
async def setup_server(interaction: discord.Interaction):
    guild = interaction.guild
    if not guild:
        await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
        return

    # Create categories and channels
    categories = ['Free', 'Basic', 'Super']
    for category_name in categories:
        category = discord.utils.get(guild.categories, name=category_name)
        if not category:
            category = await guild.create_category(category_name)
            # Create a text channel in the category
        channel_name = f"{category_name.lower()}-channel"
        if not discord.utils.get(category.channels, name=channel_name):
            await guild.create_text_channel(channel_name, category=category)
        
    await interaction.response.send_message("Server setup complete!")
        
# Event to sync slash commands
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
        print(f"{bot.user} is connected to Discord!")
    except Exception as e:
                print(f"Failed to sync commands: {e}")

# Run the bot
bot.run('YOUR_BOT_TOKEN')

# Replace YOUR_BOT_TOKEN with your bot token
