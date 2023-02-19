import discord
import tkinter as tk
from io import BytesIO

# Replace this with your Discord bot token
TOKEN = "your_discord_bot_token"

client = discord.Client()

# Function to generate the profile card
def generate_profile_card(user):
    # Create a new Tkinter window
    window = tk.Tk()
    window.title(f"{user.name}#{user.discriminator}")
    window.configure(bg="black")

    # Load the user's avatar image
    avatar_url = user.avatar_url_as(format="png")
    avatar_data = BytesIO(avatar_url.read())
    avatar_image = tk.PhotoImage(data=avatar_data.getvalue())
    
    # Add the user's avatar to the window
    avatar_label = tk.Label(window, image=avatar_image)
    avatar_label.pack(side="left", padx=10, pady=10)
    
    # Add the user's name and discriminator to the window
    name_label = tk.Label(window, text=f"{user.name}#{user.discriminator}", fg="white", bg="black", font=("Arial", 20))
    name_label.pack(padx=10, pady=10)
    
    # Add the user's ID and account creation date to the window
    id_label = tk.Label(window, text=f"ID: {user.id}", fg="white", bg="black", font=("Arial", 16))
    id_label.pack(padx=10, pady=10)
    created_at_label = tk.Label(window, text=f"Created At: {user.created_at}", fg="white", bg="black", font=("Arial", 16))
    created_at_label.pack(padx=10, pady=10)
    
    # Add the user's badges to the window
    badge_text = "Badges: "
    for badge in user.public_flags.all():
        badge_text += str(badge) + " "
    badge_label = tk.Label(window, text=badge_text, fg="white", bg="black", font=("Arial", 16))
    badge_label.pack(padx=10, pady=10)
    
    # Add the user's status to the window
    status_text = f"Status: {user.status}"
    status_label = tk.Label(window, text=status_text, fg="white", bg="black", font=("Arial", 16))
    status_label.pack(padx=10, pady=10)
    
    # Run the Tkinter window
    window.mainloop()

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message contains a Discord ID
    if message.content.startswith("!profile"):
        # Extract the ID from the message
        user_id = message.content.split(" ")[1]
        
        # Retrieve the user object from the ID
        user = await client.fetch_user(user_id)
        
        # Generate the profile card for the user
        generate_profile_card(user)

# Start the bot
client.run(TOKEN)
