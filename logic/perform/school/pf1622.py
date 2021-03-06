# -*- coding: utf-8 -*-
from perform.defines import *
from perform.object import RevivePerform as CustomPerform

#导表开始
class Perform(CustomPerform):
	id = 1622
	name = "枯树生花"
	targetType = PERFORM_TARGET_FRIEND
	targetCount = 1
	bout = 1
	damage = lambda self,SLV:SLV*2+20
	power = 100
	consumeList = {
		"真气": lambda SLV:SLV*1.2+50,
		"符能": 20,
	}
	speRatio = 100
#导表结束