# -*- coding: utf-8 -*-
from task.defines import *
from task.pett.t50001 import Task as customTask

#导表开始
class Task(customTask):
	parentId = 50001
	targetType = TASK_TARGET_TYPE_NPC
	icon = 2
	title = '''螺旋草·善恶'''
	intro = '''与$target交谈，回报经过'''
	detail = '''击败樵夫后，与螺旋草一道去见异兽仙子，讲述事情经过。'''
	rewardDesc = ''''''
	goAheadScript = ''''''
	initScript = '''E(10208,1011)'''
#导表结束