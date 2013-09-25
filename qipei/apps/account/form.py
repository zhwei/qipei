#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm,CharField,EmailField,ChoiceField

from DjangoUeditor.forms import UEditorField

BOOLE_CHOICES=(
    ('是','1'),
    ('否','0'),
)

class RegisterForm(forms.Form):
    email=forms.EmailField(label=_(u"邮箱 "),max_length=30,
                           widget=forms.TextInput(attrs={'size': 30,}),
                           help_text="")
    username=forms.CharField(label=_(u"用户名 "),max_length=30,
                             widget=forms.TextInput(attrs={'size': 20,}),
                           help_text="")
    password=forms.CharField(label=_(u"密码 "),max_length=30,
                             widget=forms.PasswordInput(attrs={'size': 20,}),
                           help_text="")
    re_password=forms.CharField(label=_(u"重复密码 "),max_length=30,
                                widget=forms.PasswordInput(attrs={'size': 20,}),
                           help_text="")
    real_name = forms.CharField(label=_(u"真实姓名 "), max_length=5,
                                widget=forms.TextInput(attrs={'size':5,}),
                                help_text="填写真实姓名更容易让您通过验证!")

    def clean_username(self):
        '''验证重复昵称'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(_(u"该用户名已经被使用"))
        
    def clean_email(self):
        '''验证重复email'''
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(_(u"该邮箱已经被使用"))
        
class LoginForm(forms.Form):

    username=forms.CharField(label=_(u"用户名"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label=_(u"密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))


class UserForm(ModelForm):
    class Meta:
        model=User
        fields=('first_name','email','is_staff','is_superuser')
        widgets={
            # 'first_name':
        }


    def clean_email(self):
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(_(u"该邮箱已经被使用请使用其他的"))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=_(u"原密码"),max_length=30,
                                   widget=forms.PasswordInput(attrs={'size': 20,}))
    new_password = forms.CharField(label=_(u"新密码"),max_length=30,
                                   widget=forms.PasswordInput(attrs={'size': 20,}))
    new_password1 = forms.CharField(label=_(u"新密码确认"),max_length=30,
                                    widget=forms.PasswordInput(attrs={'size': 20,}))

    def clean_newpw(self):
        if self.new_password != self.new_password2:
            raise forms.ValidationError(_(u"两次输入的密码不同!"))



class CreateUserForm(forms.Form):

    email=forms.EmailField(label=_(u"邮箱"), max_length=50,
                           widget=forms.TextInput(attrs={'size': 50}))
    username = forms.CharField(label=_(u'用户名'), max_length=30,
                               widget=forms.TextInput(attrs={'size':30}))
    password = forms.CharField(label=_(u'密码'), max_length=30,
                               widget=forms.TextInput(attrs={'size':30}))


    def clean_username(self):
        '''验证重复昵称'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(_(u"该昵称已经被使用请使用其他的昵称"))

    def clean_email(self):
        '''验证重复email'''
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(_(u"该邮箱已经被使用"))

# class CreateUserForm(ModelForm):
#
#     class Meta:
#         model = User
#         fields = ('email','username','password')
#
#
#     def clean_username(self):
#         '''验证重复昵称'''
#         users = User.objects.filter(username__iexact=self.cleaned_data["username"])
#         if not users:
#             return self.cleaned_data["username"]
#         raise forms.ValidationError(_(u"该昵称已经被使用请使用其他的昵称"))
#
#     def clean_email(self):
#         '''验证重复email'''
#         emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
#         if not emails:
#             return self.cleaned_data["email"]
#         raise forms.ValidationError(_(u"该邮箱已经被使用"))

class NotifyForm(forms.Form):

    # level = forms.ChoiceField(label='通知等级', choices=(('success','成功'),('info', '信息'),
    #                                                  ('warning', '警告'),('error', '错误')))

    recipient=forms.IntegerField(label='接收者ID', help_text='请输入接收者的用户ID')

    verb = forms.CharField(label='通知主题',)

    description = UEditorField(label='通知内容',imagePath='notify/img',
                           filePath='notify/file', toolbars='mini')