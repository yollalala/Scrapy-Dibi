import scrapy

class DibiSpider(scrapy.Spider):
	name = "no_detail"

	def start_requests(self):
		dibi_url = 'http://bnpb.cloud/dibi/xdibi/xdibi_list?wilayah=1&waktu=1&jenis=1&wil2=&&&pp=11&th1=2013&th2=2017&bl1=&bl2=&tg1=&tg2=&jn1=&jn2=&jn3=&jflag=2&start='
		urls = [
			dibi_url+str(x) for x in range(0, 10080, 10)
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for row in response.xpath('//table[@id="table-example"]/tbody/tr[position()>1]'):
			no_obj = {}
			no_obj['no'] = row.xpath('td[10]/button[@id="btnFormView"]/@onclick').extract_first().strip()[12:-1]
			yield no_obj


	
