from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, models, widgets,Form
from .models import Reporter, Article
from django.contrib.auth.models import User


class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = "__all__" 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
        # thuoc tinh hien len tren web
    
    # muốn kt trùng nhau thì clean_<ten_thuoc_tinh>
    # hàm clean_abc() sẽ dc gọi khi hàm abc.is_valid() chạy để kiểm tra
    def clean_email(self):
        input_email = self.cleaned_data['email']
        try:
            Reporter.objects.get(email=input_email)
        except Reporter.DoesNotExist:
            return input_email
            # pass
        #email da ton tai
        #raise error 
        raise ValidationError(f"{input_email} da ton tai. Vui long nhap lai")


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__" 
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reporter': forms.Select(attrs={'class': 'form-control'})
        }
    
class RegisterForm(Form):
    username=forms.CharField(label="Tên Đăng Nhập", widget=forms.TextInput(attrs={"class": "form-control", "id": "user"}))
    password = forms.CharField(label="Mật Khẩu", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "pass"}))
    confirm_pass= forms.CharField(label="Nhập Lại Mật Khẩu", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "cfpass"}))
    first_name = forms.CharField(label="Họ", widget=forms.TextInput(attrs={"class": "form-control", "id": "firstname"}))
    last_name = forms.CharField(label="Tên", widget=forms.TextInput(attrs={"class": "form-control", "id": "lastname"}))
    email = forms.EmailField(label="Nhập emai", widget=forms.EmailInput(attrs={"class": "form-control", "id": "emai"}))

    def clean_username(self):
        input_username = self.cleaned_data['username']
        try:
            User.objects.get(username=input_username)
            raise ValidationError(f"Tên đăng nhập {input_username} đã tồn tại. Vui lòng nhập tên khác")
        except User.DoesNotExist:
            return input_username

    def clean_email(self):
        input_email = self.cleaned_data['email']
        try:
            User.objects.get(email=input_email)
            raise ValidationError(f"Email {input_email} đã tồn tại. Vui lòng nhập email khác")
        except User.DoesNotExist:
            return input_email
    
    def clean_confirm_pass(self):
        input_password = self.cleaned_data['password']
        input_confirm_pass = self.cleaned_data['confirm_pass']
        if input_password != input_confirm_pass: # làm thêm về độ mạnh mật khẩu
            raise ValidationError(f"Mật khẩu không trùng nhau")
        return 

    def save_user(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )

class LoginForm(Form):
    username=forms.CharField(label="Tên Đăng Nhập", widget=forms.TextInput(attrs={"class": "form-control", "id": "user"}))
    password = forms.CharField(label="Mật Khẩu", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "pass"}))