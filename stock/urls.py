from django.urls import path

from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('Registration/',views.Registration,name='Registration'),
    path('login/admin1/',views.admin1,name='admin1'),
    path('login/customer/',views.customer,name='customer'),
    path('About/',views.about,name='about'),
    path('login/admin1/add',views.add,name='add'),
    path('login/admin1/delete',views.delete,name='delete'),
    path('login/admin1/available',views.available,name='available'),
    path('login/admin1/update',views.update,name='update'),
    #path('loogin/admin1/update/find',)
    path('login/admin1/update/modify',views.modify,name='modify'),
    path('login/customer/Info',views.Info,name='Info'),
    path('login/customer/order',views.order,name='order'),
    path('login/admin1/customerdetail',views.customerdetail,name='customerdetail'),
    path('login/customer/find/(<id_no>\w+)',views.find,name='find'),
    path('login/customer/show',views.show,name='show'),
    path('login/customer/delorder/(<id_no>\w+)',views.delorder,name='delorder'),
    path('login/admin1/orderdetail',views.orderdetail,name='orderdetail'),
    path('login/admin1/search',views.search,name='search'),
    path('login/customer/history',views.history,name='history'),
    path('login/customer/serachhistory',views.serachhistory,name='serachhistory'),
    path('login/admin1/view',views.view,name='view'),


    
]
