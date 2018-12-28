import scrapy


class CricinfoSpider(scrapy.Spider):
    name = "cricinfo2"
    start_urls = [
        'http://www.espncricinfo.com/scores'
    ]

    def parse(self, response):

        for match in response.css('div.cscore.cscore--live.cricket.cscore--watchNotes'):
            link = match.css('div.cscore_link.cscore_link--button a::attr(href)').extract_first()
            yield response.follow(link ,callback = self.parse_inside)



    def parse_inside(self,response):
        yield{
            'match':response.css('div.cscore_info-overview::text').extract_first()
            }
        for commentary in response.css('article.sub-module.match-commentary.cricket'):
            for each in commentary.css('div.commentary-item'):
                over = each.css('div.time-stamp::text').extract_first()
                desc = each.css('div.description::text').extract_first()
                if ((over is not None) and (desc is not None)):
                    yield{
                        'over' : over,
                        'commentary': desc
                        }
            
