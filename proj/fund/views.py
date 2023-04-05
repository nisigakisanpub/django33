from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime
from .forms import QueryForm


def index(request):
    return redirect("fund:schedule")


def schedule(request):
    if request.method == "POST":
        pass

    schedules = list()
    schedules = [
        {
            "fund_id": "9998",
            "fund_name": "ファンド9998",
            "date_close": datetime.datetime(2023, 1, 23),
            "sec_type": "domestic_stock",
            "sec_type_jp": "内株",
        },
        {
            "fund_id": "9998",
            "fund_name": "ファンド9998",
            "date_close": datetime.datetime(2023, 1, 23),
            "sec_type": "domestic_fund",
            "sec_type_jp": "内債",
        },
    ]
    context = dict()
    context["schedules"] = schedules

    return render(request, "fund/schedule.html", context)


def change_status(request):
    pass


def fund(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            fund_id = form.cleaned_data["fund_id"]
            as_of_date = form.cleaned_data["as_of_date"]
        context = {"form": form}
        return render(request, "fund/fund.html", context)
    else:
        form = QueryForm()
        context = {"form": form}
        return render(request, "fund/fund.html", context)


def fund_transfer(request, sec_type, fund_id, date_close):
    as_of_date = datetime.datetime.strptime(date_close, "%Y-%m-%d").date()
    initial_dict = dict(fund_id=fund_id, as_of_date=as_of_date)
    form = QueryForm(initial=initial_dict)

    context = {"form": form}

    return render(request, "fund/fund.html", context)


def dashboard_divlist(request):
    d_div = [{"fund_id": 9998}, {"fund_id": 9998}]

    context = {"d_div": d_div}

    return render(request, "fund/dashboard_divlist.html", context)
