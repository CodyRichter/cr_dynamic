from django.conf import settings # import the settings file


#
# Allow for passing of site name to different HTML pages
def site_name(request):
    return {'SITE_NAME': settings.NAME}
