from telethon import TelegramClient
import time

# Bhai, yeh tera VIP pass – apne credentials daal, nahi toh gate band! 😏
api_id = 'YOUR_API_ID_HERE'  # Yeh nahi daala toh bhai ka swag waste hai! 😎
api_hash = 'YOUR_API_HASH_HERE'  # Secret masala, chhupa ke rakhna! 🌶️
phone = 'YOUR_PHONE_NUMBER_HERE'  # +91 wala number daal, warna bhool ja maza! 📱

# Channel IDs – apne hisaab se badal dena, bhai log! 🎯
SOURCE_CHANNEL = -100  # /UnUpload – yahan se lootenge posts! 💰
DESTINATION_CHANNEL = -100  # /Work Place – yahan daalenge polished maal! 🔥

# Bot ka gang – yeh teen bhai log kaam karenge! 🤖
BOT1 = "@Link"  # Link ka makeover king! 💅
BOT2 = "@LinkShotner"  # Short aur sweet banayega! ✂️
BOT3 = "@Logo"  # Logo daal ke shaan badhayega! 🌟

# Telegram ka darwaza kholte hain, bhai ka style shuru! 🚪
client = TelegramClient('session', api_id, api_hash)

async def get_posts_from_channel(channel_id):
    # Bhai, source se posts lootne ka waqt hai! 🏃‍♂️
    print(f"Bhai log, {channel_id} se posts loot rahe hain – ekdum filmy style mein!")
    messages = await client.get_messages(channel_id, limit=100)  # 100 posts ek baar mein, badal sakte ho!
    return messages

async def forward_and_get_response(from_entity, to_entity, message):
    # Post ko forward karo, bhai ka swag dikhao! 😎
    print(f"Forward kar raha hoon {to_entity} ko – kaam shuru!")
    await client.forward_messages(to_entity, message)
    time.sleep(5)  # Thodi si thandi, bot ko saans lene do! 😴
    # Bot ka jawab loot lo, latest wala! 🔥
    responses = await client.get_messages(to_entity, limit=1)
    if responses:
        print(f"{to_entity} ne jawab diya – ekdum mast!")
        return responses[0]
    print(f"Arre, {to_entity} ne kuch nahi bola? Chhodo!")
    return None

async def main():
    # Party shuru, login ka time hai, bhai log! 🎉
    await client.start(phone=phone)
    print("Bhai ka client shuru ho gaya! Telegram ke jungle mein swagat hai! 😎")
    
    post_count = 0  # Kitne posts polish hue, ginenge! 📊

    while True:
        print("\nNaya round shuru, bhai log – tayyar raho! 🔥")
        posts = await get_posts_from_channel(SOURCE_CHANNEL)
        
        if not posts:
            print("Arre, /UnUpload mein kuch nahi mila? Thodi der thandi lete hain!")
            time.sleep(60)  # 1 minute ka break, chill karo! 😴
            continue
        
        for post in posts:
            try:
                print(f"Post ID: {post.id} pe kaam shuru – dekho bhai ka jadoo!")
                
                # Step 1: Bot 1 ko bhejo – link ka makeover! 💅
                bot1_response = await forward_and_get_response(SOURCE_CHANNEL, BOT1, post)
                if not bot1_response:
                    print(f"{BOT1} ne nakre dikhaye, koi response nahi! Agla try karte hain!")
                    continue
                
                # Step 2: Bot 2 ko bhejo – link ko chhota karo! ✂️
                bot2_response = await forward_and_get_response(BOT1, BOT2, bot1_response)
                if not bot2_response:
                    print(f"{BOT2} ne dhoka diya, koi jawab nahi! Chhodo, agla!")
                    continue
                
                # Step 3: Bot 3 ko bhejo – logo daal ke shaan badhao! 🌟
                bot3_response = await forward_and_get_response(BOT2, BOT3, bot2_response)
                if not bot3_response:
                    print(f"{BOT3} ne time waste kiya, koi response nahi! Next!")
                    continue
                
                # Step 4: Destination pe polished maal daal do! 🔥
                await client.forward_messages(DESTINATION_CHANNEL, bot3_response, from_peer=BOT3)
                print(f"Post ID {post.id} polish ho gaya – /Work Place pe dhamaka! 🎉")
                post_count += 1
                
                # Thodi si thandi – ban se bacho, bhai! 😴
                time.sleep(2)  # 2 seconds ka break har post ke baad!
                
                # 100 posts pe bada break – safety first! 💪
                if post_count % 100 == 0:
                    print(f"{post_count} posts ho gaye, bhai! 5 minute ka break – ban se bacho!")
                    time.sleep(300)  # 5 minute ka chill time!
                
            except Exception as e:
                print(f"Post ID {post.id} mein gadbad – {e}! Thodi der thandi, phir try!")
                time.sleep(2)  # Error ke baad chhota break!
                continue
        
        print("Round khatam, bhai log! Thodi der chill karte hain!")
        time.sleep(60)  # 1 minute ka break har round ke baad!

if __name__ == "__main__":
    print("Bhai ka AutoWorker shuru – Ctrl+C se rok sakte ho! @sup_toon_1 ka swag! 🔥")
    try:
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Arre bhai, tune rok diya? Thik hai, milte hain @sup_toon_1 pe! 😎")
