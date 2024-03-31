from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⏸️ ᴘᴀᴜsᴇ ⏸️",
            description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴜsɪᴄ.",
            thumb_url="https://te.legra.ph/file/9dcb4e3f8392e4aea0292.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="⏹️ ʀᴇsᴜᴍᴇ ⏹️",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ ᴍᴜsɪᴄ.",
            thumb_url="https://te.legra.ph/file/78445accf6d74242d56fb.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⏩ sᴋɪᴘ ⏩",
            description=f"sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴜsɪᴄ & ᴘʟᴀʏ ɴᴇxᴛ ᴍᴜsɪᴄ",
            thumb_url="https://te.legra.ph/file/dd8423621d77860885d70.jpg",
            input_message_content=InputTextMessageContent("/skip", "/next"),
        ),
        InlineQueryResultArticle(
            title="📴 ᴇɴᴅ 📴",
            description="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.",
            thumb_url="https://te.legra.ph/file/6f3513fabd84be1ecf423.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🔉 sʜᴜғғʟᴇ 🔉",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴜsɪᴄ.",
            thumb_url="https://te.legra.ph/file/3810eb9a72fd36c0aed50.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🔈 ʟᴏᴏᴘ 🔈",
            description="ʟᴏᴏᴘ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ .",
            thumb_url="https://te.legra.ph/file/d35e187e613d1b6cbfb07.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
