def cleaning_committed(message):
    global poll_info_status

    if message.text == 'Кухня': points, half_point = 150 ,50
    else: points, half_point = 100, 50

    if not poll_info_status:

        name = message.json['from']['first_name']
        sender_id =  str(message.from_user.id)
        bot.send_poll(int(family_chat_id), f'Убрал ли {name} комнату {message.text}?',
                                  [ f'Да (+{points}б)', 'Нет(0б.)', f'50/50 (+{half_point}б.)' ], is_anonymous=False, type='regular',
                                  disable_notification=True)
        poll_info_status = True

        global poll_info_name, poll_info_place, poll_info_points,poll_info_half_points
        poll_info_name = sender_id
        poll_info_place = message.text
        poll_info_half_points = half_point


    else:
        bot.send_message(message.chat.id,'Одно голосование сейчас на проверке.Подождите, пожалуйста, а то я запутаюсь :)')



def poll_status_checker():

    global poll_info_status
    global opt_yes, opt_no, opt_mid
    global poll_info_name, poll_info_place, poll_info_points, poll_info_half_points

    if int(opt_yes) >= poll_min_number :

        bot.send_message(family_chat_id, 'Последнее голосование завершено, большинство согласно 😁')
        poll_info_status = False
        update_score(poll_info_name, poll_info_points, poll_info_place)

        opt_yes, opt_no, opt_mid = 0, 0, 0



    elif int(opt_no) >= poll_min_number - 1  :

        bot.send_message(family_chat_id,'Последнее голосование завершено, большинство не согласно 🤓')
        poll_info_status = False

        opt_yes, opt_no, opt_mid = 0, 0, 0


    elif int(opt_no) >= poll_min_number - 2 and opt_yes+opt_no+opt_mid >= poll_min_number:
        # Last poll is finished

        bot.send_message(family_chat_id, 'Последнее голосование завершено, Не все согласны. Половоина баллов за уборку зачислено 🥴 ')

        poll_info_status = False
        #  False = pole is finished so you can start a new one. True - is in progress, wait for smth

        update_score(poll_info_name, poll_info_half_points, poll_info_place)
        opt_yes, opt_no, opt_mid = 0, 0, 0

    else: pass


#  Keep tracking of a new votes in a telegram poll. Using poll_handler below
def process_new_poll_answer(poll):
    global opt_yes, opt_no, opt_mid

    answer = poll.option_ids[0]

    if answer == 0 : opt_yes += 1
    elif answer == 1 : opt_no += 1
    elif answer == 2: opt_mid +=1

@bot.poll_answer_handler(process_new_poll_answer)
def poll_answer_handler(_):
    pass


if __name__ == '__main__':

    global poll_info_status
    global opt_yes, opt_no
    opt_yes, opt_no, opt_mid= 0, 0, 0
    poll_info_status = False

    # An infinite loop: if bot loses a connection, it restarts.
    while True:
        try:

            print('Включение', str(datetime.datetime.now().time())[:8])

            thread1 = threading.Thread(target=morning_checker)
            thread1.start()

            bot.polling(none_stop=True)
        except Exception as exc:
            print('Выключение', exc, str(datetime.datetime.now().time())[:8])
            time.sleep(15)