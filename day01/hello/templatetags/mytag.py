from django import template
register = template.Library()
@register.filter
def test(x,y): # 接收两个参数
    return int(x)*2+int(y)