import discord
from discord import app_commands
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyOAuth

DISCORD_TOKEN = 'MTQ4Mzg5MjU4ODAxNTY0ODc5OA.G14ZEz.X4NZxDAPpA9uGXE94klMbrJEZgw5c2cA0U7LpQ'
SPOTIFY_ID = 'ebb3f25bac424f5e9e7b96906ef50f22'
SPOTIFY_SECRET = '47e5d322f5284109882ee6639a9b91ad'
REDIRECT_URI = 'https://example.com/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-public user-library-read"
))

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Slash komandas sinhronizētas!")

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Bots {bot.user} ir Online un Slash komandas ir gatavas!')

@bot.tree.command(name="mekle", description="Atrod dziesmas saiti Spotify")
@app_commands.describe(nosaukums="Ieraksti dziesmas nosaukumu")
async def mekle(interaction: discord.Interaction, nosaukums: str):
    results = sp.search(q=nosaukums, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        await interaction.response.send_message(f"🎵 **{track['name']}** - {track['artists'][0]['name']}\n{track['external_urls']['spotify']}")
    else:
        await interaction.response.send_message("Normālāku dziesmu atrodi", ephemeral=True)

@bot.tree.command(name="taisi", description="Izveido automātisku playlist")
@app_commands.describe(nosaukums="Kā sauksim tavu jauno playlist?")
async def taisi(interaction: discord.Interaction, nosaukums: str):
    await interaction.response.send_message(f"Gatavoju playlist: **{nosaukums}**...", ephemeral=True)
    
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, nosaukums, public=True)
    
    search_results = sp.search(q=nosaukums, limit=5, type='track')
    track_uris = [track['uri'] for track in search_results['tracks']['items']]
    
    if track_uris:
        sp.playlist_add_items(playlist['id'], track_uris)
        await interaction.followup.send(f"Gatavs! Re kur tava plejliste: {playlist['external_urls']['spotify']}")
    else:
        await interaction.followup.send("Neatradu dziesmas, ko pievienot.")

bot.run(DISCORD_TOKEN)