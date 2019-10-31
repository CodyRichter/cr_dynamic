from django.conf import settings


#
# Allow for passing of site name to different HTML pages
def site_name(request):
    return {'SITE_NAME': settings.NAME}


#
# Allow for passing of site logo to different HTML pages
def logo_url(request):
    return {'LOGO_URL': settings.LOGO_URL}


#
# Allow for passing of site logo to different HTML pages
def allow_new_users(request):
    return {'ALLOW_NEW_USERS': settings.ALLOW_NEW_USERS}
