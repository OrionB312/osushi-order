#########################################
# おすしプログラム
#########################################
import os
import csv

import utils

menu_num = ''

# メイン処理
if __name__ == '__main__':
    retire_select = 0
    while retire_select != '2':
        menu_num = utils.first_talk()
        utils.todo(menu_num)
        if menu_num == '3':
            break
        retire_select = utils.retire()