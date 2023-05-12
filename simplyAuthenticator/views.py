from django.contrib.auth.views import LoginView, LogoutView

class simplyLogin(LoginView):
    template_name = 'login.html'

redirect_authenticated_user = True

class simplyLogout(LogoutView):
    def logout_view(selfrequest):
        logout(request)
    template_name = 'login.html'
    next_page = 'scanner'
