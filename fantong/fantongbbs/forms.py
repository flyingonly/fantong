from django import forms
from .models import BBSPost, BBSUser
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = BBSPost
        fields = ('PContent',)

class IndexPostForm(forms.ModelForm):
    LOCATION_CHOICE = (
        (u'海淀区', u'海淀区'),
        (u'朝阳区', u'朝阳区'),
        (u'东城区', u'东城区'),
        (u'西城区', u'西城区'),
        (u'丰台区', u'丰台区'),
        (u'石景山区', u'石景山区'),
        (u'大兴区', u'大兴区'),
        (u'通州区', u'通州区'),
        (u'昌平区', u'昌平区'),
        (u'房山区', u'房山区'),
        (u'顺义区', u'顺义区'),
        (u'门头沟区', u'门头沟区'),
        (u'怀柔区', u'怀柔区'),
        (u'平谷区', u'平谷区'),
        (u'延庆县', u'延庆县'),
        (u'密云县', u'密云县'),
    )
    CLASS_CHOICE = (
        (u'火锅', u'火锅'),
        (u'自助餐', u'自助餐'),
        (u'咖啡厅', u'咖啡厅'),
        (u'烧烤', u'烧烤'),
        (u'面包', u'面包'),
        (u'甜点', u'甜点'),
        (u'韩国料理', u'韩国料理'),
        (u'日本菜', u'日本菜'),
        (u'西餐', u'西餐'),
        (u'小吃快餐', u'小吃快餐'),
        (u'北京菜', u'北京菜'),
        (u'江浙菜', u'江浙菜'),
        (u'粤菜', u'粤菜'),
        (u'清真菜', u'清真菜'),
        (u'素菜', u'素菜'),
        (u'川菜', u'川菜'),
        (u'新疆菜', u'新疆菜'),
        (u'西北菜', u'西北菜'),
        (u'海鲜', u'海鲜'),
        (u'东南亚菜', u'东南亚菜'),
        (u'家常菜', u'家常菜'),
        (u'云南菜', u'云南菜'),
        (u'贵州菜', u'贵州菜'),
        (u'鲁菜', u'鲁菜'),
        (u'湖北菜', u'湖北菜'),
        (u'东北菜', u'东北菜'),
        (u'湘菜', u'湘菜'),
        (u'其他', u'其他'),
    )
    PRICE_CHOICE = (
        (u'50以下', u'50以下'),
        (u'50-100', u'50-100'),
        (u'100-300', u'100-300'),
        (u'300以上', u'300以上'),
    )
    PTagLocation = forms.ChoiceField(choices=LOCATION_CHOICE)
    PTagClass = forms.ChoiceField(choices=CLASS_CHOICE)
    PTagPrice = forms.ChoiceField(choices=PRICE_CHOICE)
    class Meta:
        model = BBSPost
        fields = ('PTitle', 'PContent', 'PTagLocation', 'PTagClass', 'PTagPrice','PKeywords')



class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(label='OLD PASSWORD', widget=forms.PasswordInput)
    new_pwd = forms.CharField(label='NEW PASSWORD', widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(label='CONFIRM', widget=forms.PasswordInput)

    def pwd_validate(self, p1, p2):
        return p1 == p2
