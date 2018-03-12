import scrapy
import json
from ast import literal_eval 

class DibiSpider(scrapy.Spider):
	name = "dibi"

	def start_requests(self):

		dibi_url = 'http://bnpb.cloud/dibi/xdibi/xdibi_list?wilayah=1&waktu=1&jenis=1&wil2=&&&pp=11&th1=2013&th2=2017&bl1=&bl2=&tg1=&tg2=&jn1=&jn2=&jn3=&jflag=2&start='

		urls = [
			dibi_url+str(x) for x in range(0, 10080, 10)
		]
		
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		# print(response.xpath('//table[@id="table-example"]/tbody/tr[position()>1]/td'))
		# result['Text'] = response.xpath('//table[@id="table-example"]/tbody//text()').extract();
		# yield result
		with open('detail3.txt') as f:
			dict_detail = literal_eval(f.read())

		for row in response.xpath('//table[@id="table-example"]/tbody/tr[position()>1]'):
			result = {}
			result['no'] = row.xpath('td[1]//text()').extract_first().strip()
			result['kib'] = ''.join([item.strip() for item in row.xpath('td[2]/span//text()').extract()])
			result['kejadian'] = row.xpath('td[3]//text()').extract_first().strip()
			result['tanggal'] = row.xpath('td[4]//text()').extract_first().strip()
			result['meninggal'] = row.xpath('td[5]//text()').extract_first().strip()
			result['lukaluka'] = row.xpath('td[6]//text()').extract_first().strip()
			result['hilang'] = row.xpath('td[7]//text()').extract_first().strip()
			result['menderita'] = row.xpath('td[8]//text()').extract_first().strip()
			result['mengungsi'] = row.xpath('td[9]//text()').extract_first().strip()
			# result['Kontrol'] = row.xpath('td[10]//text()').extract_first().strip()
			result['detail'] = dict_detail[row.xpath('td[10]/button[@id="btnFormView"]/@onclick').extract_first().strip()[12:-1]]
			# result['Detail'] = detail_extraction_helper(id_detail)

			yield result


	# def detail_extraction_helper(id_detail):
	# 	detail_url = "http://bnpb.cloud/dibi/xdibi/read/" + id_detail
	# 	detail = {}
	# 	return detail


		# extract_response = response.css("td#td").extract()
		# print(extract_response)
		# print("length of the list:", len(extract_response))

		# for i in range(0, len(extract_response), 10):
		# 	result = {}
		# 	result['No'] = extract_response[i+0]
		# 	result['KIB'] = extract_response[i+1]
		# 	result['Kejadian'] = extract_response[i+2]
		# 	result['Tanggal'] = extract_response[i+3]
		# 	result['Meninggal'] = extract_response[i+4]
		# 	result['Luka-luka'] = extract_response[i+5]
		# 	result['Hilang'] = extract_response[i+6]
		# 	result['Menderita'] = extract_response[i+7]
		# 	result['Mengungsi'] = extract_response[i+8]
		# 	result['Kontrol'] = extract_response[i+10]

		# 	yield result
		
		# page = response.url.split("=")[-1];
		# filename = 'dibi-%s.json' % page
		# with open(filename, 'wb') as f:
		# 	f.write(list_result)
		# self.log('Saved file %s' % filename)

	
