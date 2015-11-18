from .settings import PORTAL_URL

def students_proc(request):
    PORTAL_URL = request.build_absolute_uri
    return {'PORTAL_URL': PORTAL_URL}