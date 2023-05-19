from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views import View

class simplyLogin(LoginView):
    template_name = 'login.html'

redirect_authenticated_user = True

class simplyLogout(LogoutView):
    def logout_view(selfrequest):
        logout(request)
    template_name = 'login.html'
    next_page = 'scanner'

class ManageUserView(View):
    def get(self, request):
        pengguna = User.objects.all()
        return render(request, 'manage_pengguna.html', {'users': pengguna})
    
class CreateUserView(View):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('manage_users')
    
class EditUserView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'edit_user.html', {'user': user})

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('manage_users')