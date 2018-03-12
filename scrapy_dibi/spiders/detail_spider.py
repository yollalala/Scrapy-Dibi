import scrapy
import json

class DibiSpider(scrapy.Spider):
	name = "detail"
	list_no_detail = []



	def start_requests(self):
		with open('no_detail.json') as json_data:
			list_no_detail = json.load(json_data)

		detail_url = "http://bnpb.cloud/dibi/xdibi/read/"
		urls = [
			detail_url+no['no'] for no in list_no_detail
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	

	def parse(self, response):

		def parsing_helper(result):
			if result == None:
				return ""
			else:
				return result.strip()


		result_detail = {}
		# result_detail['no'] = response.url.split("/")[-1]
		
		# table 1
		result1 = {}
		result1['kib'] = parsing_helper(response.xpath('//table[1]//h2//text()').extract_first())
		result1['propinsi'] = parsing_helper(response.xpath('//table[1]//tr[2]//td[2]/text()').extract_first())
		result1['kabupaten_kota'] = parsing_helper(response.xpath('//table[1]//tr[3]/td[2]/text()').extract_first())
		result1['kejadian'] = parsing_helper(response.xpath('//table[1]//tr[4]/td[2]/text()').extract_first())
		result1['waktu'] = parsing_helper(response.xpath('//table[1]//tr[5]/td[2]/text()').extract_first())
		result1['wilayah_terdampak'] = parsing_helper(response.xpath('//table[1]/tr[6]/td[2]/text()').extract_first())
		result1['penyebab'] = parsing_helper(response.xpath('//table[1]/tr[7]/td[2]/text()').extract_first())
		result1['kronologis'] = parsing_helper(response.xpath('//table[1]/tr[8]/td[2]/text()').extract_first())
		result1['kerugian'] = parsing_helper(response.xpath('//table[1]/tr[9]/td[2]/text()').extract_first())
		result1['bantuan_bnpd'] = parsing_helper(response.xpath('//table[1]/tr[10]/td[2]/text()').extract_first())
		result1['bantuan_kementrian_lembaga'] = parsing_helper(response.xpath('//table[1]/tr[11]/td[2]/text()').extract_first())
		result1['bantuan_pemerintah_provinsi'] = parsing_helper(response.xpath('//table[1]/tr[12]/td[2]/text()').extract_first())
		result1['bantuan_lainnya'] = parsing_helper(response.xpath('//table[1]/tr[13]/td[2]/text()').extract_first())
		result1['keterangan'] = parsing_helper(response.xpath('//table[1]/tr[14]/td[2]/text()').extract_first())
		result1['sumber'] = parsing_helper(response.xpath('//table[1]/tr[15]/td[2]/text()').extract_first())
		
		# table 2
		result2 = {}
		result2['waktu_update'] = parsing_helper(response.xpath('//table[2]//td[1]/text()').extract_first())
		result2['meninggal_hilang'] = parsing_helper(response.xpath('//table[2]//td[2]/text()').extract_first())
		result2['luka_luka'] = parsing_helper(response.xpath('//table[2]//td[3]/text()').extract_first())
		result2['terdampak_mengungsi'] = parsing_helper(response.xpath('//table[2]//td[4]/text()').extract_first())
		result2['rusak_ringan'] = parsing_helper(response.xpath('//table[2]//td[5]/text()').extract_first())
		result2['rusak_sedang'] = parsing_helper(response.xpath('//table[2]//td[6]/text()').extract_first())
		result2['rusak_berat'] = parsing_helper(response.xpath('//table[2]//td[7]/text()').extract_first())

		# table 3
		result3 = {}
		result3['waktu_update'] = parsing_helper(response.xpath('//table[3]//td[1]/text()').extract_first())
		result3['dampak'] = parsing_helper(response.xpath('//table[3]//td[2]/text()').extract_first())
		result3['upaya'] = parsing_helper(response.xpath('//table[3]//td[3]/text()').extract_first())
		result3['kendala'] = parsing_helper(response.xpath('//table[3]//td[4]/text()').extract_first())
		result3['kondisi'] = parsing_helper(response.xpath('//table[3]//td[5]/text()').extract_first())
		result3['kebutuhan'] = parsing_helper(response.xpath('//table[3]//td[6]/text()').extract_first())
		result3['RTL'] = parsing_helper(response.xpath('//table[3]//td[7]/text()').extract_first())

		detail = {}
		detail['table_1'] = result1
		detail['table_2'] = result2
		detail['table_3'] = result3

		result_detail[response.url.split("/")[-1]] = detail

		yield result_detail



			# result = {}
			# result['no'] = row.xpath('td[1]//text()').extract_first().strip()
			# result['kib'] = ''.join([item.strip() for item in row.xpath('td[2]/span//text()').extract()])
			# result['kejadian'] = row.xpath('td[3]//text()').extract_first().strip()
			# result['tanggal'] = row.xpath('td[4]//text()').extract_first().strip()
			# result['meninggal'] = row.xpath('td[5]//text()').extract_first().strip()
			# result['lukaluka'] = row.xpath('td[6]//text()').extract_first().strip()
			# result['hilang'] = row.xpath('td[7]//text()').extract_first().strip()
			# result['menderita'] = row.xpath('td[8]//text()').extract_first().strip()
			# result['mengungsi'] = row.xpath('td[9]//text()').extract_first().strip()
			# # result['Kontrol'] = row.xpath('td[10]//text()').extract_first().strip()
			# result['detail'] = row.xpath('td[10]/button[@id="btnFormView"]/@onclick').extract_first().strip()[12:-1]
			# # result['Detail'] = detail_extraction_helper(id_detail)

			# yield result

	
