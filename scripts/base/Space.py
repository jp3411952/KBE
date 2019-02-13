# -*- coding: utf-8 -*-
'''
auther : Zjy
Time : 2019/2/13  22:36 
Note :
'''

import KBEngine
from KBEDebug import *


class Space(KBEngine.Entity):
	"""
	账号实体
	客户端登陆到服务端后，服务端将自动创建这个实体，通过这个实体与客户端进行交互
	"""
	
	def __init__(self):
		KBEngine.Entity.__init__(self)