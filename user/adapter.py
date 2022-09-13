from allauth.account.adapter import DefaultAccountAdapter


# AbstractUser를 사용했을 때 nickname,introduction 등의 정보가 저장되도록 한다.
class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        user.introduction = data.get('introduction')
        user.profile_image = data.get('profile_image')
        user.save()
        return user
