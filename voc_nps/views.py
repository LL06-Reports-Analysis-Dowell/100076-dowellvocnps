from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
#from voc_nps.dowell_scale import Scale,Scale_user
import json
from . import passgen
from . import dowellconnection
from . import autologinfunction
from cryptography.fernet import Fernet
from PIL import Image
from voc_nps import models
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import requests

def encode(key,text):
    cipher_suite = Fernet(key.encode())
    encoded_text = cipher_suite.encrypt(text.encode())
    return encoded_text
def decode(key,decodetext):
    cipher_suite = Fernet(key.encode())
    decoded_text = cipher_suite.decrypt(decodetext.encode())
    return decoded_text.decode()
key="l6h8C92XGJmQ_aXpPN7_VUMzA8LS8Bg50A83KNcrVhQ="
from django.views.decorators.clickjacking import (
    xframe_options_exempt
)
from . import qrcodegen



@method_decorator(xframe_options_exempt, name='dispatch')
def index(request):
    return render(request,'voc/nps_index.html')


@method_decorator(xframe_options_exempt, name='dispatch')
def home(request):
    return render(request,'voc/home.html')


@xframe_options_exempt
def preview(request):
    return render(request,'voc/nps_privew.html')



@method_decorator(xframe_options_exempt, name='dispatch')
def emcode(request):
    return render(request,'voc/nps_emcode.html')



@method_decorator(xframe_options_exempt, name='dispatch')
def qrGen(request):
    context={}
    if request.method == 'POST':
        brand1 = request.POST['brand']
        brand=encode(key,brand1)
        product1 = request.POST['product']
        product=encode(key,product1)
        is_accept = request.POST['checkbox']
        logo=request.FILES['logo']
        loc=request.POST["loc"]
        device=request.POST["dev"]
        os=request.POST["os"]
        browser =request.POST["brow"]
        ltime=request.POST["time"]
        ipuser=request.POST["ip"]
        conn=request.POST["conn"]
        ruser=passgen.generate_random_password1(8)
        rpass=passgen.generate_random_password(10)

        data= json.dumps({
            "username":ruser,
            "email": f'{ruser}@lav.com',
            "phone": 12345678,
            "first_name" :"nps_user",
            "last_name": "voc",
            "teamcode": "15692532",
            "password": rpass,
            "phonecode": 919
      })

        headers = {'content-type': 'application/json'}
        url = 'https://100014.pythonanywhere.com/api/register/'
        response = requests.request('POST',url, headers=headers,data=data)
        response_data = response.json()

        url1 = 'https://100014.pythonanywhere.com/api/linklogin/'
        headers = {'content-type': 'application/json'}
        data1 = json.dumps({"username":ruser,"password":rpass})
        req=requests.post(url1,headers=headers,data=data1)
        dic=json.loads(req.text)
        session_id = dic["session_id"]
        print(session_id)

        field={"Username":ruser,"OS":os,"Device":device,"Browser":browser,"Location":loc,"Time":str(ltime),"SessionID":"abcdefgh","Connection":conn}
        auto_login = autologinfunction.dowellconnection("login","bangalore","login","login","login","6752828281","ABCDE","insert",field,"nil")
        r={'username':ruser}
        qrcodegen.qrgen1(json.dumps(r),f"dowell_login/media/userqrcodes/{ruser}.png")
        logoname1=logo.name.replace(" ","")
        logoname=encode(key,logoname1)
        qrcodegen.qrgen(logo,"https://100076.pythonanywhere.com/brandurl",brand.decode(),product.decode(),f"dowell_login/media/qrcodes/{logoname1}",logoname.decode())
        insertdata=models.voc_nps(brand=brand,product=product,is_accept=is_accept,upload=logo,username=ruser,qrcodename=f'dowell_login/media/qrcodes/{logoname1}.png',userqrcode=f'dowell_login/media/userqrcodes/{ruser}.png',link=f"https://100076.pythonanywhere.com/nps/brandurl/?brand={brand},product={product},logo={logoname.decode()}")
        insertdata.save()
        field = {"brand":brand.decode('utf-8'),"product":product.decode('utf-8'),"is_accept":is_accept,"upload":f'https://100076.pythonanywhere.com/media/brandlogos/{logoname1}',"username":ruser,"qrcodename":f"dowell_login/media/qrcodes/{logoname1}.png","userqrcode":f"dowell_login/media/userqrcodes/{ruser}.png","link":f"https://100076.pythonanywhere.com/nps/brandurl/?brand={brand},product={product},logo={logoname.decode()}"}
        pfm_response=dowellconnection.dowellconnection("voc","bangalore","voc","voc_nps","voc_nps","1081","ABCDE","insert",field,"nil")
        with Image.open(f"dowell_login/media/qrcodes/{logoname1}") as image:
            image.thumbnail((128,128))
            image.save(f"dowell_login/media/qrcodes/thumbnails/{logoname1}","JPEG")
        with Image.open(f"dowell_login/media/brandlogos/{logo.name.replace(' ','_')}") as image:
            image.thumbnail((256,256))
            image.save(f"dowell_login/media/brandlogos/thumbnails/{logoname1}",quality=100)
        context["linkurl"]=f"https://100076.pythonanywhere.com/brandurl?brand={brand.decode()}&product={product.decode()}&logo={logoname.decode()}"
        context["brnd"]=brand1
        context["prd"]=product1
        context["img"]=logoname1
        return render(request,'voc/nps_showqr.html',context)
    return render(request,'voc/nps_emcode.html')


@method_decorator(xframe_options_exempt, name='dispatch')
def ShowQr(request):
    context={}
    en=encode(key,"dowell_test")
    context["encd"]=en
    context["enc"]=decode(key,en.decode())
    return render(request,'voc/nps_showqr.html',context)


@method_decorator(xframe_options_exempt, name='dispatch')
def ShowVideo(request):
    context={}
    return render(request,'voc/nps_video.html',context)



@method_decorator(xframe_options_exempt, name='dispatch')
def preview1(request):
    context={}
    if request.method == 'POST':
        rate = request.POST['rate']
        brand = request.POST['brand']
        product = request.POST['product']
        context["success"]="Thank you for rating our product"
        return render(request,'voc/test.html',context)
    brand=request.GET.get('brand',None)
    context["brand"]=decode(key,brand)
    product=request.GET.get('product',None)
    context["product"]=decode(key,product)
    logo=request.GET.get('logo',None)
    context["logo"]=decode(key,logo)
    return render(request,'voc/nps_responsive_preview.html',context)


@method_decorator(xframe_options_exempt, name='dispatch')
def SendMail(request):
    context={}
    if request.method == 'POST':
        email = request.POST['email']
        user = request.POST['user']
        img = request.POST['imager']
        urlim = request.POST['urlsr']
        context["email"]=email
        htmlgen = f"Dear {user}, <br> QR code link  is <strong>https://100076.pythonanywhere.com/media/qrcodes/{img}</strong> <br/> <h2><br> Embed this code to your website copy this and paste your website</h2><br>&lt;iframe width='300' height='500' style='background-color:white' src='{urlim}' style='-webkit-transform:scale(0.7);-moz-transform-scale(0.7);' FRAMEBORDER='no' BORDER='0' SCROLLING='no'&gt;&lt;/iframe&gt;>"
        send_mail('Embed your code to your website',"Thank You",'dowelllogintest@gmail.com',[email], fail_silently=False, html_message=htmlgen)
        context["user"]=user
        context["email"]=email
        context["urlm"]=urlim
        return render(request,'voc/nps_qrsend.html',context)


@method_decorator(xframe_options_exempt, name='dispatch')
def sendfeed(request):
    context={}
    context["success"]="Thank you for rating our product"
    if request.method == 'POST':
        rate = request.POST['rate']
        brand = request.POST['brand']
        product = request.POST['product']
        baseurl = request.POST['baseurl']
        context["success"]="Thank you for rating our product"
        context["baseurl"]=baseurl
        #return render(request,'voc/nps_preview.html',context)
        #return redirect(baseurl)
        return render(request,'voc/test.html',context)
    context["brand"]=request.GET.get('brand',None)
    context["product"]=request.GET.get('product',None)
    context["logo"]=request.GET.get('logo',None)
    return render(request,'voc/nps_responsive_preview.html',context)
    #return render(request,'voc/nps_responsive_preview.html',context)



@method_decorator(xframe_options_exempt, name='dispatch')
def logout(request):
    del request.session["username"]
    return redirect('https://100014.pythonanywhere.com/')
