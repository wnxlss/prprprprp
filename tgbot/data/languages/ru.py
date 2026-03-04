# Удаление отступов у текста
def ots(get_text: str):
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)

    return get_text


class Texts:
    ##################################                #####################################
    ##################################     /start     #####################################
    ##################################                #####################################

    # Фото, оставьте пустым если хотите убрать (прямая ссылка на фото)
    start_photo = "https://i.ibb.co/TqpHrwT0/IMG-1299.jpg"
    profile_photo = "https://i-zdrav.ru/upload/iblock/ca8/ca83b3878fa97ce94bb3ad4c375a80ce.png"
    products_photo = "https://www.bobrlife.by/wp-content/uploads/2022/04/tovary-v-krizis_0.jpg"
    faq_photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX817aptpJsuxUeCzjOizmQyc2wwoPdR9CrrZ-a7KQvEdKNAFfnCp6-wwkZUSb5XAIP_U&usqp=CAU"
    support_photo = "https://www.castcom.ru/netcat_files/114/157/castcom_support.png"
    refill_photo = "https://info.exmo.me/wp-content/uploads/2021/10/banner_rub-1032x540.png"
    contest_photo = "https://i.imgur.com/zlblPgk.jpg"

    # Стартовый текст
    start_text = """
Добро пожаловать {user_name}! Спасибо что пользуетесь нашим Магазином
Главное меню:
    """

    error_refill = "❌ Ошибка, пополнение уже произошло!"
    choose_crypto = "<b>⚙️ Выберите криптовалюту:</b>"
    ref_s = ['реферал', 'реферала', 'рефералов']  # не трогать скобки
    day_s = ['день', 'дня', "дней"]  # не трогать скобки
    member_s = ["участник", "участника", "участников"]  # не трогать скобки
    winner_s = ["победитель", "победителя", "победителей"]  # не трогать скобки
    refill_s = ["пополнение", "пополнения", "пополнений"]  # не трогать скобки
    purchase_s = ["покупка", "покупки", "покупок"]  # не трогать скобки
    channel_s = ['канал', 'канала', 'каналов']  # не трогать скобки
    conditions = "\n\n<b>❗ Условия: </b>\n\n"  # не трогать \n\n !!!
    nobody = "<code>Никто</code>"
    change_language = "🔗 Изменить язык"
    choose_language = "<b>❗ Выберите язык</b>"

    no_sub = "<b>❗ Ошибка!\nВы не подписались на канал.</b>"

    is_buy_text = "❌ Покупки временно отключены!"
    is_ban_text = f"<b>❌ Вы были заблокированы в боте!</b>"
    is_work_text = f"<b>❌ Бот находиться на тех. работах!</b>"
    is_refill_text = f"❌ Пополнения временно отключены!"
    is_ref_text = f"❗ Реферальная система отключена!"
    is_contests_text = f"❌ Розыгрыши временно отключены!"

    yes_reffer = f"<b>❗ У вас уже есть рефер!</b>"
    invite_yourself = "<b>❗ Вы не можете пригласить себя</b>"
    new_refferal = "<b>💎 У вас новый реферал! @{user_name} \n" \
                   "⚙️ Теперь у вас <code>{user_ref_count}</code> {convert_ref}!</b>"

    ##################################               #####################################
    ################################## Inline-Кнопки #####################################
    ##################################               #####################################

    # Меню пользователя
    products = "🛍️ Купить"
    profile = "👤 Профиль"
    refill = "💰 Пополнить баланс"
    faq = "📌 FAQ"
    support = "💎 Саппорт"
    back = "⬅ Вернуться"
    contest = "🎁 Розыгрыши"

    payok_text = '🪙 PayOK'
    cryptoBot_text = '💡 CryptoBot'
    qiwi_text = "🔥 Qiwi"
    yoomoney_text = "📌 ЮMoney"
    lava_text = "💰 Lava"
    lzt_text = "💚 Lolz"
    crystalPay_text = "💎 CrystalPay"
    aaio_text = "💳 Карта (РФ, УК, КЗ)"
    aaio_short_text = "Карта"  # текст должен быть не больше 18 символов!

    support_inl = "⚙️ Тех. Поддержка"

    buy = "🛍️ Купить"  # При открытии позиции

    #####################################         #####################################
    ##################################### Профиль #####################################
    #####################################         #####################################

    # Кнопки Профиля
    ref_system = "💎 Реферальная система"
    promocode = "💰 Активировать промокод"
    last_purchases_text = "⭐ Последние покупки"

    open_profile_text = """
<b>👤 Ваш Профиль:
💎 Юзер: {user_name}
🆔 ID: <code>{user_id}</code>
💰 Баланс: <code>{balance}{curr}</code>
💵 Всего пополнено: <code>{total_refill}{curr}</code>
📌 Дата регистрации: <code>{reg_date}</code>
👥 Рефералов: <code>{ref_count} чел</code></b>
"""

    last_10_purc = "⚙️ Последние 10 покупок"
    no_purcs = "❗ У вас отсутствуют покупки"
    last_purc_text = "<b>🧾 Чек: <code>{receipt}</code> \n" \
                     "💎 Товар: <code>{name} | {count}шт | {price}{curr}</code> \n" \
                     "🕰 Дата покупки: <code>{date}</code> \n" \
                     "💚 Товары: \n{link_items}</b>\n"

    promo_act = "<b>📩 Для активации промокода напишите его название</b>\n" \
                "<b>⚙️ Пример: promo2023</b>"
    no_uses_coupon = "<b>❌ Вы не успели активировать промокод!</b>"
    no_coupon = "<b>❌ Промокода <code>{coupon}</code> не существует!</b>"
    yes_coupon = "<b>✅ Вы успешно активировали промокод и получили <code>{discount}{curr}</code>!</b>"
    yes_uses_coupon = "<b>❌ Вы уже активировали данный промокод!</b>"

    new_ref_lvl = "<b>💚 У вас новый реферальный уровень, {new_lvl}! До {next_lvl} уровня осталось {remain_refs} {convert_ref}</b>"
    max_ref_lvl = f"<b>💚 У вас новый реферальный уровень, 3! Максимальный уровень!</b>"
    cur_max_lvl = f"💚 У вас максимальный уровень!</b>"
    next_lvl_remain = "💚 До следующего уровня осталось пригласить <code>{remain_refs} чел</code></b>"
    ref_text = "<b>💎 Реферальная система \n\n" \
               "🔗 Ссылка: \n" \
               "{ref_link} \n\n" \
               "📔 Наша реферальная система позволит вам заработать крупную сумму без вложений. Вам необходимо лишь давать свою ссылку друзьям и вы будете получать пожизненно <code>{ref_percent}%</code> с их пополнений в боте. \n\n" \
               "⚙️ Вас пригласил: {reffer} \n" \
               "💵 Всего заработано <code>{ref_earn}{curr}</code> с {convert_ref} \n" \
               "📌 Всего у вас <code>{ref_count}</code> {convert_ref} \n" \
               "🎲 Реферальный уровень: <code>{ref_lvl}</code> \n" \
               "{mss}"
    yes_refill_ref = "<b>💎 Ваш реферал {name} пополнил баланс на <code>{amount}{cur}</code> и с этого вам зачислено <code>{ref_amount}{cur}</code></b>"

    #####################################         #####################################
    #####################################   FAQ   #####################################
    #####################################         #####################################

    no_faq_text = "<b>⚙️ FAQ Не было настроено, обратитесь в поддержку!</b>"
    faq_chat_inl = "💎 Чат"
    faq_news_inl = "📩 Новостной"

    ################################                    ################################
    ################################   Тех. Поддержка   ################################
    ################################                    ################################

    no_support = "<b>⚙️ Владелец бота не оставил ссылку на Тех. Поддержку!</b>"
    yes_support = "<b>📩 Чтобы обратиться в Тех. Поддержку нажмите на кнопку снизу:</b>"

    #######################################
    #     Мин./Макс. Сумма пополнения     #
    #                                     #
    min_amount = 5  #
    max_amount = 100000  #
    #                                     #
    #                                     #
    #######################################

    ################################                  ################################
    ################################    Пополнения    ################################
    ################################                  ################################

    refill_text = "<b>💰 Выбери способ пополнения:</b>"
    refill_amount_text = "<b>💰 Введите сумму пополнения (От {min_amount}{curr} до {max_amount}{curr})</b>"
    refill_link_inl = "💵 Перейти к оплате"
    refill_check_inl = "💎 Проверить оплату"
    refill_check_no = "❌ Оплата не найдена"
    no_int_amount = "<b>❗ Сумма пополнения должна быть числом!</b>"
    min_max_amount = "<b>❗ Сумма пополнения должна быть больше или равна <code>{min_amount}{curr}</code> но меньше или равна <code>{max_amount}{curr}</code></b>"

    def refill_gen_text(self, way, amount, id, curr):
        msg = f"""
<b>⭐ Пополнение через: <code>{way}</code>
💰 Сумма: <code>{amount}{curr}</code>
🆔 ID платежа: <code>{id}</code>
💎 Чтобы оплатить нажмите на кнопку внизу:</b>
        """

        return ots(msg)

    def refill_success_text(self, way, amount, receipt, curr):
        msg = f"""
<b>⭐ Вы успешно пополнили баланс на сумму <code>{amount}{curr}</code>
💎 Способ: <code>{way}</code>
🧾 Чек: <code>{receipt}</code></b>
        """

        return ots(msg)

    ##########################                                 ############################
    ##########################    Открытие категорий/Товары    ############################
    ##########################                                 ############################

    open_pos_text = """
<b>💎 Категория: <code>{cat_name}</code>

🛍️ Товар: <code>{pos_name}</code>
💰 Стоимость: <code>{price}{cur}</code>
⚙️ Количество: <code>{items}</code>
🎲 Описание: </b>\n{desc}
    """

    no_cats = f"<b>К сожалению в данный момент нет категорий :(</b>"
    available_cats = f"<b>Доступные на данный момент категории:</b>"
    current_cat = "<b>Текущая категория: <code>{name}</code>:</b>"

    no_products = f"<b>К сожалению в данный момент нет товаров :(</b>"
    no_product = f"К сожалению сейчас нет данного товара :("
    gen_products = "Подготовка товаров..."

    current_pod_cat = "<b>Текущая под-категория: <code>{name}</code></b>"

    here_count_products = f"<b>❗ Введите кол-во товаров которое хотите купить:</b>"

    choose_buy_product = "<b>❓ Вы уверены что хотите купить <code>{name}</code> в кол-ве <code>1шт.</code>?</b>"
    choose_buy_products = "<b>❓ Вы уверены что хотите купить <code>{name}</code> в кол-ве <code>{amount}шт.</code>?</b>"

    no_num_count = "<b>❗ Кол-во должно быть числом!</b>"

    yes_buy_items = """
<b>✅ Вы успешно купили товар(ы)</b>

🧾 Чек: <code>{receipt}</code>
💎 Товар: <code>{name} | {amount}шт | {amount_pay}{cur}</code>
🎲 Дата: <code>{buy_time}</code>
    """

    no_balance = "❗ У вас недостаточно средств. Пополните баланс!"
    edit_prod = "<b>❗️ Товар который вы хотели купить закончился или изменился.</b>"
    otmena_buy = "<b>❗ Вы отменили покупку товаров.</b>"

    #######################                             ###########################
    #######################          Розыгрыши          ###########################
    #######################                             ###########################

    contest_text = """
<b>🎁 Розыгрыш

💰 Сумма: <code>{}{}</code>

🕒 Конец через <code>{}</code>

🎉 {} {}
👥 {} {}</b>"""

    conditions_refills = '<b>💳 {num} {refills} - {status}</b>\n'
    conditions_purchases = '<b>🛒 {num} {purchases} - {status}</b>\n'
    conditions_channels = '<b>✨ Подписаться на {num} {channels_text}: \n\n{channels}</b>\n'

    no_contests = '❗ В данный момент розыгрышей нет!'

    contest_enter = '🎉 Участвовать'

    choose_contest = "<b>❗ Выберите розыгрыш:</b>"
    u_win_the_contest = "<b>🎉 Поздравляю, вы выиграли в розыгрыше! \n💰 Приз в размере {}{} был выдан!</b>"
    u_didnt_have_time_to_enter_contest = "Вы не успели принять участие! 💥"
    success = "✅ Успешно"
    error = "⚠ Произошла ошибка, попробуйте позже!"
    u_already_enter_contest = "❌ Вы уже участвуете!"
    contest_already_ended = "💥 Розыгрыш уже завершен!"
