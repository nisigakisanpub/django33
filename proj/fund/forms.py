from django import forms


class QueryForm(forms.Form):
    fund_id = forms.CharField(label="Fund ID", max_length=4, required=True)
    as_of_date = forms.DateField(
        label="As of Date", required=True, input_formats=["%Y-%m-%d"]
    )
