from booking.views import form
from django import forms
from django.db.models import fields
from .models import Customers, Room, Pricing
from ownerAdmin import models


class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_view', 'occupation_adult', 'occupation_children', 'room_size', 'room_beds',
                  'room_number']


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_view', 'occupation_adult', 'occupation_children', 'room_size', 'room_beds',
                  'room_image', 'room_number', 'room_features_price']


class EditPricing(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['bed_price', 'breakfast_only_price', 'half_board_price', 'full_board_price', 'all_inclusive_price',
                  'is_refundable']

# class CreateCustomer(forms.ModelForm):
#     class Meta:
#         model = Customers
#         fields = ['customer_first_name', 'customer_last_name', 'customer_email', 'customer_date']

# class CreateCustomer(forms.ModelForm):
#     class Meta:
#         model = Customers
#         fields = ['customer_name', 'customer_phone', 'checkin', 'checkout']