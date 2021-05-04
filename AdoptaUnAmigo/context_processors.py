from .models import MoreinfoUsers

def add_variable_to_context(request):
    if request.user.is_active:
        moreinfo = MoreinfoUsers.objects.get_or_create(user_id=request.user.id)
        moreinfo = MoreinfoUsers.objects.get(user_id=request.user.id)
        return {
        'moreinfo': moreinfo
        }
    return{
        'moreinfo': 'hola'
    }