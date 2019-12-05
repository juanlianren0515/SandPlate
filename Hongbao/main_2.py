# encoding=utf-8
from pprint import pprint

import time

from Hongbao.Sub import get_product_info, send_all_product_to_all_qun
from Room.Sub import get_all_qq_win

if __name__ == '__main__':

	# 获取所有win
	h_list = get_all_qq_win()

	pprint([x[1] for x in h_list])

	ipt = input('上述是所有win，输入“确定”继续！')

	# time.sleep(60*60*2)

	if ipt == '确定':
		p_list = get_product_info(r'C:/Users\paul\Desktop\文案')

		while True:
			send_all_product_to_all_qun(
				qun_list_=[x[0] for x in h_list],
				product_list=p_list,
				text_st=0.5,
				pic_st=0.3,
				product_st=60*60*2)

