from django import forms
from restaurant.models import Restaurant

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'local_category','food_category_1st','food_category_2nd', 'dining_food_cate_1',
                  'dining_food_cate_2', 'isParking', 'isValet', 'isPet',
                  'isPackaging', 'isReservation', 'address', 'phone', 'menu1', 'price1',
                  'menu2', 'price2', 'menu_url','mon_business', 'mon_breaktime',
                  'tues_business', 'tues_breaktime', 'wed_business', 'wed_breaktime',
                  'thurs_business', 'thurs_breaktime', 'fri_business', 'fri_breaktime',
                  'sat_business', 'sat_breaktime', 'sun_business', 'sun_breaktime',
                  'imgfile_1', 'imgfile_2', 'imgfile_3', 'closest_parking_name', 'closest_parking_address',
                  ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'local_category': forms.TextInput(attrs={'class': 'form-control'}),
            'food_category_1st': forms.TextInput(attrs={'class': 'form-control'}),
            'food_category_2nd': forms.TextInput(attrs={'class': 'form-control'}),
            'dining_food_cate_1': forms.TextInput(attrs={'class': 'form-control'}),
            'dining_food_cate_2': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'menu1': forms.TextInput(attrs={'class': 'form-control'}),
            'price1': forms.TextInput(attrs={'class': 'form-control'}),
            'menu2': forms.TextInput(attrs={'class': 'form-control'}),
            'price2': forms.TextInput(attrs={'class': 'form-control'}),
            'menu_url': forms.TextInput(attrs={'class': 'form-control'}),
            'mon_business': forms.TextInput(attrs={'class': 'form-control'}),
            'mon_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'tues_business': forms.TextInput(attrs={'class': 'form-control'}),
            'tues_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'wed_business': forms.TextInput(attrs={'class': 'form-control'}),
            'wed_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'thurs_business': forms.TextInput(attrs={'class': 'form-control'}),
            'thurs_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'fri_business': forms.TextInput(attrs={'class': 'form-control'}),
            'fri_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'sat_business': forms.TextInput(attrs={'class': 'form-control'}),
            'sat_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'sun_business': forms.TextInput(attrs={'class': 'form-control'}),
            'sun_breaktime': forms.TextInput(attrs={'class': 'form-control'}),
            'imgfile_1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imgfile_2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imgfile_3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'closet_parking_name': forms.TextInput(attrs={'class': 'form-control'}),
            'closet_parking_address': forms.TextInput(attrs={'class': 'form-control'}),


        }
            #forms.textinput - 위젯 크기 옆으로 크게 설정, rows는 원하는 줄만큼 설정
