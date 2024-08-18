import keyboard as kb
import pyautogui as pgui
from pyscreeze import Box
# import telegram_bot
from time import sleep
import os

# email_value = str(input("Введите адрес электронной почты для получения hh.ru: "))
# password_value = str(input("Введите пароль: "))
# search_value = str(input("Пойск по резюме и навыкам: "))

# открывать браузер
pgui.hotkey('win')
pgui.write('microsoft edge')
pgui.hotkey('enter')
sleep(1)
pgui.hotkey("ctrl", "t")
pgui.write('https://hh.ru/')
pgui.hotkey('enter')

# # Войти в hh.ru
# sleep(5)
# login_loc = pgui.locateOnScreen('Letters\\log_in.png')
# login_button = pgui.center(login_loc)
# pgui.moveTo(login_button)
# pgui.click()

# # заполнить форму для входа в систему

# # писать email
# sleep(1)
# email_fill_loc = pgui.locateOnScreen('Letters\\fillin_email.png')
# email_fill = pgui.center(email_fill_loc)
# pgui.moveTo(email_fill)
# pgui.click()
# pgui.write('hello@uxuid.ru') # Вы можете здесь сразу ввести почту) 'hello@uxuid.ru'

# # писать пароль
# sleep(1)
# pass_fill_loc = pgui.locateOnScreen('Letters\\fillin_pass.png')
# pass_fill = pgui.center(pass_fill_loc)
# pgui.moveTo(pass_fill)
# pgui.click()
# pgui.write('N2u3NnV9') # Вы можете здесь сразу ввести пароль) 'N2u3NnV9'

# sleep(2)
# sign_in_loc = pgui.locateOnScreen('Letters\\sign_in.png')
# sign_in = pgui.center(sign_in_loc)
# pgui.moveTo(sign_in)
# pgui.click()

sleep(3)
search_loc = pgui.locateOnScreen('Letters\\search.png')
search = pgui.center(search_loc)
pgui.moveTo(search)
pgui.click()
pgui.write('programmer') # Вы можете здесь сразу ввести пойск) 'uxui designer'
pgui.hotkey('enter')

blanc_loc = pgui.locateOnScreen('Letters\\blanc.png')
blanc = pgui.center(blanc_loc)
sleep(2)
pgui.moveTo(blanc)
pgui.click()

counts = 0
while kb.is_pressed('Esc') == False:
    counts += 1

    try:
        if counts >= 10:
            print('Дальнейшие действия на странице не найдены')
            break

        star_loc = None
        try: 
            star_loc = pgui.locateOnScreen("Letters\\Star.png")
        except pgui.ImageNotFoundException:
            print('Кнопка "Star" не найдена')

        if star_loc:
            counts = 0
            star = pgui.center(star_loc)
            sleep(1)
            pgui.moveTo(star)
            pgui.click(star)

            fav_loc = pgui.locateOnScreen('Letters\\favorites.png')
            fav = pgui.center(fav_loc)
            sleep(1)
            pgui.moveTo(fav)
            pgui.click()

            save_loc = pgui.locateOnScreen('Letters\\save.png')
            save = pgui.center(save_loc)
            sleep(1)
            pgui.moveTo(save)
            pgui.click()

            limit = None
            try: 
                limit = pgui.locateOnScreen("Letters\\Limit500.png", confidence=0.9)
            except pgui.ImageNotFoundException:
                pass
            if limit != None:
                print('Превышен лимит 500')
                break

            # выбирать кандидата
            offset_loc = pgui.locateOnScreen('Letters\\offset.png', confidence=0.9)
            pgui.moveTo(offset_loc.left + offset_loc.width + 270, (offset_loc.top - 40) + offset_loc.height / 2, duration=1)
            sleep(1)
            pgui.click()

            # скролл кандидата
            pgui.sleep(3)
            print('Скролл')
            for i in range(10):
                pgui.sleep(0.2)
                pgui.scroll(-200)

            sleep(2)
            pgui.hotkey('ctrl', 'w')

            sleep(5)
            print('Скролл')
            pgui.scroll(-300)
            pgui.moveTo(132, 250)
            pgui.sleep(1)

            next_button = None
            try: 
                next_button = pgui.locateOnScreen("Letters\\Next.png", confidence=0.8)
            except pgui.ImageNotFoundException:
                print('Кнопка "Next" не найдена')

            if next_button:
                pgui.click(next_button)
                pgui.sleep(5)
            else:
                print('Скролл')
                pgui.scroll(-250)
                pgui.sleep(2)
        
    except Exception as e:
        print(f'Неизвестная ошибка\n{e}')
        break

