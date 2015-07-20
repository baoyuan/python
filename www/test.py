#!/usr/bin/env python3
# coding=utf-8

import orm, asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop = loop, user = 'root', password = 'root', db = 'awesome')
    u = User(name = 'Test', email = 'test@example.com', passwd = '1234', image = 'about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
