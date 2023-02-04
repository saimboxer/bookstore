from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-book/', Add_Book.as_view(), name='add-book'),
    path('delete-book/', Delete_Book.as_view(), name='delete-book'),
    path('edit-book/<int:id>/', Edit_Book.as_view(), name='edit-book'),
    path('attribute', AttributeList.as_view(), name='attribute'),
    path('add-attribute/', Add_Attribute.as_view(), name='add-attribute'),
    path('edit-attribute/<int:id>/', Edit_Attribute.as_view(), name='edit-attribute'),
    path('delete-attribute/', Delete_Attribute.as_view(), name='delete-attribute'),
    path('attribute-value/', AttributeValueList.as_view(), name='attribute-value'),
    path('addattribute-value/', Add_AttributeValue.as_view(), name='addattribute-value'),
    path('edit-attribute-value/<int:id>/', Edit_Attributevalue.as_view(), name='edit-attribute-value'),
    path('delete-attributevalue/', Delete_Attributevalue.as_view(), name='delete-attributevalue'),

]

