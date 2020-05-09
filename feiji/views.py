from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse
from . import models
from django.core import serializers
from  ji.models import Ji
from random import *

# Create your views here.
from . import models

def index(request): #首页
	try:
		if request.session['uname']=='':
			return HttpResponse('请登入')
	except:
		return HttpResponse('请登入')
	feiji=Ji.objects.filter(status='1')
	hang=['A','B','C','D','E','F','G','H']
	lie=[1,2,3,4,5,6]
	return render(request, 'index.html',{'feiji': feiji,'hang':hang,'lie':lie} )
def getfeiji(request): #首页
	jid=str(request.POST.get('id'))
	
	feiji=models.Feiji.objects.filter(jid=jid)
	shuzu={}
	hang=['A','B','C','D','E','F','G','H']
	lie=[1,2,3,4,5,6]
	for h in hang:
		#temp={}
		for l in lie:
			shuzu[h+str(l)]=0
	for zuo in feiji:
		
		shuzu[zuo.zuowei]=1
	return JsonResponse(shuzu, safe=False)
		
	
def dingpiao(request): #定飞机票
    
	
	jid=request.POST.get('id')
	num=int(request.POST.get('num'))
	type=str(request.POST.get('type'))
	uid=request.session['uname']
	feiji=models.Feiji.objects.filter(jid=jid)

	shuzu={}
	hang=['A','B','C','D','E','F','G','H']
	lie=[1,2,3,4,5,6]
	for h in hang:
		#temp={}
		for l in lie:
			shuzu[h+str(l)]=0
	for zuo in feiji:
		shuzu[zuo.zuowei]=1

	if num==1:# 1人的时候判断是否靠窗

		if  type=='0':
			for n in shuzu:
				if shuzu[n]==0:
					fei=models.Feiji(uid=uid, jid=jid,zuowei=n)
					fei.save()
					return HttpResponse(n)
			
		if  type=='1':  #要求过道
			for h in hang:
				for l in [3,4]:	
					if shuzu[h+str(l)]==0:
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l))
						fei.save()
						return HttpResponse(h+str(l))
		if  type=='2':  #要求窗户
			for h in hang:
				for l in [1,6]:	
					if shuzu[h+str(l)]==0:
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l))
						fei.save()
						return HttpResponse(h+str(l))
	if num==2 : #2人的时候，要选连坐
		for h in hang:
				for l in [1,2]:	
					if shuzu[h+str(l)]==0 and shuzu[h+str(l+1)]==0:
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l))
						fei.save()
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l+1))
						fei.save()
						return HttpResponse(h+str(l)+'和'+h+str(l+1))
				for l in [4,5]:
					if shuzu[h+str(l)]==0 and shuzu[h+str(l+1)]==0:
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l))
						fei.save()
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l+1))
						fei.save()
						return HttpResponse(h+str(l)+'和'+h+str(l+1))
	if num==3 : #2人的时候，要选连坐
		for h in hang:
				for l in [1]:	
					if shuzu[h+str(l)]==0 and shuzu[h+str(l+1)]==0  and shuzu[h+str(l+2)]==0:
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l))
						fei.save()
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l+1))
						fei.save()
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l+2))
						fei.save()
						return HttpResponse(h+str(l)+'和'+h+str(l+1)+'和'+h+str(l+2))
				for l in [4]:
					if shuzu[h+str(l)]==0 and shuzu[h+str(l+1)]==0  and shuzu[h+str(l+2)]==0:
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l))
						fei.save()
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l+1))
						fei.save()
						fei=models.Feiji(uid=uid,jid=jid,zuowei=h+str(l+2))
						fei.save()
						return HttpResponse(h+str(l)+'和'+h+str(l+1)+'和'+h+str(l+2))
	return HttpResponse('none')
def getinfo(request): #某人的机票
	uid=request.session['uname']
	jid=request.POST.get('id')
	feiji=models.Feiji.objects.filter(jid=jid,uid=uid)
	feiji = json.loads(serializers.serialize("json",feiji))
	return JsonResponse(feiji, safe=False)
# objects.get()结果转换
def chongzhi(request): #重置某飞机
	jid=request.POST.get('id')
	models.Feiji.objects.filter(jid=jid).delete()
	return HttpResponse('ok')
def object_to_json(obj):
    return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])
