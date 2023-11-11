from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import *

# Create your views here.
def login_all(request):

    if 'submit' in request.POST:
        uname = request.POST['uname']
        psw = request.POST['psw']

        try:
            qa=login.objects.get(username=uname, password=psw)
            print(qa.usertype,'/////aaaaa')
            if qa:
                request.session['lid']=qa.pk
                if qa.usertype=='admin':
                    return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 1px; text-align: center; border-radius: 50px;">
        <img src="/static/loading.gif"  style="width: 100px; height: 200px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_home';
        }, 500); // Redirect after 2 seconds
    </script>
""")
                elif qa.usertype=='officer':
                        q1 = officer.objects.get(login_id=request.session['lid'])
                        if q1:
                            request.session['oid'] = q1.pk
                            return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif"  style="width: 100px; height: 200px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'officer_home';
        }, 500); // Redirect after 2 seconds
    </script>
""")
                elif qa.usertype=='user':
                            q2 = user.objects.get(login_id=request.session['lid'])
                            if q2:
                                request.session['uid'] = q2.pk                        
                                return HttpResponse("""
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
            <img src="/static/loading.gif"  style="width: 100px; height: 200px;border-radius: 20px;">
            <h3 style="color: red;">Loading......</h3>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = 'user_home';
            }, 500); // Redirect after 2 seconds
       </script>
    """)
                                        
        except:
            return HttpResponse("<script>alert('Invalid credentials');window.location='/login';</script>")
        
    return render(request,'login.html')







def public_home_page(request):
    
    return render(request, 'public_home_page.html')











##################################################          ADMIN MODULE            ################################################################################################

def admin_home(request):
    return render(request,'admin_home.html')

#MANAGE BLOCK#######################################################################################################################################################################


def manage_block(request):
    qa = blocks.objects.all()
    qt = types.objects.all()

    if 'submit' in  request.POST:
        block=request.POST['block']
        type=request.POST['type_name']

        q2 = blocks(block=block, type_id=type)
        q2.save()

        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/insert.jpg" alt="Smiley Image" style="width: 120px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;"> Successfully Inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_block';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    
    return render(request,'admin_manage_block.html',{'qa':qa, 'qt':qt})


def update_block(request,id):
    qa = blocks.objects.all()
    qt = types.objects.all()
    qz = blocks.objects.get(block_id=id)

    if 'update' in request.POST:
        block=request.POST['block']
        type=request.POST['type_name']

        qz.block=block
        qz.type_id=type
        qz.save()
        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_block';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    return render(request,'admin_manage_block.html',{'qa':qa, 'qt':qt,'qz':qz})


def delete_block(request,id):
    qa = blocks.objects.get(block_id=id)
    qa.delete()
    return HttpResponse( """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_block';
        }, 2000); // Redirect after 2 seconds
    </script>
""")


# MANAGE DISTRICT ############################################################################################################################################################


def manage_district(request):
    qa = district.objects.all()
    q1 = state.objects.all()

    if 'submit' in request.POST:
        d = request.POST['district']
        s = request.POST['state']

        q2 = district(district=d, state_id=s)
        q2.save()

        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/insert.jpg" alt="Smiley Image" style="width: 120px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_district';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    
    return render(request,'admin_manage_district.html',{'qa':qa, 'q1':q1})


def update_district(request,id):
    qa = district.objects.all()
    qs = state.objects.all()
    qz = district.objects.get(district_id=id)

    if 'update' in request.POST:
        d = request.POST['district']
        s = request.POST['state']

        qz.district=d
        qz.state_id=s
        qz.save()
        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_district';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    return render(request,'admin_manage_district.html',{'qa':qa, 'qz':qz,'qs':qs})      

def delete_district(request,id):
    qa = district.objects.get(district_id=id)
    qa.delete()
    return HttpResponse( """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_district';
        }, 2000); // Redirect after 2 seconds
    </script>
""")


# MANAGE TYPE ######################################################################################################################################################################


def manage_type(request):
    qa = types.objects.all()
    q1 = district.objects.all()

    if 'submit' in  request.POST:
        n=request.POST['name']
        t=request.POST['type']
        d=request.POST['district']

        q2 = types(name=n, type=t,district_id=d)
        q2.save()

        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/insert.jpg" alt="Smiley Image" style="width: 120px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_type';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    
    return render(request,'admin_manage_type.html',{'qa':qa, 'q1':q1})


def update_type(request,id):
    qa = types.objects.all()
    q1 = district.objects.all()
    qz = types.objects.get(type_id=id)

    if 'update' in request.POST:
        n=request.POST['name']
        t=request.POST['type']
        d=request.POST['district']

        qz.name=n
        qz.type=t
        qz.district_id=d
        qz.save()
        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_type';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    return render(request,'admin_manage_type.html',{'qa':qa, 'q1':q1,'qz':qz})


def delete_type(request,id):
    qa = types.objects.get(type_id=id)
    qa.delete()
    return HttpResponse( """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_type';
        }, 2000); // Redirect after 2 seconds
    </script>
""")


# MANAGE OFFICER #######################################################################################################################################################################


def manage_officer(request):
    q1=officer.objects.get(officer_id=request.session['oid'])

    if 'update' in request.POST:
        first=request.POST['fname']
        last=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        
        q1.fname=first
        q1.lname=last
        q1.place=place
        q1.phone=phone
        q1.email=email
        q1.save()
        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/officer_home';
        }, 2000); // Redirect after 2 seconds
    </script>
""")

    return render(request,'manage_officer.html',{'q1':q1})



def delete_officer(request,id):
    qa=officer.objects.get(officer_id=id)
    lid=qa.login_id
    q1=login.objects.get(login_id=lid)
    q1.delete()
    qa.delete()
    
    return HttpResponse( """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/admin_manage_officer';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
##########################################           MANAGE OFFICER          ##################################################################################################


def ad_manage_officer(request):
    qa = officer.objects.all()

    if 'submit' in request.POST:
        first = request.POST['first']
        lname = request.POST['lname']
        place = request.POST['place']
        phone = request.POST['phone']
        email = request.POST['email']
        q1 = officer(fname=first, lname=lname, place=place, phone=phone, email=email, login_id=request.session['lid'])
        q1.save()

        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/ad_manage_officer';
        }, 2000); // Redirect after 2 seconds
    </script>
""")
    
    return render(request,'ad_manage_officer.html',{'qa':qa})


def ad_update_officer(request,id):
    qa = officer.objects.all()
    q1 = officer.objects.get(officer_id=id)

    if 'update' in request.POST:
        first = request.POST['first']
        lname = request.POST['lname']
        place = request.POST['place']
        phone = request.POST['phone']
        email = request.POST['email']

        q1.fname = first
        q1.lname = lname
        q1.place = place
        q1.phone = phone
        q1.email = email
        q1.save()

        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/ad_manage_officer';
        }, 2000); // Redirect after 2 seconds
    </script>
""")

    return render(request,'ad_manage_officer.html',{'q1':q1,'qa':qa})


def ad_delete_officer(request,id):
    qa = officer.objects.get(officer_id=id)
    lid = qa.login_id
    lid = login.objects.get(login_id=lid)
    qa.delete()
    return HttpResponse( """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/ad_manage_officer';
        }, 2000); // Redirect after 2 seconds
    </script>
""")




#VIEW USER ########## VIEW POST ######################################################################################################################################################################################


def view_users(request):
    qa = user.objects.all()
    return render(request,'admin_view_users.html',{'qa':qa})


def view_post(request):
    id=request.GET.get('user_id',None)
    qa=post.objects.filter(user_id=id)
    return render(request,'admin_view_post.html',{'id':id,'qa':qa})


#VIEW COMPLAINTS #############################################################################################################################################################################################


def view_complaints(request):
    qa = complaints.objects.all()
    return render(request,'admin_view_complaints.html',{'qa':qa})
 
def send_reply(request):
    id = request.GET.get('complaint_id', None)
    if 'submit' in request.POST:
        r=request.POST['reply']
        qa=complaints.objects.get(complaint_id=id)
        qa.reply=r
        qa.save()
        return redirect('/admin_view_complaints')
    return render(request,'send_reply.html',{'id':id})




###########################################      OFFICER MODULE       ###############################################################################################################################################


def officer_home(request):
    return render(request,'officer_home.html')

def officer_view_post(request):

    return render(request,'officer_view_post.html')

def officer_update(request,id): 
    if 'submit' in request.POST:
        status = request.POST['status']
        q1 = post.objects.get(post_id = id)

        q1.status=status
        q1.save()
        return HttpResponse("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/update.jpg" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/officer_view_post';
        }, 2000); // Redirect after 2 seconds
    </script>
 """)
    return render(request,'officer_update.html')
# MANAGE OFFICER PROFILE #############################################################################################################################################################################################




def officer_view_post(request):
    qa = post.objects.all()
    return render(request,'officer_view_post.html', {'qa':qa})



############################################          USER MODULE         ###############################################################################################################################################################


def user_home(request):
    return render(request,'user_home.html')


def user_registration(request):
    if 'submit' in request.POST:
        first = request.POST['fname']
        last = request.POST['lname']
        p = request.POST['place']
        b = request.POST['block']
        ph = request.POST['phone']
        e = request.POST['email']
        username = request.POST['uname']
        password = request.POST['psw']

        obj = login(username=username, password=password, usertype='user')
        obj.save()
        print(obj.pk)
        q = user(fname=first, lname=last, place=p, phone=ph, email=e, block_id=b, login_id=obj.pk)
        q.save()
        return redirect('/login')
    return render(request,'user_registration.html')


# SEND COMPLAINTS #############################################################################################################################################################################################################################


def user_send_complaint(request):

    if 'submit' in request.POST: 
        complaint = request.POST['comp']
        d = request.POST['date']
        q = complaints(complaints=complaint, date=d, user_id=request.session['uid'], reply='pending')
        q.save()
        return HttpResponse("<script>alert('Complaint is send');window.location='/user_home'</script>")
    qa = complaints.objects.all()
    return render(request,'user_send_complaint.html')


# View reply ########################################################################################################################################################################################################################################


def user_view_reply(request):
    id=request.session['uid']
    qa = complaints.objects.filter(user_id=id)
    return render(request,'user_view_reply.html',{'qa':qa,'id':id})


# POST ################################################################################################################################################################################################################################################


def add_post(request):
    q1 = post.objects.all()

    if 'submit' in request.POST:
        posts = request.POST['posts']
        date = request.POST['date']
        type = request.POST['type']
        q = post(post=posts, date=date, type=type, status='pending', user_id=request.session['uid'])
        q.save()
    return render(request,'user_post.html', {'q1':q1})


# COMMENT #################################################################################################################################################################################################################################################

def user_post_comment(request):
    q1 = post.objects.all()

    if 'submit' in request.POST:
        posts = request.POST['posts']
        date = request.POST['date']
        type = request.POST['type']
        q = post(post=posts, date=date, type=type, status='pending', user_id=request.session['uid'])
        q.save()
    return render(request,'user_post_comment.html', {'q1':q1})

def comments(request):
    id=request.GET.get('id',None)
    if 'submit' in request.POST:
        comments = request.POST['comment']
        date = request.POST['date']
        q = comment(comments=comments, reply='pending',date=date,post_id=id)
        q.save()
        return redirect('/user_post_comment')
    return render(request,'comments.html')
