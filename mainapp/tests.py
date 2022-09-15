from django.test import TestCase
from django.urls import reverse, resolve
from .views import indexView, aboutView, podcasterslugView, logoutView
from .models import PodcastModel, PodcasterModel

class TestView(TestCase):
    # test IndexView...
    def test_project_list_GET(self):
        index_url = reverse('main:index')
        response = self.client.get(index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    # test URLS...
    def test_index_resolves(self):
        url = reverse('main:index')
        self.assertEquals(resolve(url).func, indexView)
        
    def test_about_resolves(self):
        url = reverse('main:about')
        self.assertEquals(resolve(url).func, aboutView)
        
    def test_podcastersPodcast_resolves(self):
        url = reverse('main:slug', args=['slg']) 
        self.assertEquals(resolve(url).func, podcasterslugView)
        
    def test_logout_resolves(self):
        url = reverse('main:logout')
        self.assertEquals(resolve(url).func, logoutView)
    
    # test Models...
    def setUp(self): 
        PodcastModel.objects.create(
            title = 'podcast1',
            content = 'test content',
            slug = 'podcastslg',
            url = 'http://www.largesound.com/ashborytour/sound/AshboryBYU.mp3',
            pic = 'test.png'
        )
        PodcasterModel.objects.create(
            name = 'test podcaster',
            pic = 'podcaster.png',
            slug = 'podcastertest',
            position = 4
        )