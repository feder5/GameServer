# -*- coding: utf-8 -*-
from buff.defines import *
from buff.object import Buff as CustomBuff

#导表开始
class Buff(CustomBuff):
	name = "高级隐形"
	type = BUFF_TYPE_SPECIAL
	applyList = {
		"隐身":True,
		"物理伤害结果加成":-15,
		"法术伤害结果加成":-15,
		"禁止法术":True,
	}
#导表结束