# -*- coding: utf-8 -*-
'''
auther : Zjy
Time : 2019/1/14  1:27 
Note : 地图 管理器
'''

import KBEngine
from KBEDebug import *


class SpaceMgr(KBEngine.Entity):
	"""
	账号实体
	客户端登陆到服务端后，服务端将自动创建这个实体，通过这个实体与客户端进行交互
	"""
	
	def __init__(self):
		KBEngine.Entity.__init__(self)