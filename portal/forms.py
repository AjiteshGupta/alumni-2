from django.forms import ModelForm
import django.forms as forms

from .models import User, UserProfile, Qualification, Address, WorkExperience


class User_BasicInfoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email_1', 'date_of_birth', 'gender']


class User_MiscInfoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email_2', 'phone_1', 'phone_2', 'marital_status',
                  'blood_group', 'photograph', 'nationality',
                  'scope_permanent_address', # removed address themselves
                  'scope_current_address']


class User_SocialLinksForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['link_facebook', 'scope_facebook',
                  'link_twitter', 'scope_twitter',
                  'link_linkedin', 'scope_linkedin',
                  'link_skype', 'scope_skype',
                  'link_github', 'link_blog', 'link_website']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        # set user_roll_no as hidden


class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'


class WorkExperienceForm(forms.Form):
    employer = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    sector = forms.CharField()
    designation = forms.CharField()
    founder = forms.BooleanField()
    # address_pk = forms.IntegerField(widget=forms.HiddenInput())
    address_pk = forms.IntegerField()


class WorkExperienceModelForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'
