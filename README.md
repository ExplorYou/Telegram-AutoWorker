# Telegram AutoWorker 🤖✨

Arre bhai log, taiyar ho jao ekdum *filmy automation* ke liye! Yeh hai **Telegram AutoWorker**, banaya hai tere bhai ne – @sup_toon_1 ka asli baadshah! 😎 Yeh script ek channel se posts uthata hai, teen bots ke zariye unko polish karta hai, aur doosre channel pe daal deta hai – sab kuch apne aap, koi mehnat nahi! 💪

> **Disclaimer**: Yeh mazaa aur kaam ke liye hai, bhai. Copyright ka hungama mat karna, nahi toh @CopyRightConte pe chillana padega! 😂

---

## Yeh Kya Jadoo Hai? 🪄
Yeh script ek *automation ka dabangg* hai jo:
- **Source Channel** se posts fetch karta hai (`/UnUpload`).
- **Bot 1** (`@LinkConvertTerabot`) se link convert karta hai.
- **Bot 2** (`@TeraboxLinkshortnerbot`) se link short karta hai.
- **Bot 3** (`@MovieAnimeHub_Bot`) se logo add karta hai.
- Aur phir **Destination Channel** (`/Work Place`) pe polished post daal deta hai!

Ek baar start karo, aur baith ke maza lo – kaam apne aap hota rahega! 😏

---

## Features (Bhai Ki Shaan) 🌟
- 🚀 **Full Automation**: Post fetch se lekar final posting tak – sab apne aap!
- 🤖 **Bot Chain**: Teen bots ek saath kaam karte hain – link convert, shorten, aur logo add!
- ⏰ **Smart Delays**: Ban se bachne ke liye delays – 2 sec per post, 5 min har 100 posts ke baad!
- 🔥 **Error Handling**: Kuch gadbad hui? Script rukta nahi, agla post try karta hai!
- 😎 **Masti Mode**: Prints mein swag aur attitude, kyunki bhai ka style alag hai!

---

## Setup Kaise Kare? (Bhai Ka Master Plan) 🛠️
1. **Python Laga Le**: System mein Python 3.x install kar, bhai. Yeh toh basic hai! 🐍
2. **Telethon Daal Do**: Terminal khol aur yeh command thok do:
   ```bash
   pip install telethon
   ```
3. **API Credentials Lelo**:  
   - [my.telegram.org](https://my.telegram.org) pe jao.  
   - Login kar, "API Development Tools" pe click kar, aur ek app bana.  
   - `api_id` aur `api_hash` copy kar lo – yeh tera secret weapon hai, bhai! 🔑

---

## Script: `autoworker.py` (Automation Ka Baap) 🤖
Yeh script tera kaam aasaan karega – posts ko source se destination tak bot ke zariye le jayega!

### Kaise Chalaye?
- Script mein `api_id`, `api_hash`, aur `phone` apne daal do.  
- `SOURCE_CHANNEL` aur `DESTINATION_CHANNEL` ke IDs apne channels ke hisaab se update karo.  
  - Channel ID kaise milega? `@getidsbot` se ya Telegram ke URL se (jaise `-1002134433090`).  
- Bots ke usernames check karo (`BOT1`, `BOT2`, `BOT3`) – agar alag bots use karna hai toh badal do.  
- Command: `python autoworker.py`  
- Output mein dekho kaam ka jadoo, jaise:  
  ```
  Client started. Connected to your account.
  Processing post ID: 123
  Processed and posted: Post ID 123
  Processed 100 posts. Taking a 5-minute break to avoid ban.
  ```

---

## @sup_toon_1 Ki Shaan! 🔥
Bhai, yeh script banaya hai tere bhai ne – @sup_toon_1 ke mastermind ne! Yeh group hai asli entertainment ka adda:  

- **ID**: [https://t.me/sup_toon_1](https://t.me/sup_toon_1)  
- **Description**:  
  ⚠️ *ᴄʜᴀɴɴᴇʟ ᴅɪꜱᴄʟᴀɪᴍᴇʀ: ᴀʟʟ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ɪɴ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ ɪꜱ ᴇɪᴛʜᴇʀ ꜰᴏʀᴡᴀʀᴅᴇᴅ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟꜱ ᴏʀ ᴛᴀᴋᴇɴ ꜰʀᴏᴍ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴡᴇ ᴅᴏɴ'ᴛ ᴏᴡɴ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ.* 🚫  
  ❌ *ᴅᴏ ɴᴏᴛ ᴅᴏ ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴꜰʀɪɴɢᴇᴍᴇɴᴛ ɪɴᴛᴇɴᴅᴇᴅ* ❌  
  *ɪꜰ ᴜ ꜰɪɴᴅ ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛ ᴄᴏɴᴛᴇɴᴛ ᴍꜱɢ ʜᴇʀᴇ @CopyRightConte*  

- **Other Channels**:  
  📢 *🔥 Welcome to the Ultimate Streaming & Backup Hub! 🔥*  
  🚀 *@StreemCode1* - Sabhi Movies, Series & Anime ka Asli Adda!  
  🎬 *@FileFormatHere* - Direct File [MP4, MKV & More] Download Hub!  
  🔄 *@sup_toon_1* - Backup Group! Koi Link Work Na Kare? Yaha Se Le!  

✅ Har Language, Har Format, Har Quality – Sab Kuch Yahi Milega!  
✅ Agar Koi Content Chahiye? Request Karo & Enjoy Karo!  
📌 Jaldi Join Karo & Streaming ka Full Maza Uthao!  
🔥 Stay Tuned for the Best Entertainment Experience! 🔥  

Join karo aur maza lo, bhai log! 😎

---

## Contribute Karo, Bhai! 🤝
- Idea hai? Fork karo, code badlo, aur pull request bhejo!  
- Issue hai? GitHub pe bol do, bhai fix kar dega!  

---

## Credits
- **Coded by**: @sup_toon_1 ka baadshah! 😎  
- **Shoutout**: Sare bhai log jo @sup_toon_1 pe shaan badhate hain! 🔥  

---

### Extra Masti Tips 😜
- **Repo Description**:  
  "Automation ka boss – Telegram posts ko polish karke channel pe daalta hai! @sup_toon_1 ka swag! 😎"
- **Stars Maango**: @sup_toon_1 pe bol do – "Bhai log, repo pe star dena mat bhoolna, shaan badhao meri!" 🌟
