from django.urls import path
from .views import MemberListView, MemberView

urlpatterns = [
    path('', MemberListView.as_view()),
    path('<str:member_id>/', MemberView.as_view()),
]
