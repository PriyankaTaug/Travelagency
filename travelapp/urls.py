from django.urls import path
from .views import ContactpageView, FrontpageView,UdupiPage,murudeswarPage,mookambikaPage,shringeriPage,aboutPage

 
app_name = 'travelapp'

urlpatterns = [
    path('', FrontpageView.as_view(), name='frontpage'),  # Assign a URL route for the view
    path('contact/', ContactpageView.as_view(), name='ContactpageView'),  # Assign a URL route for the view
    path('Udupi/', UdupiPage.as_view(), name='UdupiPage'),  # Assign a URL route for the view
    path('murudeswar/', murudeswarPage.as_view(), name='murudeswarPage'),  # Assign a URL route for the view
    path('mookambika/', mookambikaPage.as_view(), name='mookambikaPage'),  # Assign a URL route for the view
    path('shringeriPage/', shringeriPage.as_view(), name='shringeriPage'),  # Assign a URL route for the view
    path('aboutPage/', aboutPage.as_view(), name='aboutPage'),  # Assign a URL route for the view
]

