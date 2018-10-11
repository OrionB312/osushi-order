#########################################
# おすしプログラム
#########################################
import os
import csv

menu_num = ''
osushi_list = []

# 会話部分
def first_talk():
    print('何をしますか？')
    menu = {'1':'おすしを食べる', '2':'履歴を見る', '3':'やっぱりやめる'}
    print(menu)
    try:
        menu_num = input('番号を入力してね：')
        print('==========================================')
        print('You>「' + menu[menu_num] + '」を選択しました')
        print('==========================================')
    except KeyError:
        print('番号を入力してください')
    except Exception:
        print('最初からやり直して下さい')

    return menu_num


def todo(menu_num):
    count = 0
    price = 0
    # 選択肢ごとの分岐
    if menu_num == '1':
        osushi = input('何を食べますか？：')
        print('==========================================')
        print('You>' + osushi + 'を食べました')
        print('==========================================')

        osushi_list.append(osushi)

        with open('osushi.csv','a',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(osushi_list)
    elif menu_num == '2':
        print('履歴を表示します')
        print('==========================================')

        try:
            with open('osushi.csv','r',encoding='utf-8') as f:
                for line in f:
                    print(line, end='')
                    count += 1
                price = 108 * count
                print('合計金額は' + str(price) + '円です')
                print('==========================================')
        except FileNotFoundError:
            print('履歴がありませんよ。おすしを食べてください')
    else:
        print('さようなら')
        if os.path.exists('osushi.csv'):
            os.remove('osushi.csv')


def retire():
    print('続けますか？')
    retire_menu = {'1':'続ける', '2':'やめる'}
    print(retire_menu)
    retire_select = input('番号を入力してね：')
    print('==========================================')
    if retire_select == '2':
        print('さようなら')
        if os.path.exists('osushi.csv'):
            os.remove('osushi.csv')
    return retire_select

# メイン処理
if __name__ == '__main__':
    retire_select = 0
    while retire_select != '2':
        menu_num = first_talk()
        todo(menu_num)
        if menu_num == '3':
            break
        retire_select = retire()