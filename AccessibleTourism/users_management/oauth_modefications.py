from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount


class UserAccountAdapter(DefaultSocialAccountAdapter):

    def new_user(self, request, sociallogin):
        user = super(UserAccountAdapter, self).new_user(request, sociallogin)
        # user.save()
        # social_account = SocialAccount.objects.filter(user=user).first()
        # platform_user = User.objects.filter(email = user.email,tenant = request.tenant ).first()
        # platform_user.first_name = social_account.extra_data['properties']['nickname']
        # platform_user.user_image = social_account.extra_data['properties']['profile_image']
        # platform_user.save()