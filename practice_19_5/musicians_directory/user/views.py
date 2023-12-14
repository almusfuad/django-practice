from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View

# Create your views here.
class UserSignUpView(View):
      template_name = 'signup.html'
      form_class = UserCreationForm
      
      def get(self, request, *args, **kwargs):
            sign_form = self.form_class()
            return render(request, self.template_name, {'form': sign_form})
      
      def post(self, request, *args, **kwargs):
            sign_form = self.form_class(request.POST)
            if sign_form.is_valid():
                  form.save(commit = False)
                  return redirect('login')
            return render(request, self.template_name, {'form': sign_form})