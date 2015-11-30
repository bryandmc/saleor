from purl import URL
import re
from collections import OrderedDict

class FacetMunger(object):
    def __init__(self, facet_data, url):
        print "init"
        print facet_data
        self.url = url
        self.facet_data = facet_data
        self.selected_facets = self.clean_pre_selected(URL(url))

    def clean_pre_selected(self, pre_selected):
        print dir(pre_selected)
        pre = pre_selected.query_param('selected_facets', as_list=True)
        if pre:
            pre = [ a.split(':') for a in pre ]
            pre = [ (a[0].split('_exact')[0], a[1]) for a in pre ]
            return pre
        else:
            return []

    def clean_facets(self):
        facets = {}
        for facet_name, name_count in self.facet_data.items():
            sub_field = []
            for name, count in name_count:
                facet_temp = Facet(facet_name, name, count)
                if (facet_name, name) in self.selected_facets:
                    print "selected!"
                    facet_temp.deselect_url = facet_temp.deselect(self.url)
                    facet_temp.selected=True
                sub_field.append(facet_temp)
            print "*" * 10
            sub_field.sort(key=lambda x: x.name, reverse=True)
            facets[facet_name] = sub_field
        #print facets
        return facets

class Facet(object):
    def __init__(self, facet_name, key, count, selected=False):
        self.facet_name = facet_name
        self.key = key
        self.count = count
        self.name = key
        self.selected = selected
        self.deselect_url = ""

    def deselect(self, url):
        url = URL(url)
        field_name = '%s_exact' % self.facet_name
        url = url.remove_query_param('selected_facets', '%s:%s' % (field_name, self.key))
        self.selected = False
        return url

    def select(self, url):
        print "SELECTED!!"
        url = URL(url)
        field_name = '%s_exact' % self.facet_name
        url = url.append_query_param('selected_facets', '%s:%s' % (field_name, self.key))
        self.selected = True
        return url

    def __str__(self):
        return self.name + ": " + str(count)

    def __repr__(self):
        return str(type(self)) + str(self.key) + ": " + str(self.count)
