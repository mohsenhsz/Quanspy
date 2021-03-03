from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from bucket import bucket
from django.contrib import messages
from accounts.forms import UserProfileForm
from django.conf import settings
from permissions import IsSuperUserMixin


class Home(View):
    def get(self, request):
        return render(request, 'core/home.html')

    def post(self, request):
        pass


class BucketHome(IsSuperUserMixin, View):
    template_name = 'core/buckets.html'
    contents = bucket.get_objects
    form_class = UserProfileForm

    def get(self, request):
        objects = self.contents
        return render(request, self.template_name, {'objects':objects, 'form':self.form_class})

        
class BucketDelete(LoginRequiredMixin, View):
    def get(self, request, key):
        bucket.delete_object(key)
        messages.success(request, 'Deleted successfully.', 'info')
        return redirect('core:buckets_home') 


class BucketDownload(LoginRequiredMixin, View):
    def get(self, request, key):
        bucket.download_object(key)
        messages.success(request, 'Your file downloaded successfully', 'info')
        return redirect('core:buckets_home')


class BucketUpload(LoginRequiredMixin, View):  
    def post(self, request):

        file_obj = request.FILES['filename']
        # file_path = settings.AWS_LOCAL_STORAGE + file_obj.name
        file_path = file_obj.temporary_file_path
        bucket.upload_object(file_path)
        messages.success(request, 'Your file uploaded successfully', 'info')
        return redirect('core:buckets_home')




