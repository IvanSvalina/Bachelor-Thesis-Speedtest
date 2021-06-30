from django.urls import path
from .import views

urlpatterns=[path("savemeas",views.savemeas,name="savemeas"),
            path("measureuspeed",views.measureuspeed,name="measureuspeed"),
            path("measureping",views.measureping,name="measureping"),
            path("history",views.history,name="history"),
            path("getweekdatahistory",views.getweekdatahistory,name="getweekdatahistory"),
            path("getmonthdatahistory",views.getmonthdatahistory,name="getmonthdatahistory"),
            path("getdaydatahistory",views.getdaydatahistory,name="getdaydatahistory"),
            path("getalldatahistory",views.getalldatahistory,name="getalldatahistory"),
            path("deletemention",views.deletemention,name="deletemention")
            ]
#urlpatterns=[path("",views.ping,name="ping")]
#urlpatterns=[path("",views.d_speed1,name="d_speed1")]
#urlpatterns=[path("",views.measureping,name='measureping')]

