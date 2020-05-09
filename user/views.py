from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse
from . import models
from django.core import serializers



# Create your views here.
from . import models
def reg(request): #注册会员
	uname=str(request.POST.get('uname'))
	mima=str(request.POST.get('mima'))
	dianhua=str(request.POST.get('dianhua'))
	name=str(request.POST.get('name'))
	user=models.User.objects.filter(uname=uname).count()
	if user==0:
		user=models.User(uname=uname,mima=mima,dianhua=dianhua,name=name)
		user.save()
		return HttpResponse('ok')
	else:
		return HttpResponse('none')
		pass
	return HttpResponse('none')
def reghtml(request): #登入会员
	return render(request, 'reg.html', )
def loginapi(request): #注册会员
	uname=str(request.POST.get('uname'))
	mima=str(request.POST.get('mima'))

	user=models.User.objects.filter(uname=uname,mima=mima).count()
	if user==1:
		request.session['uname'] = uname
		#request.session['id'] = uname
		return HttpResponse('ok')
	else:
		return HttpResponse('none')
		pass
	return HttpResponse('none')
def loginhtml(request): #注册会员
	return render(request, 'login.html', )
# objects.get()结果转换
def object_to_json(obj):
    return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])
def getopenid(request):  #获取openid
	code=str(request.GET.get('code'))
	url='''https://api.weixin.qq.com/sns/jscode2session?appid=wx94814d14eed848a4&secret=3792d6ba67a5a31475413e44fa13aa51&js_code='''+code+'''&grant_type=authorization_code'''
	r = requests.get(url)
	info=json.loads(r.content)
	#print(info)
	return  JsonResponse(info)
def login(request):  #获取openid
	name = request.COOKIES['PHPSESSID']
	user=models.User.objects.filter(openid=name).count()
	if user==0:
		user=models.User(openid=name)
		user.save()
	else:
		pass
	return HttpResponse('ok')
def getinfo(request):  #获取个人信息
	name = request.COOKIES['PHPSESSID']
	user=models.User.objects.get(openid=name)
	user=object_to_json(user)
	#user = json.loads(serializers.serialize("json",user))
	return JsonResponse(user, safe=False)
def baocun(request):  #获取个人信息
	name = request.COOKIES['PHPSESSID']
	touxiang=str(request.POST.get('touxiang'))
	dianhua=str(request.POST.get('dianhua'))

	user=models.User.objects.get(openid=name)
	user.dianhua=dianhua
	user.touxiang=touxiang
	user.save()
	image = user.touxiang
	options = {}
	imageType = "BASE64"
	groupId = "python"
	userId = user.openid
	client.addUser(image, imageType, groupId, userId);
	client.updateUser(image, imageType, groupId, userId, options)
	return  HttpResponse('ok')