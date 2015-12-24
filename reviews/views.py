from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from django.contrib import messages


from models import Review
from saleor.userprofile.models import User
from saleor.product.models.base import Product


class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['subject', 'user_name', 'comment', 'rating']

    def get_success_url(self):
        return '/'

    def post(self, request, *args, **kwargs):
        value = super(CreateReview, self).post(request, *args, **kwargs)
        msg = "Thank you! Your review will be checked by a staff member before being made public. This is only to prevent spam and innapropriate language!"
        messages.success(request, msg)
        return redirect(request.GET.get('next', '/'))

    def form_valid(self, form):
        review = form.save(commit=False)
        print self.kwargs
        print self.kwargs['product_id']
        review.product = Product.objects.get(id=self.kwargs['product_id'])
        review.user = User.objects.get(id=self.request.user.id)  # use your own profile here
        review.save()
        return HttpResponseRedirect(self.get_success_url())


class EditReview(LoginRequiredMixin, UpdateView):
    model = Review
    success_url = "/"
    fields = ['subject', 'user_name', 'comment', 'rating']

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            response = super(EditReview, self).get(request, *args, **kwargs)
            return response
        else:
            return HttpResponseForbidden() #you can't go here!

    def post(self, request, *args, **kwargs):
        value = super(EditReview, self).post(request, *args, **kwargs)
        msg = "Thank you! Your review will be checked by a staff member before being made public. This is only to prevent spam and innapropriate language!"
        messages.success(request, msg)
        return redirect(request.GET.get('next', '/'))

    def get_object(self, queryset=None):
        obj = Review.objects.get(id=self.kwargs['review_id'])
        return obj

    def form_valid(self, form):
        review = form.save(commit=False)
        review.validated = False
        review.save()
        return HttpResponseRedirect(self.get_success_url())
