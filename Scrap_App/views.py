from django.shortcuts import render
from requests_html import HTMLSession
from django.views import View

# Create your views here.


class News_Home_Page(View):
    def get(self, request):
        url = "https://www.indiatoday.in/india"
        url_1 = "https://www.indiatoday.in/india?page=1"
        url_2 = "https://www.indiatoday.in/india?page=2"
        url_3 = "https://www.indiatoday.in/india?page=3"
        url_4 = "https://www.indiatoday.in/india?page=4"
        url_5 = "https://www.indiatoday.in/india?page=5"
        url_6 = "https://www.indiatoday.in/india?page=6"
        session = HTMLSession()
        r = session.get(url)
        r_1 = session.get(url_1)
        r_2 = session.get(url_2)
        r_3 = session.get(url_3)
        r_4 = session.get(url_4)
        r_5 = session.get(url_5)
        r_6 = session.get(url_6)
        articles = r.html.find(".detail a, .pic img")
        article = r_1.html.find(".detail a, .pic img")
        article_2 = r_2.html.find(".detail a, .pic img")
        article_3 = r_3.html.find(".detail a, .pic img")
        article_4 = r_4.html.find(".detail a, .pic img")
        article_5 = r_5.html.find(".detail a, .pic img")
        article_6 = r_6.html.find(".detail a, .pic img")

        image = r.html.find('.pic img')
        context = {'articles':articles, 'article':article, 'article_2':article_2, 'article_3':article_3,
         'article_4':article_4, 'article_5':article_5, 'article_6':article_6, 'image':image}
        return render(request, 'Home_Page.html', context )


