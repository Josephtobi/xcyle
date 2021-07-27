from wasteprod.views import WasteOwnerList,WasteListAPIView,WasterOwnerDetail,WasteDetailAPIView,BidCreateAPIView
from django.urls import path


urlpatterns = [
    path('user', WasteOwnerList.as_view(),name='user'),
    path('user/<int:id>', WasterOwnerDetail.as_view(),name='user_detail'),
    path('', WasteListAPIView.as_view(),name='all'),
    path('<int:id>', WasteDetailAPIView.as_view(),name='detail'),
    path('<int:id>/comment', BidCreateAPIView.as_view(),name='post_comment'),
]