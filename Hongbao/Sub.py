# encoding=utf-8

"""
推广文件夹中的东西
"""
import glob
import os
import time

from Text.Material import note_to_individual, add_qun_note
from Room.Sub import get_all_win_by_name
from SendMsgByQQ.QQGUI import send_qq_hwnd_click_string, send_qq_pic_hwnd_click_string, send_qq_pic
import codecs

def get_product_info(root_url):

    """
    获取产品信息表
    :param root_url:
    :return:
    """

    # 存储结果
    product_list = []

    # 遍历其下的文件夹（商品）
    fs = os.listdir(root_url)

    for product_path_rela in fs:

        # 去除模板
        if product_path_rela == '模板':
            continue

        product_path_abs = os.path.join(root_url, product_path_rela)

        if os.path.exists(product_path_abs + '/文本.txt'):

            # 获取购买关键字
            try:
                with open(product_path_abs + '/文本.txt', 'r') as f:
                    buy_key = f.read()
                    buy_key =buy_key.replace('復製评论', '復製这一段话')

            except Exception as e:
                with open(product_path_abs + '/文本.txt', 'r', encoding='utf-8') as f:
                    buy_key = f.read()
                    buy_key =buy_key.replace('復製评论', '復製这一段话')
        else:
            buy_key = ''

        # 获取介绍
        try:
            with codecs.open(product_path_abs + '/介绍.txt', 'r', encoding="gb18030") as f:
                introduce_text = f.read()
        except:

            # 获取介绍
            with codecs.open(product_path_abs + '/介绍.txt', 'r', encoding="utf-8") as f:
                introduce_text = f.read()
            pass



        # 获取图片路径
        img_list = glob.glob(product_path_abs + '/*.bmp')
        if not len(img_list):
            img_list = \
                glob.glob(product_path_abs + '/*.jpg') + \
                glob.glob(product_path_abs + '/*.png') + \
                glob.glob(product_path_abs + '/*.jpeg')

        product_list.append({
            'product_name': product_path_abs,
            'product_introduce': introduce_text,
            'product_image_list': img_list,
            'product_buy_key': buy_key
        })

    return product_list


def send_single_product_to_single_qun(product_dict, win_hwnd, pic_st, text_st):
    """
    向一个窗口发送一个产品
    :param product_dict:
    :param win_hwnd:
    :return:
    """

    # 发送介绍
    if len(product_dict['product_introduce']) > 0:
        send_qq_hwnd_click_string(win_hwnd, product_dict['product_introduce'])
        time.sleep(text_st)

    # 发送图片
    if len(product_dict['product_image_list']) > 0:
        for image in product_dict['product_image_list']:
            send_qq_pic(win_hwnd, image)
            time.sleep(pic_st)

    # 发送buy key
    if len(product_dict['product_buy_key']) > 0:
        send_qq_hwnd_click_string(win_hwnd, product_dict['product_buy_key'])
        time.sleep(text_st)


def split_list_average_n(origin_list, n):
    for i in range(0, len(origin_list), n):
        yield origin_list[i:i + n]


def send_all_product_to_all_qun(qun_list_, product_list, text_st, pic_st, product_st):
    """
    将所有product 发送到所有群
    :param qun_list_:
    :param product_list:
    :param sleep_time:
    :return:
    """

    # 将产品等分
    for list_sub in split_list_average_n(product_list, 3):
        for qun in qun_list_:
            try:
                for product in list_sub:

                    send_single_product_to_single_qun(product, qun, text_st=text_st, pic_st=pic_st)

                # 附带加qun推广
                # send_qq_hwnd_click_string(qun, add_qun_note)

            except Exception as e:
                print('发送商品到群出错!原因：\n' + str(e))

        time.sleep(product_st)


if __name__ == '__main__':

    # 获取产品列表
    r = get_product_info(r'C:/Users\paul\Desktop\文案')

    # 获取群列表
    qun_list = \
        list(set(get_all_win_by_name('影子')))

    send_all_product_to_all_qun(qun_list, r, 1.5, 0)



    end = 0

