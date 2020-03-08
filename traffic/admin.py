from django.contrib import admin
from traffic.models import Posts,Comments,User,Reactions

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(User)
admin.site.register(Reactions)
