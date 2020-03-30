from django.contrib import admin
from traffic.models import Posts, Comments, UserProfile

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(UserProfile)

