#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
import makeData.txtParser

#公会设施分析器
class cTxtParser(makeData.txtParser.cTxtParser):
	#override
	def getParseTxt(self):
		lKeyList1=[]
		lValList1=[]
		lKeyList2=[]
		lValList2=[]
		sKey0=""
		tFieldName=("Type","Effect","UpConsume","UpNeed","CDTime","Percent","Desc","EffectDesc")
		lLines=self.parseTxtTo2dGroup()

		for iRow,lLine in enumerate(lLines):
			sTemp=self.makeDict(tFieldName,lLine[2:],False,3)
			lKeyList2.append(lLine[1])
			lValList2.append(sTemp)

			if lLine[0]!="":
				sKey0=lLine[0]

			if self.isLastInGroup(lLines,iRow,0):
				sTemp=self.makeDict(lKeyList2,lValList2,True,2)
				lKeyList2=[]
				lValList2=[]
				lKeyList1.append(sKey0)
				lValList1.append(sTemp)

		return self.makeDict(lKeyList1,lValList1,True,1)





