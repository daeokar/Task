from django import forms

#-- creter the for 

class OrderForms(forms.Form):
    """ Create the form for the order """

    order_date = forms.DateTimeField()
    product = forms.CharField(max_length=100)
    user = forms.CharField(max_length=100)


