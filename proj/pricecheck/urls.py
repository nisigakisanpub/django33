from django.urls import path
from . import views

app_name = "pricecheck"

urlpatterns = [
    path("", views.index, name="index"),
    path("schedule/", views.schedule, name="schedule"),
    path("schedule/change_status", views.change_status, name="schedule_change_status"),
    path("fund/", views.fund, name="fund"),
    path(
        "pricecheck/<str:sec_type>/<str:fund_id>/<str:date_close>",
        views.pricecheck_transfer,
        name="pricecheck_transfer",
    ),
    path("pricecheck/dashboard/divlist/", views.dashboard_divlist, name="dashboard_divlist"),
]
