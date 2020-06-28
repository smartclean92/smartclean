from django.urls import path,include
from dryclean import views
urlpatterns = [
    path('demo/',views.demoview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('home/',views.homeview.as_view()),
    path('page/',views.pageview.as_view()),
    path('homelaundry/',views.homelaundry.as_view()),
    path('ourblog/',views.ourblogview.as_view()),
    path('feedback/',views.feedbackview.as_view()),
    path('pages/',views.pagesview.as_view()),
    path('services/',views.servicesview.as_view()),
    path('pricing/',views.product_list),
    path('about1/',views.about1view.as_view()),
    path('form/',views.formview.as_view()),
    path('order/',views.orderview.as_view()),
    path('practice/',views.practiceview.as_view()),
    path('cartdetail/', views.cartdetailview.as_view()),
    path('detail/', views.cartdetailview.as_view()),
    path('insert',views.insert),
    path('insertorder',views.insertorder),
    path('payment/',views.paymentview.as_view()),
    path('login/',views.loginview.as_view()),
] 