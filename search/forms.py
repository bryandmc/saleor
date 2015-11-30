from django import forms
from haystack.forms import FacetedSearchForm

class ProductSearchForm(FacetedSearchForm):
    """ My basic search form
    """
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control",
                                                                    "placeholder": "Search for..."}),)

    def no_query_found(self):
        print "no query found!!"
        return self.searchqueryset.all()

    
