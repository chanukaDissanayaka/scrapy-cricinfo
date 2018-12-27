import scrapy


class CricinfoSpider(scrapy.Spider):
    name = "cricinfo1"
    start_urls = [
        'http://www.espncricinfo.com/scores'
    ]

    def parse(self, response):

        for match in response.css('div.cscore.cscore--live.cricket.cscore--watchNotes'):
            yield{
            'live matches':match.css('div.cscore_info-overview::text').extract_first()
            }
            for team in match.css('ul.cscore_competitors'):
                yield{
                    'team':team.css('span.cscore_name.cscore_name--long::text').extract_first(),
                    'score':team.css('div.cscore_score::text').extract_first(),
                    'ovres':team.css('span.cscore_overs::text').extract_first()
                    }
            
        for match in response.css('div.cscore--final.cricket.cscore--home-winner.cscore--watchNotes'):
            yield{
                'results':match.css('div.cscore_info-overview::text').extract_first()
            }
            for team in match.css('ul.cscore_competitors'):
                yield{
                    'team':team.css('span.cscore_name.cscore_name--long::text').extract_first(),
                    'score':team.css('div.cscore_score::text').extract_first(),
                    'ovres':team.css('span.cscore_overs::text').extract_first()
                    }

        for match in response.css('div.cscore--final.cricket.cscore--away-winner.cscore--watchNotes'):
            yield{
                'results':match.css('div.cscore_info-overview::text').extract_first()
                }

        for match in response.css('div.cscore.cscore--pregame.cricket.cscore--watchNotes'):
            yield{
                'pregame':match.css('div.cscore_info-overview::text').extract_first()
                }

