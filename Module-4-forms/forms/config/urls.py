from django.contrib import admin
from django.urls import path


from app.views import hub_page, Open_Page, Hey_You, Age_in_2050, Order, Codingbat_Hub, font_times, teen, xyz, centered_average

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Open_Page, name="home"),
    path("codinghub/", Codingbat_Hub, name="CBHub"),
    path("codinghub/warmup-2/font-times/", font_times, name="FONT"),
    path("codinghub/logic-2/no-teen-sum/", teen, name="TEEN"),
    path("codinghub/string-2/xyz-there", xyz, name="XYZ"),
    path("codinghub/list-2/centered-average", centered_average, name="AVERAGE"),
    path("function/", hub_page, name="hub"),
    path("function/hey/", Hey_You, name="HEY"),
    path("function/age_in_2050/", Age_in_2050, name="AGE"),
    path("function/order/", Order, name="ORDER"),
]