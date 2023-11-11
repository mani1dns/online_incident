from django.db import models

# Create your models here.
class login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    usertype = models.CharField(max_length=225)


class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=225)


class district(models.Model):
    district_id = models.AutoField(primary_key=True)
    state = models.ForeignKey(state,on_delete=models.CASCADE)
    district = models.CharField(max_length=225)


class types(models.Model):
    type_id = models.AutoField(primary_key=True)
    district = models.ForeignKey(district,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    type = models.CharField(max_length=225)


class blocks(models.Model):
    block_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(types,on_delete=models.CASCADE)
    block = models.CharField(max_length=225)


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(login,on_delete=models.CASCADE)
    block = models.ForeignKey(blocks,on_delete=models.CASCADE)
    fname = models.CharField(max_length=225)
    lname = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    email = models.CharField(max_length=225)


class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    post = models.CharField(max_length=225)
    date = models.CharField(max_length=225)
    type = models.CharField(max_length=225)
    status = models.CharField(max_length=225)


class officer(models.Model):
    officer_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=225)
    lname = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    email = models.CharField(max_length=225)


class assignstaff(models.Model):
    assign_id = models.AutoField(primary_key=True)
    officer = models.ForeignKey(officer,on_delete=models.CASCADE)
    assigned = models.CharField(max_length=225)


class work_status(models.Model):
    work_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    description = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    date = models.CharField(max_length=225)


class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    comments = models.CharField(max_length=225)
    reply = models.CharField(max_length=225)
    date = models.CharField(max_length=225)


class complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    complaints = models.CharField(max_length=225)
    reply = models.CharField(max_length=225)
    date = models.CharField(max_length=225)