# -*- coding: utf-8 -*-
from KBEDebug import *


class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)

# ---------------------------------------------客户端请求------------------------------------------
	def	 ReqCreateAvatar(self):
		'''
		创建角色
		:return:
		'''
		pass

	def GetAvatarList(self):
		'''
		返回角色列表
		:return:
		'''

#---------------------------------------------kbe回调------------------------------------------
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
<<<<<<< HEAD
		
		
=======

>>>>>>> 2a1449d319b0c1b2048237bea59bc539f8d2105c
	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))

	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT

	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()

	def onGiveClientToFailure(self):
		"""
		如果在脚本中实现了此回调，当实体调用giveClientTo失败时，该回调被调用。这个方法没有参数。

		"""
		pass



