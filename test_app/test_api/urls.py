from django.urls import path
from test_api.views import ParticipantCreateView, IQTestResultCreateView, EQTestResultCreateView, TestResultsView

urlpatterns = [
    path('test/', ParticipantCreateView.as_view(), name='test-create'),
    path('iq_result/', IQTestResultCreateView.as_view(), name='iq-result-create'),
    path('eq_result/', EQTestResultCreateView.as_view(), name='eq-result-create'),
    path('test_results/<str:login>/', TestResultsView.as_view(), name='test-results'),
]
