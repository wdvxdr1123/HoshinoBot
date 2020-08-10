from hoshino import R, Service, priv, util

sv = Service('special_title', visible=False)


@sv.on_prefix("申请头衔")
async def get_special_title(bot, ev):
    uid = ev.user_id
    gid = ev.group_id
    sp_title = ev.message.extract_plain_text().strip()
    if len(sp_title) > 0:
        await bot.set_group_special_title(group_id=gid, user_id=uid, special_title=sp_title, duration=-1)
