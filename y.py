import scrapy
from scrapy import Request
import json,csv

class ySpider(scrapy.Spider):
    name = 'y'
    def start_requests(self):
        url='https://45bwzj1sgc-3.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%3B%20JS%20Helper%20(3.1.0)&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NDYzYmNmMTRjYzU4MDE0ZWY0MTVmMTNiYzcwYzMyODFlMjQxMWI5YmZkMjEwMDAxMzE0OTZhZGZkNDNkYWZjMHJlc3RyaWN0SW5kaWNlcz0lNUIlMjJZQ0NvbXBhbnlfcHJvZHVjdGlvbiUyMiU1RCZ0YWdGaWx0ZXJzPSU1QiUyMiUyMiU1RCZhbmFseXRpY3NUYWdzPSU1QiUyMnljZGMlMjIlNUQ%3D'
        seasons = ['W21', 'S20', 'W20', 'S19', 'W19', 'S18', 'W18', 'S17', 'W17', 'IK12', 'S16', 'W16', 'S15', 'W15', 'S14','W14',
                   'S13', 'W13', 'S12', 'W12', 'S11', 'W11', 'S10', 'W10', 'S09', 'W09', 'S08', 'W08', 'S07', 'W07', 'S06', 'W06',
                   ]
        bodies=['{"requests":[{"indexName":"YCCompany_production","params":"hitsPerPage=1000&query=&page=0&facets=%5B%22top_company%22%2C%22isHiring%22%2C%22nonprofit%22%2C%22batch%22%2C%22industries%22%2C%22subindustry%22%2C%22status%22%2C%22regions%22%5D&tagFilters=&facetFilters=%5B%5B%22batch%3A'+season+'%22%5D%5D"},{"indexName":"YCCompany_production","params":"hitsPerPage=1&query=&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=batch"}]}' for season in seasons]
        for body in bodies:
            yield scrapy.Request(url = url, method = 'POST', body = body, callback = self.parse)

    def parse(self, response):
        companies = json.loads(response.text)['results'][0]['hits']
        with open('y.json','a') as f:
            for c in companies:
                json.dump({'name':c['name'],
                           'moto':c['one_liner'],
                           'batch':c['batch'],
                           'description':c['description'],
                           'former_names':c['former_names'],
                           'id':c['id'],
                           'industries':c['industries'],
                           'industry':c['industry'],
                           'isHiring':c['isHiring'],
                           'location':c['location'],
                           'nonprofit':c['nonprofit'],
                           'objectID':c['objectID'],
                           'regions':c['regions'],
                           'small_logo_thumb_url':c['small_logo_thumb_url'],
                           'status':c['status'],
                           'subindustry':c['subindustry'],
                           'tags':c['tags'],
                           'team_size':c['team_size'],
                           'top_company':c['top_company'],
                           'website':c['website']}, f, indent = 4)
