# Удаление отступов у текста
def ots(get_text: str):
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "":
            split_text.pop(0)
        if split_text[-1] == "":
            split_text.pop(-1)
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
Ласкаво просимо {user_name}! Дякую що користуєтесь нашим Магазином
Головне меню:
    """

    error_refill = "❌ Помилка, поповнення вже відбулося!"
    choose_crypto = "<b>⚙️ Виберіть криптовалюту:</b>"
    ref_s = ['реферал', 'реферала', 'рефералів']  # не трогать скобки
    day_s = ['день', 'дня', 'днів']  # не трогать скобки
    member_s = ["учасник", "учасника", "учасників"]  # не трогать скобки
    winner_s = ["переможець", "переможця", "переможців"]  # не трогать скобки
    refill_s = ["поповнення", "поповнення", "поповнення"]  # не трогать скобки
    purchase_s = ["купівля", "купівлі", "купівель"]  # не трогать скобки
    channel_s = ['канал', 'каналу', 'каналів']  # не трогать скобки
    conditions = "\n\n<b>❗ Умови: </b>\n\n"  # не трогать \n\n !!!
    nobody = "<code>Ніхто</code>"
    change_language = "🔗 Змінити мову"
    choose_language = "<b>❗ Виберіть мову</b>"

    no_sub = "<b>❗ Помилка!\nВи не підписалися на канал.</b>"

    is_buy_text = "❌ Покупки тимчасово вимкнено!"
    is_ban_text = f"<b>❌ Ви були заблоковані в роботі!</b>"
    is_work_text = f"<b>❌ Бот знаходиться на тих. роботах!</b>"
    is_refill_text = f"❌ Поповнення тимчасово вимкнено!"
    is_ref_text = f"❗ Реферальну систему вимкнено!"
    is_contests_text = f"❌ Розіграші тимчасово відключені!"

    yes_reffer = f"<b>❗ Ви вже маєте рефер!</b>"
    invite_yourself = "<b>❗ Ви не можете запросити себе</b>"
    new_refferal = "<b>💎 У вас новий реферал! @{user_name} \n" \
                   "⚙️ Тепер у вас є <code>{user_ref_count}</code> {convert_ref}!</b>"

    ##################################               #####################################
    ################################## Inline-Кнопки #####################################
    ##################################               #####################################

    # Меню пользователя
    products = "🛍️ Придбати"
    profile = "👤 Профіль"
    refill = "💰 Поповнити баланс"
    faq = "📌 FAQ"
    support = "💎 Тех. Підтримка"
    back = "⬅ Повернутись"
    contest = "🎁 Розіграші"

    payok_text = '🪙 PayOK'
    cryptoBot_text = '💡 CryptoBot'
    qiwi_text = "🔥 Qiwi"
    yoomoney_text = "📌 ЮMoney"
    lava_text = "💰 Lava"
    lzt_text = "💚 Lolz"
    crystalPay_text = "💎 CrystalPay"
    aaio_text = "💳 Банк. Картка (РФ, УК, КЗ)"
    aaio_short_text = "Банк. Картка" # текст должен быть не больше 18 символов!

    support_inl = "⚙️ Тех. Підтримка"

    buy = "🛍️ Придбати"  # При открытии позиции

    #####################################         #####################################
    ##################################### Профиль #####################################
    #####################################         #####################################

    # Кнопки Профиля
    ref_system = "💎 Реферальна система"
    promocode = "💰 Активувати промокод"
    last_purchases_text = "⭐ Останні покупки"

    open_profile_text = """
<b>👤 Ваш Профіль:
💎 Користувач: {user_name}
🆔 ID: <code>{user_id}</code>
💰 Баланс: <code>{balance}{curr}</code>
💵 Всього доповнено: <code>{total_refill}{curr}</code>
📌 Дата реєстрації: <code>{reg_date}</code>
👥 Рефералів: <code>{ref_count}</code></b>
"""


    last_10_purc = "⚙️ Останні 10 покупок"
    no_purcs = "❗ У вас відсутні покупки"
    last_purc_text = "<b>🧾 Чек: <code>{receipt}</code> \n" \
                     "💎 Товар: <code>{name} | {count}шт | {price}{curr}</code> \n" \
                     "🕰 Дата купівлі: <code>{date}</code> \n" \
                     "💚 Товари: \n{link_items}</b>\n"

    promo_act = "<b>📩 Для активації промокоду напишіть його назву </b>\n" \
                "<b>⚙️ Приклад: promo2023</b>"
    no_uses_coupon = "<b>❌ Ви не встигли активувати промокод!</b>"
    no_coupon = "<b>❌ Промокоду <code>{coupon}</code> не існує!</b>"
    yes_coupon = "<b>✅ Ви успішно активували промокод та отримали <code>{discount}{curr}</code>!</b>"
    yes_uses_coupon = "<b>❌ Ви вже активували цей промокод!</b>"

    new_ref_lvl = "<b>💚 У вас є новий реферальний рівень, {new_lvl}! До рівня {next_lvl} залишилося {remain_refs} {convert_ref}</b>"
    max_ref_lvl = f"<b>💚 У вас є новий реферальний рівень, 3! Максимальний рівень!</b>"
    cur_max_lvl = f"💚 У вас максимальний рівень!</b>"
    next_lvl_remain = "💚 До наступного рівня залишилося запросити <code>{remain_refs} осіб</code></b>"
    ref_text = "<b>💎 Реферальная система \n\n" \
               "🔗 Посилання: \n" \
               "{ref_link} \n\n" \
               "📔 Наша реферальна система дозволить заробити велику суму без вкладень. Вам необхідно лише давати своє посилання друзям і ви отримуватимете довічно <code>{ref_percent}%</code> з їх поповнення в боті. \n\n" \
               "⚙️ Вас запросив: {reffer} \n" \
               "💵 Усього зароблено <code>{ref_earn}{curr}</code> с {convert_ref} \n" \
               "📌 Усього у вас <code>{ref_count}</code> {convert_ref} \n" \
               "🎲 Реферальний рівень: <code>{ref_lvl}</code> \n" \
               "{mss}"
    yes_refill_ref = "<b>💎 Ваш реферал {name} поповнив баланс на <code>{amount}{cur}</code> і з цього вам зараховано <code>{ref_amount}{cur}</code></b>"

    #####################################         #####################################
    #####################################   FAQ   #####################################
    #####################################         #####################################

    no_faq_text = "<b>⚙️ FAQ Не було налаштовано, зверніться до підтримки!</b>"
    faq_chat_inl = "💎 Чат"
    faq_news_inl = "📩 Новинний"

    ################################                    ################################
    ################################   Тех. Поддержка   ################################
    ################################                    ################################

    no_support = "<b>⚙️ Власник робота не залишив посилання на Тех. Підтримка!</b>"
    yes_support = "<b>📩 Щоб звернутися до Тех. Підтримку натисніть кнопку знизу:</b>"

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

    refill_text = "<b>💰 Вибери спосіб поповнення:</b>"
    refill_amount_text = "<b>💰 Введіть суму поповнення (Від {min_amount}{curr} до {max_amount}{curr})</b>"
    refill_link_inl = "💵 Перейти до оплати"
    refill_check_inl = "💎 Перевірити оплату"
    refill_check_no = "❌ Оплати не знайдено"
    no_int_amount = "<b>❗ Сума поповнення має бути числом!</b>"
    min_max_amount = "<b>❗ Сума поповнення має бути більшою або дорівнює <code>{min_amount}{curr}</code> але меншою або дорівнює <code>{max_amount}{curr}</code></b>"

    def refill_gen_text(self, way, amount, id, curr):
        msg = f"""
<b>⭐ Поповнення через: <code>{way}</code>
💰 Сума: <code>{amount}{curr}</code>
🆔 ID платежу: <code>{id}</code>
💎 Щоб сплатити, натисніть кнопку внизу:</b>
        """

        return ots(msg)

    def refill_success_text(self, way, amount, receipt, curr):
        msg = f"""
<b>⭐ Ви успішно поповнили баланс на суму <code>{amount}{curr}</code>
💎 Спосіб: <code>{way}</code>
🧾 Чек: <code>{receipt}</code></b>
        """

        return ots(msg)

    ##########################                                 ############################
    ##########################    Открытие категорий/Товары    ############################
    ##########################                                 ############################

    open_pos_text = """
<b>💎 Категорія: <code>{cat_name}</code>

🛍️ Товар: <code>{pos_name}</code>
💰 Вартість: <code>{price}{cur}</code>
⚙️ Кількість: <code>{items}</code>
🎲 Опис: </b>
{desc}
    """

    no_cats = f"<b>На жаль, на даний момент немає категорій :(</b>"
    available_cats = f"<b>Доступні на даний момент категорії:</b>"
    current_cat = "<b>Поточна категорія: <code>{name}</code>:</b>"

    no_products = f"<b>На жаль на даний момент немає товарів :(</b>"
    no_product = f"На жаль зараз немає даного товару :("
    gen_products = "Підготовка товарів..."

    current_pod_cat = "<b>Поточна підкатегорія: <code>{name}</code></b>"

    here_count_products = f"<b>❗ Введіть кількість товарів, які хочете купити:</b>"

    choose_buy_product = "<b>❓ Ви впевнені, що хочете купити <code>{name}</code> у кількості <code>1шт.</code>?</b>"
    choose_buy_products = "<b>❓ Ви впевнені, що хочете купити <code>{name}</code> у кількості <code>{amount}шт.</code>?</b>"

    no_num_count = "<b>❗ Кількість має бути числом!</b>"

    yes_buy_items = """
<b>✅ Ви успішно купили товар(и)</b>

🧾 Чек: <code>{receipt}</code>
💎 Товар: <code>{name} | {amount}шт | {amount_pay}{cur}</code>
🎲 Дата: <code>{buy_time}</code>
    """

    no_balance = "❗ У вас недостатньо коштів. Поповніть баланс!"
    edit_prod = "<b>❗️ Товар, який ви хотіли купити, закінчився або змінився.</b>"
    otmena_buy = "<b>❗ Ви скасували покупку товарів.</b>"

    #######################                             ###########################
    #######################          Розыгрыши          ###########################
    #######################                             ###########################

    contest_text = """
<b>🎁 Розіграш

💰 Сума: <code>{}{}</code>

🕒 Кінець через <code>{}</code>

🎉 {} {}
👥 {} {}</b>"""

    conditions_refills = '<b>💳 {num} {refills} - {status}</b>\n'
    conditions_purchases = '<b>🛒 {num} {purchases} - {status}</b>\n'
    conditions_channels = '<b>✨ Підписатися на {num} {channels_text}: \n\n{channels}</b>'

    no_contests = '❗ На даний момент розіграшів немає!'

    contest_enter = '🎉 Брати участь'

    choose_contest = "<b>❗ Виберіть розіграш:</b>"
    u_win_the_contest = "<b>🎉 Вітаю, ви виграли у розіграші! \n💰 Приз у розмірі {}{} був виданий!</b>"
    u_didnt_have_time_to_enter_contest = "Ви не встигли взяти участь! 💥"
    success = "✅ Успішно"
    error = "⚠ Сталася помилка, спробуйте пізніше!"
    u_already_enter_contest = "❌ Ви вже берете участь!"
    contest_already_ended = "💥 Розіграш вже завершено!"