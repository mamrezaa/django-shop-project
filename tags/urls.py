from django.urls import path
from tags.api_views import (
    tag_list_api,
    tag_detail_api,
    create_tag_api,
    update_tag_api,
    delete_tag_api
)

app_name = 'tags'

urlpatterns = [
    path('api/tags/', tag_list_api, name='tag_list_api'),
    path('api/tags/<int:tag_id>/', tag_detail_api, name='tag_detail_api'),
    path('api/tags/create/', create_tag_api, name='create_tag_api'),
    path('api/tags/<int:tag_id>/update/', update_tag_api, name='update_tag_api'),
    path('api/tags/<int:tag_id>/delete/', delete_tag_api, name='delete_tag_api'),
]