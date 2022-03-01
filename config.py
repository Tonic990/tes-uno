#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import json

with open("config.json","r") as f:
    config = json.loads(f.read())

TOKEN = getenv("BOT_TOKEN")
WORKERS = getenv("32")
ADMIN_LIST = getenv("ADMIN_LIST")
OPEN_LOBBY = getenv("True")
ENABLE_TRANSLATIONS = getenv("False")
DEFAULT_GAMEMODE = getenv("Fast")
WAITING_TIME = getenv("120")
TIME_REMOVAL_AFTER_SKIP = getenv("20")
MIN_FAST_TURN_TIME = getenv("15")
MIN_PLAYERS = getenv("2")
