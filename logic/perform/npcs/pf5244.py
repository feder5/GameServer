# -*- coding: utf-8 -*-
from perform.defines import *
from perform.npcs.pf5144 import Perform as CustomPerform

#导表开始
class Perform(CustomPerform):
	id = 5244
	name = "高级汇灵"
	configInfo = {
		"符能":30,
	}
#导表结束