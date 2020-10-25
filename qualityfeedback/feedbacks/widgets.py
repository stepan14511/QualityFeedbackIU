from django import forms
from django.utils.safestring import mark_safe
import re

class RangeSlider(forms.TextInput):
    def __init__(self, minimum, maximum, step, elem_name, *args, **kwargs):
        widget = super(RangeSlider, self).__init__(*args, **kwargs)
        self.minimum = str(minimum)
        self.maximum = str(maximum)
        self.step = str(step)
        self.elem_name = str(elem_name)

    def render(self, name, value, attrs=None, renderer=None):
        s = super(RangeSlider, self).render(name, value, attrs)
        self.elem_id = re.findall(r'id_([A-Za-z0-9_\./\\-]*)"', s)[0]
        html = """<div id=\"slider-""" + self.elem_id + """\">
                <p>
                """+self.elem_name+"""
                </p>
                <input type="range" min=\""""+self.minimum+ \
                    """\" max=\""""+self.maximum+ \
                    """\" value=\""""+self.maximum+ \
                    """\" step=\"""" + self.step + \
                    """\"  id=\""""+self.elem_id+"""\">
                <span id=\"out-"""+self.elem_id+ \
                    """\" style="font-weight:bold;color:red">-1</span>
                </div>
                <script>
                    var slider = document.getElementById(\""""+self.elem_id+"""\");
                    var output = document.getElementById(\"out-"""+self.elem_id+"""\");
                    output.innerHTML = slider.value;
                    
                    slider.ouinput = function(){
                        output.innerHTML = this.value;
                    }
                    
                </script>
                """
        return mark_safe(s + html)
