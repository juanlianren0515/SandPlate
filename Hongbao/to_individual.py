# encoding=utf-8
from pprint import pprint

from Hongbao.Sub import get_product_info, send_all_product_to_all_qun
from Room.Sub import get_all_qq_win

if __name__ == '__main__':

	# 获取所有win
	h_list = get_all_qq_win()

	pprint([x[1] for x in h_list])

	ipt = input('上述是所有win，确定继续？')

	if ipt == '继续':
		p_list = get_product_info(r'C:/Users\paul\Desktop\文案')

		send_all_product_to_all_qun(
			qun_list_=h_list,
			product_list=p_list,
			text_st=0.2,
			pic_st=1.5,
			product_st=0)
