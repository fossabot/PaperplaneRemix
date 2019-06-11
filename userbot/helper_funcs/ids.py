# TG-UserBot - A modular Telegram UserBot for Python3.6+. 
# Copyright (C) 2019  Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.


from telethon.tl.types import MessageEntityMention, MessageEntityMentionName


async def get_user_from_entity(event):
    for entity in event.entities:
        if isinstance(entity, MessageEntityMentionName):
            return entity.user_id
        elif isinstance(entity, MessageEntityMention):
            offset = entity.offset
            length = entity.length
            maxlen = offset + length
            return event.text[offset:maxlen]
    return None