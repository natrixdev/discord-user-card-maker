import discord
import tkinter as tk
from io import BytesIO

# Replace this with your Discord bot token
TOKEN = "your_discord_bot_token"

client = discord.Client()

# Create a Tkinter window
window = tk.Tk()
window.configure(bg="black")

# Create Tkinter labels
avatar_label = tk.Label(window, bg="black")
name_label = tk.Label(window, fg="white", bg="black", font=("Arial", 20))
id_label = tk.Label(window, fg="white", bg="black", font=("Arial", 16))
created_at_label = tk.Label(window, fg="white", bg="black", font=("Arial", 16))
badge_label = tk.Label(window, fg="white", bg="black", font=("Arial", 16))
status_label = tk.Label(window, fg="white", bg="black", font=("Arial", 16))

# Function to update the profile card
def update_profile_card(user):
    # Load the user's avatar image
    avatar_url = user.avatar_url_as(format="png")
    avatar_data = BytesIO(avatar_url.read())
    avatar_image = tk.PhotoImage(data=avatar_data.getvalue())
    
    # Update the user's avatar in the window
    avatar_label.configure(image=avatar_image)
    avatar_label.image = avatar_image
    
    # Update the user's name and discriminator in the window
    name_label.configure(text=f"{user.name}#{user.discriminator}")
    
    # Update the user's ID and account creation date in the window
    id_label.configure(text=f"ID: {user.id}")
    created_at_label.configure(text=f"Created At: {user.created_at}")
    
    # Update the user's badges in the window
    badge_text = "Badges: "
    for badge in user.public_flags.all():
        badge_text += str(badge) + " "
    badge_label.configure(text=badge_text)
    
    # Update the user's status in the window
    status_label.configure(text=f"Status: {user.status}")
    
    # Update the window layout
    window.update_idletasks()

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
        
        # Update the profile card for the user
        update_profile_card(user)

# Set the layout for the Tkinter labels
avatar_label.pack(side="left", padx=10, pady=10)
name_label.pack(padx=10, pady=10)
id_label.pack(padx=10, pady=10)
created_at_label.pack(padx=10, pady=10)
badge_label.pack(padx=10, pady=10)
status_label.pack(padx=10, pady=10)

# Start the bot
client.run(TOKEN)
