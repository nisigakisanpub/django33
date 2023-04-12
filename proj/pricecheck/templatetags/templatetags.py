from django import template

register = template.Library()

# sec_type(銘柄種別)
# 0全部　　　all
# 1国内株式　
# 2海外株式　
# 3国内債券　
# 4海外債券　
# 5国内投資証券
# 6海外投資証券

@register.filter
def to_name_jp_sec_type(value):
    if value==0:
        return "全部"
    if value==1:
        return "国内株式"
    if value==2:
        return "海外株式"
    if value==3:
        return "国内債券"
    if value==4:
        return "海外債券"
    if value==5:
        return "国内投資証券"
    if value==6:
        return "海外投資証券"
    return ""

@register.filter
def to_name_en_sec_type(value):
    if value==0:
        return "all"
    return ""
